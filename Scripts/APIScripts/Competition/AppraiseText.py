import requests
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.AppraiseItem import *


class AppraiseText:
    """
    评价内容
    """
    def __init__(self, token):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        self.token = token

    def appraise_text(self, text=""):
        post_data = {"item": "%d" % self.item(),
                     "explain": "%s" % text}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': self.token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        appraise_text_url = "http://%s/activity/%d/feedback" % (ConfigFile().host(), self.match_id)
        request = requests.put(appraise_text_url, post_data, headers=headers)
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
            log_list = [u'评价内容', u"put", appraise_text_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def item(self):
        """
        随机选择一项反馈选项ID
        :return:
        """
        item_json = AppraiseItem().appraise_item(self.token)
        item_data = item_json["data"]
        if item_data:
            for i in range(len(item_data)):
                item = random.choice([item_data[i]["id"]])
                return item
        else:
            print(item_json["info"])


if __name__ == '__main__':
    token = Login().login("14700000003", "aaaaaa")["data"]["auth_token"]
    _run = AppraiseText(token)
    print(_run.item())
    print(_run.appraise_text(token))