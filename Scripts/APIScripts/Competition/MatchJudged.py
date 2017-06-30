# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class MatchJudged:
    """
    我裁定的比赛，即被添加为附加裁判
    """
    def match_judged(self, token, match_status, page):
        """

        :param token:
        :param match_status: 1-报名中  2-比赛中  3-已结束
        :param page:分页
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        match_judged_url = "http://%s/activity/referee/%d?p=%d" % (ConfigFile().host(), match_status, page)
        request = requests.get(match_judged_url, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        print(match_judged_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'我裁定的', u"get", match_judged_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    token = Login().login("14700000002", "aaaaaa")["data"]["auth_token"]
    _run = MatchJudged()
    print(_run.match_judged(token, 3, 1))
