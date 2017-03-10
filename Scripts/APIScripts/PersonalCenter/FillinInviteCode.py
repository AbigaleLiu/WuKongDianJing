# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.PersonalCenter.GetInviteCode import *
class FillinInviteCode:
    def fillin_invite_code(self, login, fromcode):
        post_data = {"fromcode": "%s" % fromcode}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        get_invate_code_url = "http://%s/member/fillcode" % ConfigFile().host()
        request = requests.post(get_invate_code_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取邀请码', u"post", get_invate_code_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


def main():
    login = Login().login("18708125570", "aaaaaa")
    fromcode = GetInviteCode().get_invite_code(login)["data"]["code"]
    r = FillinInviteCode()
    print(r.fillin_invite_code(login, fromcode))
if __name__ == "__main__":
    main()
