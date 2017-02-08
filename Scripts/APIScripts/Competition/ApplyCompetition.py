# _*_ coding:utf-8 _*_
"""
报名比赛接口
"""

from GameMemberID import *


class ApplyCompetition:
    def apply(self, activity_id, member_game_id, mobile, token):
        """
        模拟报名，返回报名结果
        :return:报名成功返回：time、status、msg
                 报名失败返回：time、mobile、状态码、错误原因
        """
        time = GetCurrentTime().getCurrentTime()
        # mobile = GetUsers().get_mobile()
        # token = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
        post_data = {"activity_id": activity_id,
                     "member_game_id": member_game_id,
                     "mobile": mobile,
                     "password": ""}
        headers = {"accesstoken": token,
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
        post_data = urllib.urlencode(post_data)
        apply_url = "%s/Api/EventGroup/sign" % ConfigFile().host()
        try:
            request = urllib2.Request(apply_url, post_data, headers)  # 构造request
            response = urllib2.urlopen(request, timeout=30)  # 将返回的request转为可以像本地文件一样操作的对象，10s超时
            result = response.read().decode('utf-8')
            dict_response = json.loads(result)
            print dict_response
            status = dict_response["status"]
            msg = dict_response["msg"]
            # print {"time": time,
            #        "description": u"报名比赛",
            #        "mobile": mobile,
            #        "status_code": e.code,
            #        "msg": urllib.unquote(e.reason)}
        except urllib2.HTTPError as e:
            print {"time": time,
                    "description": u"报名比赛",
                    "mobile": mobile,
                    "status_code": e.code,
                    "msg": urllib.unquote(e.reason)}


def main():
    mobile = GetUsers().get_mobile()
    token = Login().login(GetUsers().get_mobile(3), GetUsers().get_password(3))["token"]
    activity_id = ConfigFile().activity_id()
    member_game_id = GetGameMember().get_game_member_id(token)
    r = ApplyCompetition()
    r.apply(activity_id, member_game_id, mobile, token)
if __name__ == "__main__":
    main()
