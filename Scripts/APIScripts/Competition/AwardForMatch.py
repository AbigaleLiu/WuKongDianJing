# _*_ coding:utf-8 _*_
import requests
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class AwardForMatch:
    """
    赛事蟠桃使用规则
    """
    def award_for_match(self, token):
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        award_for_match_url = "http://%s/activity/goldrule" % ConfigFile().host()
        request = requests.get(award_for_match_url, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        print(award_for_match_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'我裁定的', u"get", award_for_match_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    token = Login().login("14700000002", "aaaaaa")["data"]["auth_token"]
    _run = AwardForMatch()
    print(_run.award_for_match(token))
