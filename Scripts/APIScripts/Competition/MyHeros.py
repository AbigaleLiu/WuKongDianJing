# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class MyHeros:
    """
    已选择（已被ban）的英雄
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        self.screening = config_file.get_current_screening()

    def my_heros(self, token):
        post_data = {"screenings": "%d" % self.screening}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        my_heros_url = "http://%s/activity/%d/myheros" % (ConfigFile().host(), self.match_id)
        request = requests.get(my_heros_url, data=post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                return info
        finally:
            log_list = [u'已选英雄或地图', u"get", my_heros_url, str(post_data), time, status_code, info]  # 单条日志记录
            print(log_list)
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    # token = Login().login("14700000004", "aaaaaa")["data"]["auth_token"]
    _run = MyHeros()
    for token in ConfigFile().get_token():
        print(_run.my_heros(token))

