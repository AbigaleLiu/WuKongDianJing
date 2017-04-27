# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.BanList import *


class CheckPassword:
    """
    检测赛事房间密码
    """
    def check_password(self, login, id, password):
        post_data = {"password": "%d" % password}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        check_password_url = "http://%s/activity/%d/checkpassword" % (ConfigFile().host(), id)
        request = requests.post(check_password_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        print(check_password_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交房间密码', u"post", check_password_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    id = 159  # 赛事ID
    password = 123456
    users = GetUsers().get_users()
    for user in range(len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        _run = CheckPassword()
        print(_run.check_password(login, id, password))