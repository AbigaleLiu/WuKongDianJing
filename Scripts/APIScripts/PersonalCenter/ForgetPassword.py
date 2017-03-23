# _*_ coding:utf-8 _*_
import requests
from Scripts.GetReport import *
from Scripts.ConfigFile import *
from Scripts.GetCurrentTime import *


class ForgetPassword:

    def forget_password(self, mobile, password, code):
        """
        :param mobile:
        :param password:
        :param code: 忘记密码验证码
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
        forget_password_url = "http://%s/user/forget" % ConfigFile().host()
        request = requests.put(forget_password_url, data=post_data, headers=headers)
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
            log_list = [u'忘记密码', u"put", forget_password_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    r = ForgetPassword()
    print(r.forget_password("18708125571", "123456", ""))
