# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.BanList import *


class Ban:
    """
    提交禁选的英雄/地图
    """
    def ban(self, login, id, screenings, heros):
        post_data = {"screenings": "%d" % screenings,
                     "heros": "%s" % heros}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        ban_url = "http://%s/activity/%d/ban" % (ConfigFile().host(), id)
        request = requests.put(ban_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        # print(ban_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交禁选的英雄或地图', u"put", ban_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志

    def ban_heros(self, login):
        pick_data = BanList().ban_list(login, id, screenings)["data"]
        if type(pick_data) is dict:
            pick_list = []
            sign_num = pick_data["sign_num"]
            for i in range(len(pick_data["list"])):
                pick_list.append(pick_data["list"][i]["id"])
            heros_list = [random.choice(pick_list) for i in range(int(sign_num))]
            heros = ""
            for hero in heros_list:
                heros = heros + str(hero) + ","
            return heros


if __name__ == '__main__':
    id = 76  # 赛事ID
    screenings = 1  # 轮次
    users = GetUsers().get_users()
    for user in range(6,80):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        _run = Ban()
        print(_run.ban(login, id, screenings, "11,15"))
