# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class BanList:
    """
    获取对手选择的英雄/地图列表
    """
    def ban_list(self, login, id, screenings):
        post_data = {"screenings": "%d" % screenings}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        ban_list_url = "http://%s/activity/%d/banheros" % (ConfigFile().host(), id)
        request = requests.get(ban_list_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        print(ban_list_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'获取对手选择的英雄或地图', u"get", ban_list_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    login = Login().login("18708125570", "aaaaaa")
    _run = BanList()
    print(_run.ban_list(login, 19, 1))