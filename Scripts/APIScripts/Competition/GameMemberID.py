#_*_ coding:utf-8 _*_
"""
获取登录用户绑定的游戏角色ID
"""
from Scripts.APIScripts.PersonalCenter.Login import *
from Scripts.ConfigFile import *

class GetGameMember:
    def get_game_member_id(self, token):
        post_data = {}
        headers = {"accesstoken": "%s" % token,
                   "Content - Length": "66",
                   "Content - Type": "application / x - www - form - urlencoded",
                   "Host": "192.168.1.184:8012",
                   "Connection": "Keep - Alive",
                   "User - Agent": "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; MHA-AL00 Build/HUAWEIMHA-AL00) "
                                   "AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                   "Cookie": "PHPSESSID=9ei2qc3j90opmpdao82cl14v90",
                   "Cookie2": "$Version = 1",
                   "Accept - Encoding": "gzip"
                   }
        try:
            post_data = urllib.urlencode(post_data)
            game_member_url = "%s/api/users/mygames?" % ConfigFile().host()
            request = urllib2.Request(game_member_url, post_data, headers)  # 构造request
            response = urllib2.urlopen(request, timeout=10)  # 将返回的request转为可以像本地文件一样操作的对象，10s超时
            result = response.read().decode('utf-8')
            list_result = json.loads(result)  # 获取绑定的游戏角色列表
            # print result
            for i in range(len(list_result)):
                if list_result[i]["game_id"] == "110":  # 游戏ID：110为炉石传说
                    return list_result[i]["id"]
                else:
                    return "该用户没有绑定炉石角色"
        except urllib2.HTTPError as e:
            return e.code, urllib.unquote(e.reason)


def main():

    r = GetGameMember()
    r.get_game_member_id(Login().login("18708125571", "aaaaaa")["token"])
if __name__ == "__main__":
    main()
