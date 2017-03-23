# _*_ coding:utf-8 _*_

from Scripts.APIScripts.Other.Login import *
from Scripts.GetUsers import *


class Record:
    """
    任务完成情况
    """
    def record(self, login):
        """
        日常完成任务记录与统计接口，GET
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        record_url = "http://%s/usertask/record" % ConfigFile().host()
        time = GetCurrentTime().getCurrentTime()
        request = requests.get(record_url, headers=headers)
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
            log_list = [u'日常任务完成情况', u"get", record_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    login = Login().login("18708125571", "aaaaaa")
    r = Record()
    print(r.record(login))
