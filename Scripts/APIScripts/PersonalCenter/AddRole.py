# _*_ coding:utf-8 _*_
import requests
from Scripts.APIScripts.PersonalCenter.GameRegion import *
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
from Scripts.ConfigFile import *
from Scripts.GetCurrentTime import *
from Scripts.GetUsers import *


class AddRole:
    """
    添加游戏角色
    """
    def add_role(self, login, game_id, name):
        """
        添加游戏角色
        :param login:登录
        :param game_id: 游戏编号
        :return:
        """
        post_data = {"gameId": "%d" % game_id,
                     "gamePlayer": "%s" % name,#% ConfigFile().game_role_name(game_id),
                     "gameServiceId": '146'}#"%s" %  GameRegion().game_region(game_id)["data"][0]["id"]}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        add_role_url = "http://%s/usergames/addRole" % ConfigFile().host()
        request = requests.post(add_role_url, data=post_data, headers=headers)
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
            log_list = [u'添加游戏角色', u"post", add_role_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    users = GetUsers().get_users()
    roles = []
    for i in range(661, 722):
        role = "i"+str(i)+"#"+"8%d" % i
        roles.append(role)
    for user in range(61, len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        print(login)
        r = AddRole()
        print(roles[user-61])
        print(r.add_role(login, 1, roles[user-61]))