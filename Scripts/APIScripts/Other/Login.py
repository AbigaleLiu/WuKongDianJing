# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.ConfigFile import *
from Scripts.GetReport import *


class Login:
    """
    用户登录，获取登录后token
    """
    def login(self, mobile, password):
        """
        模拟用户登录
        :param mobile:
        :param password:
        :return:接口返回的json数据
        """
        post_data = {'mobile': '%s' % mobile,
                     'password': '%s' % password}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        login_url = "http://%s/user/login" % ConfigFile().host()
        request = requests.post(login_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'登录', u"post", login_url, str(post_data), time, status_code, info]
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        print(GetCurrentTime().getHeaderTime())
        return json

    def run(self):
        pass
if __name__ == "__main__":
    t = Login()
    print(t.login("18708125500", "aaaaaa"))