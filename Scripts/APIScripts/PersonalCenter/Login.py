# _*_ coding:utf-8 _*_

"""
用户登录，获取登录后token
"""
import json
import urllib
import urllib2
from Scripts.GetCurrentTime import *
from Scripts.GetUsers import *
from Scripts.ConfigFile import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Login:
    def login(self, mobile, password):
        """
        模拟用户登录
        :param mobile:
        :param password:
        :return:登录成功返回字典：{"token": token,
                                    "time": time,
                                    "description": u"登录",
                                    "mobile": mobile,
                                    "status_code": 200,
                                    "msg": u"登录成功"}
                 登录失败返回字典：{"time": time,
                                    "description": u"登录",
                                    "mobile": mobile,
                                    "status_code": e.code,
                                    "msg": urllib.unquote(e.reason)}
        """
        post_data = {
            'mobile': '%s' % mobile,
            'password': '%s' % password,
            'device_token': '190e35f7e046ce87363',
            'lng': '104.056807',
            'lat': '30.537012'
        }
        headers = {
            'Content - Length': '96',
            'Content - Type': 'application / x - www - form - urlencoded',
            'Host': 'test.gvgcn.com',
            'Connection': 'Keep - Alive',
            'User - Agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Lenovo K32c36 Build/LMY47V) '
                            'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Cookie': 'PHPSESSID = sgui3sdft8jibd86l057fm9791',
            'Cookie2': '$Version = 1',
            'Accept - Encoding': 'gzip'
        }
        post_data = urllib.urlencode(post_data)
        login_url = "%s/api/member/login" % ConfigFile().host()
        time = GetCurrentTime().getCurrentTime()
        try:
            request = urllib2.Request(login_url, post_data, headers)  # 构造request
            response = urllib2.urlopen(request, timeout=30)  # 将返回的request转为可以像本地文件一样操作的对象，10s超时
            result = response.read().decode('utf-8')
            dict_response = json.loads(result)
            token = self.getAccessToken(dict_response)
            return {"token": token,
                     "time": time,
                     "description": u"登录",
                     "mobile": mobile,
                     "status_code": 200,
                     "msg": u"登录成功"}
        except urllib2.HTTPError as e:
            return {"time": time,
                     "description": u"登录",
                     "mobile": mobile,
                     "status_code": e.code,
                     "msg": urllib.unquote(e.reason).decode("utf-8")}

    @staticmethod
    def getAccessToken(dict_response):
        """
        获取每次登录的token
        :param dict_response:
        :return:accesstoken
        """
        dict_data = dict(dict_response['data'])
        accesstoken = dict_data['accesstoken']
        return accesstoken


# def main():
#     t = Login()
#     t.login(GetUsers().get_mobile(), GetUsers().get_password())
# if __name__ == "__main__":
#     main()

