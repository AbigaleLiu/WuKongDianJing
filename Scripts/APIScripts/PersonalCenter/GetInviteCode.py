# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *


class GetInviteCode:
    """
    获取邀请码
    """
    def get_invite_code(self, login):
        """
        获取邀请码
        :param login:
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        get_invite_code_url = "http://%s/member/fromcode" % ConfigFile().host()
        request = requests.get(get_invite_code_url, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取邀请码', u"get", get_invite_code_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == "__main__":
    login = Login().login("18708125570", "aaaaaa")
    r = GetInviteCode()
    print(r.get_invite_code(login))
