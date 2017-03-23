# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class AppraiseStar:
    """
    评价-星级
    """
    def appraise_star(self, login, id, star):
        """
        :param login:
        :param id:
        :param star: 星级
        :return:
        """
        post_data = {"star": "%d" % star}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        appraise_star_url = "http://%s/activity/%d/star" % (ConfigFile().host(), id)
        request = requests.post(appraise_star_url, post_data, headers=headers)
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
            log_list = [u'评价-星级', u"post", appraise_star_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    login = Login().login("18708125570", "aaaaaa")
    _run = AppraiseStar()
    print(_run.appraise_star(login, 1, 1))