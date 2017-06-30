# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class PickList:
    """
    获取可选择的英雄/地图列表
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        self.screening = config_file.get_current_screening()

    def pick_list(self, token):
        post_data = {"screenings": "%d" % self.screening}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        pick_list_url = "http://%s/activity/%d/signheros" % (ConfigFile().host(), self.match_id)
        request = requests.get(pick_list_url, post_data, headers=headers)
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
            log_list = [u'选英雄或地图', u"get", pick_list_url, str(post_data), time, status_code, info]  # 单条日志记录
            print(log_list)
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    # token = Login().login("14700000004", "aaaaaa")["data"]["auth_token"]
    _run = PickList()
    # for token in ConfigFile().get_token():
    #     print(_run.pick_list(token))
    result = []
    pool = mul_t.Pool(processes=100)
    for token in ConfigFile().get_token():
        result.append(pool.apply_async(func=_run.pick_list, args=(token,)))
    for r in result:
        print(r.get())
