# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
class GameRegion:
    """
    获取游戏大区
    """
    def game_region(self):
        """
        获取大区
        :return:
        """
        post_data = {"gameId": "%d" % random.randint(1, 3)}  # 1：炉石；2：英雄联盟；3：守望
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        game_region_url = "http://%s/games/service" % ConfigFile().host()
        request = requests.get(game_region_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取游戏大区', u"get", game_region_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


def main():
    r = GameRegion()
    print r.game_region()
if __name__ == "__main__":
    main()
