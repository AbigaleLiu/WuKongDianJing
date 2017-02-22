# _*_ coding:utf-8 _*_
from GameRegion import *
from Scripts.GetReport import *
class AddRole:
    """
    添加游戏角色
    """
    def add_role(self, login, game_region):
        """
        添加游戏角色
        :param login:
        :param game_region: 游戏大区编号
        :return:
        """
        post_data = {"gameId": "%s" % game_region["game_id"],
                     "gamePlayer": "%s" % ConfigFile().game_role_name(),
                     "gameServiceId": "%s" % game_region["region_id"]}
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


def main():
    login = Login().login("18708125570", "aaaaaa")
    r = AddRole()
    game_region = GameRegion().game_region()
    print r.add_role(login, game_region)
if __name__ == "__main__":
    main()
