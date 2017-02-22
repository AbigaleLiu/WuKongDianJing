# _*_ coding:utf-8 _*_
import requests
from Scripts.APIScripts.Other.Login import *
from Scripts.GetCurrentTime import *
from Scripts.ConfigFile import *
from RoleList import *
class DeleteRole:
    """
    删除已绑定的游戏角色
    """
    def delete_role(self, login):
        """
        删除角色
        :param login:
        :return:
        """
        post_data = {"roleId": ""}
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
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'删除角色', u"delete", delete_role_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


def main():
    login = Login().login("18708125570", "aaaaaa")
    r = DeleteRole()
    print r.delete_role(login)
    print RoleList().role_list(login)

if __name__ == '__main__':
    main()