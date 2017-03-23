# _*_ coding:utf-8 _*_
import requests
from Scripts.GetReport import *
from Scripts.GetCurrentTime import *

class WeixinLogin:
    def weixin_login(self, openid):
        """
        微信登录
        :param openid:
        :return:
        """
        post_data = {"type": "weixin",  # QQ: 'qq'; 微信: 'weixin'
                     "openid": openid,  # 第三方平台的唯一标识
                     "auth_token": ""}  # 第三方平台的授权码
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
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'微信登录', u"post", third_login_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    r = WeixinLogin()
    print(r.weixin_login("openid"))