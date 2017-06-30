from Scripts.APIScripts.Other.Login import *
from Scripts.ConfigFile import *


class SignList:
    """
    获取报名用户
    """
    def __init__(self):
        config_file = ConfigFile()
        self.judgement_token = Login().login(config_file.judgement()[0], config_file.judgement()[1])["data"]["auth_token"]
        self.match_id = config_file.activity_id()

    def sign_list(self, wheather_main_draw=None, page=None):
        """
        获取报名用户
        :param wheather_main_draw:None（获取全部）；0（获取正选）；1（获取候补）
        :param page:分页
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                    "Content - Type": "text / html;charset = UTF - 8",
                    'Accept': 'application/json',
                    'Authorization': self.judgement_token,
                    "Date": "%s" % GetCurrentTime().getHeaderTime(),
                    "Proxy - Connection": "Keep - alive",
                    "Server": "nginx / 1.9.3(Ubuntu)",
                    "Transfer - Encoding": "chunked"}
        if wheather_main_draw:
            sign_list_url = "http://%s/activity/%d/signlist/%d?p=%d" % (ConfigFile().host(), self.match_id, wheather_main_draw, page)
        else:
            sign_list_url = "http://%s/activity/%d/signlist" % (ConfigFile().host(), self.match_id)
        request = requests.get(sign_list_url, headers=headers)
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
            log_list = [u'获取报名用户', u"get", sign_list_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
    _run = SignList()
    print(_run.sign_list())
