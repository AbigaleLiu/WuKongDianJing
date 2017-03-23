# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
class UserData:
    """
    获取用户个人中心数据（蟠桃等）
    """
    def user_data(self, login):
        """
        获取用户个人中心数据（蟠桃等）
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
        user_data_url = "http://%s/user/info" % ConfigFile().host()
        request = requests.get(user_data_url, headers=headers)
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
            log_list = [u'获取用户数据', u"get", user_data_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == "__main__":
    login = Login().login("18708125570", "aaaaaa")
    r = UserData()
    print(r.user_data(login))
