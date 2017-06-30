import requests
from Scripts.GetReport import *
from Scripts.APIScripts.Other.Login import *
from Scripts.ConfigFile import *
from Scripts.GetTime import *


class MatchStatus:
    def __init__(self, judgement_token):
        self.judgement_token = judgement_token
        self.match_id = ConfigFile().activity_id()

    def match_status(self):
        """
        获取比赛状态
        :param token:
        :param match_id:
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': self.judgement_token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        match_status_url = "http://%s/activity/%d/checkuseractstatus" % (ConfigFile().host(), self.match_id)
        request = requests.get(match_status_url, data=post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'获取比赛状态', u"get", match_status_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def get_match_status(self):
        """
        返回比赛状态，1-报名中  2-比赛中  3-已结束
        :return: match_status
        """
        status_data = self.match_status()["data"]
        if status_data:
            match_status = status_data["match_status"]
            return match_status


if __name__ == '__main__':
    token = Login().login("14700000001", "aaaaaa")["data"]["auth_token"]
    _run = MatchStatus(token)
    print(_run.get_match_status())
