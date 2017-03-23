# _*_ coding:utf-8 _*_
import requests
from Scripts.GetReport import *
from Scripts.GetCurrentTime import *


class Register:
    """
    注册
    """
    def register(self, mobile, password, code):
        """
        注册
        :param mobile:
        :param password:
        :param code:验证码
        :return:
        """
        post_data = {"mobile": "%s" % mobile,
                     "password": "%s" % password,
                     "code": "%s" % code}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        register_url = "http://%s/user/register" % ConfigFile().host()
        request = requests.post(register_url, data=post_data, headers=headers)
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
            log_list = [u'注册', u"post", register_url , str(post_data), time, status_code, info]
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    r = Register()
    print(r.register("18708125576", "aaaaaa", ""))