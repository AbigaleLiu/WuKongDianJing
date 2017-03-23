# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class DisputeJudge:
    """
    争议处理
    """
    def dispute_judge(self, login, id, dispute_id ,winner_id):
        """

        :param login:
        :param id:
        :param dispute_id:
        :param winner_id:获胜者id
        :return:
        """
        post_data = {"won": "%d" % winner_id}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        dispute_judge_url = "http://%s/activity/%d/dispute/%d/judgment" % (ConfigFile().host(), id, dispute_id)
        request = requests.post(dispute_judge_url, post_data, headers=headers)
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
            log_list = [u'争议处理', u"post", dispute_judge_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    login = Login().login("18708125570", "aaaaaa")
    _run = DisputeJudge()
    print(_run.dispute_judge(login, 1, 1, 1))