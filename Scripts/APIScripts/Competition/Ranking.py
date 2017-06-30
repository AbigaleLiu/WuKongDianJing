# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class Ranking:
    """
    获取比赛排名
    """
    def __init__(self):
        config_file = ConfigFile()
        self.judgement_token = Login().login(config_file.judgement()[0], config_file.judgement()[1])["data"]["auth_token"]
        self.match_id = config_file.activity_id()

    def ranking(self, page):
        """
        获取某一比赛排名
        :param page: 分页
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': self.judgement_token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        ranking_url = "http://%s/activity/%d/rank?p=%d" % (ConfigFile().host(), self.match_id, page)
        request = requests.get(ranking_url, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        print(request)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'比赛排名', u"get", ranking_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    login = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
    _run = Ranking()
    print(_run.ranking())