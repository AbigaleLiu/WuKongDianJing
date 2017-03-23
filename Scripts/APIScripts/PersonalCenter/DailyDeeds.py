# _*_ coding:utf-8 _*_

import requests

from Scripts.APIScripts.Other.Login import *


class DailyDeed:
    """
    获取日常任务列表
    """
    def daily_deed(self, login):
        """
        日常任务接口，GET
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
        daily_deed_url = "http://%s/usertask/daily" % ConfigFile().host()
        request = requests.get(daily_deed_url, headers=headers)
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
            log_list = [u'日常任务', u"get", daily_deed_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    login = Login().login("18708125571", "aaaaaa")
    r = DailyDeed()
    print(r.daily_deed(login))
