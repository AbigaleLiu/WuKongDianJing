# _*_ coding:utf-8 _*_
import requests
from Scripts.APIScripts.Other.Login import *
from Scripts.GetCurrentTime import *
from Scripts.ConfigFile import *
from Scripts.APIScripts.PersonalCenter.RoleList import *
class DeleteRole:
    """
    删除已绑定的游戏角色
    """
    def delete_role(self, login, role_id):
        """
        删除角色
        :param login:
        :return:
        """
        post_data = {"roleId": "%d" % role_id}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        delete_role_url = "http://%s/usergmaes/deleteRole" % ConfigFile().host()
        request = requests.delete(delete_role_url, data=post_data, headers=headers)
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
            log_list = [u'删除角色', u"delete", delete_role_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    users = GetUsers().get_users()
    for user in range(len(users)):
        login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
        # print(login)
        r = DeleteRole()
        if RoleList().role_list(login)["data"]:
            role_id = RoleList().role_list(login)["data"][-1]["id"]
            print(r.delete_role(login, role_id))
