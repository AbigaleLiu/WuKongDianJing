# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class Against:
    """
    获取对阵表
    """
    def against(self, login, id, screening=None):
        post_data = {"screenings": screening}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        against_url = "http://%s/activity/%d/against" % (ConfigFile().host(), id)
        request = requests.get(against_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        print(request)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'对阵表', u"get", against_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    login = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
    _run = Against()
    print(_run.against(login, 19, 2))