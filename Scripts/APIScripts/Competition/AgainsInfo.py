# _*_ coding:utf-8 _*_
"""
获取对阵表
"""

from Scripts.APIScripts.Other.Login import *


class AgainsInfo:
    def again_info(self, token):
        """
        获取当前轮次对阵表
        :param token:
        :return:
        """
        post_data = {"id": "%s" % ConfigFile().activity_id()}
        headers = {"accesstoken": token,
                   "Content - Length": "8",
                   "Content - Type": "application / x - www - form - urlencoded",
                   "Host": "192.168.1.184:8012",
                   "Connection": "Keep - Alive",
                   "User - Agent": "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) "
                                   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                   "Cookie": "PHPSESSID=9ei2qc3j90opmpdao82cl14v90",
                   "Cookie2": "$Version = 1",
                   "Accept - Encoding": "gzip"}
        again_info_url = "%s/api/Event/againstInfo?id=%s" % (ConfigFile().host(), ConfigFile().activity_id())
        post_data = urllib.urlencode(post_data)
        try:
            request = urllib2.Request(again_info_url, post_data, headers)
            response = urllib2.urlopen(request, timeout=10)
            result = response.read().decode("utf-8")
            print result
            list_again_info = json.loads(result)
            print list_again_info
        except urllib2.HTTPError as e:
            return e.code, urllib.unquote(e.reason)

    def get_screening(self, list_again_info):
        """
        获取比赛总轮次数
        :param list_again_info:
        :return: screening
        """
        screening = list_again_info[0]["screening"]
        return screening

    def get_current_screeening(self, list_again_info):
        """
        获取当前轮次数，0为比赛未开始
        :param list_again_info:
        :return: current_screening
        """
        current_screening = list_again_info[0]["current_screening"]
        print current_screening

def main():
    r = AgainsInfo()
    r.again_info(Login().login("18708125571", "aaaaaa")["token"])
    # r.get_current_screeening(r.again_info(Login().login("18708125571", "aaaaaa")["token"]))
if __name__ == "__main__":
    main()
