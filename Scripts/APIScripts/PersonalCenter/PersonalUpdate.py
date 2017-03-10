# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *


class PersonalUpdate:
    """
    编辑个人资料
    """
    def personal_update(self, login):
        """
        编辑个人资料
        :param login:
        :return:
        """
        post_data = {"nickname": "%s" % ConfigFile().nickname(),
                     "head": "%s" % ConfigFile().pictures(),
                     "sex": "%d" % random.choice((1, 2)),   # 1是男，2是女，随机选择
                     "birthday": "%s" % ConfigFile().birthday()}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        personal_info_url = "http://%s/member/updateinfo" % ConfigFile().host()
        request = requests.put(personal_info_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'编辑个人资料', u"put", personal_info_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == "__main__":
    login = Login().login("18708125570", "aaaaaa")
    r = PersonalUpdate()
    print(r.personal_update(login))
