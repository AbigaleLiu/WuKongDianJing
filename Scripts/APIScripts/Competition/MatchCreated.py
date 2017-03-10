# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.ConfigFile import *
from Scripts.GetReport import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Other.Login import *


class MatchCreated:
    """
    我发布的比赛
    """
    def match_created(self, login, status, page, row):
        post_data = {"status": "%d" % status,  # 比赛状态：1未开始；2进行中；3已结束
                     "page": "%d" % page,  # 页数
                     "row": "%d" % row}  # 条数
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        match_created_url = "http://%s/creatematch" % ConfigFile().host()
        request = requests.get(match_created_url, post_data, headers=headers)
        # return request.reason
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取角色列表', u"get", match_created_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == '__main__':
    login = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
    _run = MatchCreated()
    print(_run.match_created(login, 1, 1, 10))