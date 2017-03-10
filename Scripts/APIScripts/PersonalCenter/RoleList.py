# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.PersonalCenter.AddRole import *
class RoleList:
    """
    获取所有游戏角色列表
    """
    def role_list(self, login):
        """
        获取游戏角色列表
        :param login:
        :return:
        """
        post_data = {"gameId": ""}  # 选填，填写后选择的游戏角色优先显示
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "page": "",  # 分页，有默认值
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        role_list_url = "http://%s/usergames/rolelist" % ConfigFile().host()
        request = requests.get(role_list_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取角色列表', u"get", role_list_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == "__main__":
    login = Login().login("18708125570", "aaaaaa")
    print("add:")
    print(AddRole().add_role(login, 1))
    print("rolelist:")
    r = RoleList()
    print(r.role_list(login))
