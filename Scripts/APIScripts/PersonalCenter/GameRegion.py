# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
import requests


class GameRegion:
    """
    获取游戏大区
    """
    def game_region(self, game_id):
        """
        获取大区
        :return:
        """
        post_data = {"gameId": "%d" % game_id}
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
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'获取游戏大区', u"get", game_region_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    r = GameRegion()
    print(r.game_region(1))