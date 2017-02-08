# _*_ coding:utf-8 _*_
"""
已报名用户确认参赛
"""

from Scripts.APIScripts.PersonalCenter.Login import *


class Confirm:
    def confirm(self, token):
        """
        单个用户报名比赛后确认参赛
        :param token:
        :return:
        """
        post_data = {"id": ConfigFile().activity_id()}
        headers = {"accesstoken": token,
                   "Content-Length": "8",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Host": "192.168.1.184:8012",
                   "Connection": "Keep-Alive",
                   "User-Agent": "Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Lenovo K32c36 Build/LMY47V) "
                                 "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                   "Cookie": "PHPSESSID=gi66dlffdi1lsvr9kk4t2dc6g1",
                   "Cookie2": "$Version=1",
                   "Accept-Encoding": "gzip"
                   }
        post_data = urllib.urlencode(post_data)
        confirm_url = "%s/Api/Activity/confirm" % ConfigFile().host()
        request = urllib2.Request(confirm_url, post_data, headers)
        response = urllib2.urlopen(request)
        result = response.read().decode("utf-8")
        list_result = json.loads(result)
        if list_result["status"] == 200:
            print list_result["status"], list_result["msg"]
        else:
            print list_result["status"], list_result["msg"]

def main():
    r = Confirm()
    r.confirm(Login().login("18708125571", "aaaaaa")["token"])
if __name__ == "__main__":
    main()