# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class Confirm:
    """
    确认参赛
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()

    def confirm(self, token):
        """
        确认参赛
        :param login: json格式，获取token
        :param id: 赛事ID
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        confirm_url = "http://%s/activity/%d/confirm" % (ConfigFile().host(), self.match_id)
        request = requests.put(confirm_url, data=post_data, headers=headers)
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
            log_list = [u'确认参赛', u"put", confirm_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    result = []
    pool = mul_t.Pool(processes=100)
    tokens = ConfigFile().get_token()
    for token in tokens:
        result.append(pool.apply_async(func=Confirm().confirm, args=(token,)))
    pool.close()
    pool.join()
    for r in result:
        print(r.get())
