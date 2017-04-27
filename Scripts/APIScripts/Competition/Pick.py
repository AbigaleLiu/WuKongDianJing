# _*_ coding:utf-8 _*_
import requests
import random
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.PickList import *
from Scripts.GetReport import GetReport

from Scripts.GetCurrentTime import GetCurrentTime

from Scripts.GetUsers import GetUsers

from Scripts.APIScripts.Other.Login import Login


class Pick:
    """
    提交选择的英雄/地图
    """
    def pick(self, login, id, screenings, heros):
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
        pick_url = "http://%s/activity/%d/bpsign" % (ConfigFile().host(), id)
        request = requests.post(pick_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交选择的英雄或地图', u"post", pick_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def pick_heros(self, login):
        pick_data = PickList().pick_list(login, id, screenings)["data"]
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
    for user in range(2, 120):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        _run = Pick()
        heros = _run.pick_heros(login)
        print(_run.pick(login, id, screenings, "11,12,13,14,15"))
