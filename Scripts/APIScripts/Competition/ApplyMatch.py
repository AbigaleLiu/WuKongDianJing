# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.PersonalCenter.RoleList import *
from Scripts.APIScripts.Other.Login import *


class ApplyMatch:
    """
    报名比赛
    """
    def apply_match(self, login, id, role_id, password=""):
        """
        报名比赛
        :param login: json，获取token
        :param id: 赛事ID
        :param role_id: 角色ID
        :param password: 房间密码
        :return: json
        """
        post_data = {"id": "%d" % id,
                     "roleId": "%d" % role_id,
                     "password": "%s" % password}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        apply_match_url = "http://%s/activity/%s/sign" % (ConfigFile().host(), id)
        request = requests.post(apply_match_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'报名比赛', u"post", apply_match_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    id = 99  # 赛事ID
    users = GetUsers().get_users()
    for user in range(len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        print(login)
        if RoleList().role_list(login)["data"]:
            print(RoleList().role_list(login)["data"])
            role_id = RoleList().role_list(login)["data"][-1]["id"]
            _run = ApplyMatch()
            print(_run.apply_match(login, id, role_id, "111111"))