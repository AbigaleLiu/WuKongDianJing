# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.PickList import *


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
        print(pick_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交选择的英雄或地图', u"post", pick_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    id = 96  # 赛事ID
    screenings = 1  # 轮次
    users = GetUsers().get_users()
    for user in range(len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        pick_list = PickList().pick_list(login, id, screenings)["data"]["list"]
        print(pick_list)
        # print(login)
        # _run = Pick()
        # print(_run.pick(login, id, 1, ""))
