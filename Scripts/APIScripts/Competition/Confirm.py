# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class Confirm:
    """
    确认参赛
    """
    def confirm(self, login, id):
        """
        确认参赛
        :param login: json格式，获取token
        :param id: 赛事ID
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        confirm_url = "http://%s/activity/%d/confirm" % (ConfigFile().host(), id)
        request = requests.put(confirm_url, data=post_data, headers=headers)
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
            log_list = [u'确认参赛', u"put", confirm_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    users = GetUsers().get_users()
    for user in range(len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        print(login)
        _run = Confirm()
        print(_run.confirm(login, 96))