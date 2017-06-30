# _*_ coding:utf-8 _*_
import requests
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class AppraiseStar:
    """
    评价-星级
    """
    def __init__(self):
        confing_file = ConfigFile()
        self.match_id = confing_file.activity_id()
        self.star = confing_file.whether_appraise()

    def appraise_star(self, token):
        """
        :param login:
        :param id:
        :param star: 星级
        :return:
        """
        post_data = {"star": "%d" % self.star}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        appraise_star_url = "http://%s/activity/%d/star" % (ConfigFile().host(), self.match_id)
        request = requests.post(appraise_star_url, post_data, headers=headers)
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
            log_list = [u'评价-星级', u"post", appraise_star_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    token = Login().login("14700000003", "aaaaaa")["data"]["auth_token"]
    _run = AppraiseStar()
    print(_run.appraise_star(token))