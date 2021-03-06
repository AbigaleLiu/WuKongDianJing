# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class MatchPeople:
    """
    创建比赛-人数方案
    """
    def match_people(self, judgement_token, game_id):
        post_data = {"gameId": "%d" % game_id}  # 游戏ID
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': judgement_token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        match_people_url = "http://%s/activity/people" % ConfigFile().host()
        request = requests.get(match_people_url, post_data, headers=headers)
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
            log_list = [u'创建比赛-人数方案', u"get", match_people_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    judgement_token = Login().login("18708125570", "aaaaaa")["data"]["auth_token"]
    _run = MatchPeople()
    print(_run.match_people(judgement_token, 1))
    print(_run.match_people(judgement_token, 1)["data"][0]["count"])