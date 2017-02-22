# _*_ coding:utf-8 _*_
import requests
from Scripts.ConfigFile import *
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *


class QQLogin:
    def qq_login(self, openid):
        """
        QQ登录
        :param openid:
        :return:
        """
        post_data = {"type": "qq",  # QQ: 'qq'; 微信: 'weixin'
                     "openid": openid,  # 第三方平台的唯一标识
                     "auth_token": ""  # 第三方平台的授权码
                     }
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        third_login_url = "http://%s/user/thirdlogin" % ConfigFile().host()
        request = requests.post(third_login_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'QQ登录', u"post", third_login_url , str(post_data), time, status_code, info]
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


def main():
    r = QQLogin()
    print r.qq_login("openid")
if __name__ == "__main__":
    main()
