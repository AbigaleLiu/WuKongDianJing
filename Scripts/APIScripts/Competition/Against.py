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
    def against_page(self, token, match_id, screening, page):
        post_data = {"screenings": screening}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        against_url = "http://%s/activity/%d/against?p=%d" % (ConfigFile().host(), match_id, page)
        request = requests.get(against_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'对阵表', u"get", against_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def against(self, token, match_id, screening):
        """
        将不同分页的对阵表数据处理，提取完整的对阵表ID
        :param token:
        :param match_id:
        :param screening:
        :return: 二维列表
        """
        page = 1
        against_data = []
        while page >= 1:
            against_page = self.against_page(token, match_id, screening, page)
            if against_page["data"]:
                for user in against_page["data"]:
                    pairs = [user["users"][0]["uid"], user["users"][1]["uid"]]
                    against_data.append(pairs)
                page = page + 1
            else:
                break
        return against_data


if __name__ == '__main__':
    login = Login().login("14700000001", "aaaaaa")
    _run = Against()
    # print(_run.against_page(login["data"]["auth_token"], 53, 2))
    print(_run.against(login["data"]["auth_token"], 53, 2))

