# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
class ComplainContext:
    """
    提交用户反馈
    """
    def complain_context(self, login):
        """
        提交反馈
        :param login:
        :return:
        """
        post_data = {"context": "",
                     "type": "%d" % random.randint(1, 2)}  # 1：功能建议；2：产品BUG
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        complain_type_url = "http://%s/complaint/opinion" % ConfigFile().host()
        request = requests.post(complain_type_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'提交用户反馈', u"post", complain_type_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


def main():
    login = Login().login("18708125500", "aaaaaa")
    r = ComplainContext()
    print r.complain_context(login)
if __name__ == "__main__":
    main()
