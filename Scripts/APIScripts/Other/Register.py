# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_p
from Scripts.GetReport import *
from Scripts.GetTime import *


class Register:
    """
    注册
    """
    def register(self, mobile, password):
        """
        注册
        :param mobile:
        :param password:
        :param code:验证码，虚构手机号收不到验证码短信，暂时屏蔽
        :return:
        """
        post_data = {"mobile": "%s" % mobile,
                     "password": "%s" % password}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        register_url = "http://%s/user/register" % ConfigFile().host()
        request = requests.post(register_url, data=post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'注册', u"post", register_url , str(post_data), time, status_code, info]
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def register_user(self):
        mobiles = []
        workbook = xlrd.open_workbook(r"F:\wukogndianjing\Scripts\register_users.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"mobiles")  # 根据索引获取工作表
        for i in range(sheet.nrows):
            mobile = str(int(sheet.col_values(0)[i]))
            mobiles.append(mobile)
        return mobiles

if __name__ == "__main__":
    r = Register()
    # print(r.register("14700001231","aaaaaa"))
    pool = mul_p.Pool(processes=100)
    result = []
    instance = Register()
    user_datas = instance.register_user()
    for mobile in user_datas:
        result.append(pool.apply_async(func=instance.register, args=(mobile, "aaaaaa")))
    pool.close()
    pool.join()
    for r in result:
        print(r.get())
