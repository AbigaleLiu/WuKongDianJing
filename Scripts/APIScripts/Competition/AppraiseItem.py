# _*_ coding:utf-8 _*_
import requests
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class AppraiseItem:
    """
    评价-评价项（评星小于等于2星时出现）
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()

    def appraise_item(self, token):
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        appraise_item_url = "http://%s/activity/%d/feeditem" % (ConfigFile().host(), self.match_id)
        request = requests.get(appraise_item_url, post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
                # pass
        finally:
            log_list = [u'评价-星级', u"get", appraise_item_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    token = Login().login("14700000001", "aaaaaa")["data"]["auth_token"]
    _run = AppraiseItem()
    print(_run.appraise_item(token))