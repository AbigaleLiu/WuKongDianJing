# _*_ coding:utf-8 _*_
import multiprocessing as mul_p
from Scripts.APIScripts.Other.Login import *


class GuessInfo:
    """
    竞猜详情
    """
    def guess_info(self, item_id, token):
        """
        竞猜详情信息
        :param item_id: 竞猜项ID
        :param token:
        :return:
        """
        post_data = {}
        headers = {"Cache - Control": "no - cache",
                    "Content - Type": "text / html;charset = UTF - 8",
                    'Accept': 'application/json',
                    'Authorization': token,
                    "Date": "%s" % GetCurrentTime().getHeaderTime(),
                    "Proxy - Connection": "Keep - alive",
                    "Server": "nginx / 1.9.3(Ubuntu)",
                    "Transfer - Encoding": "chunked"}
        guess_info_url = "http://%s/guessing/%s" % (ConfigFile().host(), item_id)
        request = requests.get(guess_info_url, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'下注', u"post", guess_info_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志

    def get_data(self):
        datas = {}
        workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\wk.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"wk")  # 根据索引获取工作表
        for row_num in range(sheet.nrows):
            row = sheet.row_values(row_num)
            datas[row_num+1] = "Bearer " + row[0]
        return datas


if __name__ == "__main__":
    pool = mul_p.Pool(processes=10)
    result = []
    instance = GuessInfo()
    user_datas = instance.get_data()
    for token in user_datas:
        result.append(pool.apply_async(func=instance.guess_info, args=(53, token)))
    pool.close()
    pool.join()
    for r in result:
        print(r.get())
