# _*_ coding:utf-8 _*_
from Scripts.GetReport import *

class SendCode:
    """
    发送验证码：注册、修改密码
    """
    def sendCode(self, mobile, type):
        """
        发送验证码：注册、修改密码
        :param mobile:
        :param type: 1:用户注册；2:忘记密码（默认值为1）
        :return:
        """
        post_data = {"mobile": "%s" % mobile,
                     "type": "%s" % type}  # 1:用户注册；2:忘记密码（默认值为1）
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        send_code_url = "http://%s/user/sendcode" % ConfigFile().host()
        request = requests.post(send_code_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'发送验证码', u"post", send_code_url, str(post_data), time, status_code, info]
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == "__main__":
    r = SendCode()
    print(r.sendCode("18708125576", 1))