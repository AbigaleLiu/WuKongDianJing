# _*_ coding:utf-8 _*_
from Scripts.APIScripts.PersonalCenter.GameRegion import *
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
from Scripts.ConfigFile import *
from Scripts.GetCurrentTime import *


class AddRole:
    """
    添加游戏角色
    """
    def add_role(self, login, game_id):
        """
        添加游戏角色
        :param login:登录
        :param game_id: 游戏编号
        :return:
        """
        post_data = {"gameId": "%d" % game_id,
                     "gamePlayer": "%s" % ConfigFile().game_role_name(game_id),
                     "gameServiceId": "%s" % GameRegion().game_region(game_id)["data"][0]["id"]}
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
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'添加游戏角色', u"post", add_role_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == "__main__":
    login = Login().login("18708125570", "aaaaaa")
    r = AddRole()
    print(r.add_role(login, 1))