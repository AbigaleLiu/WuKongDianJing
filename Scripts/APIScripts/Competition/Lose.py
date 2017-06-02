# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class Lose:
    """
    提交选择“负”
    """
    def lose(self, token, id, screenings):
        post_data = {"screenings": "%d" % screenings}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        lose_url = "http://%s/activity/%d/transport" % (ConfigFile().host(), id)
        request = requests.post(lose_url, post_data, headers=headers)
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
            log_list = [u'提交结果为负', u"post", lose_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志


    def get_data(self):
        """
        获取xml文件中保存的token
        :return:
        """
        tokens = []
        workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\wk.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"wk")  # 根据索引获取工作表
        for row_num in range(sheet.nrows):
            row = sheet.row_values(row_num)
            token = "Bearer " + row[0]
            tokens.append(token)
        return tokens  # 返回token


if __name__ == '__main__':
        id = 454  # 赛事ID
        screenings = 1  # 轮次
        pool = mul_t.Pool(processes=1)
        result = []
        for token in Lose().get_data():
            result.append(pool.apply_async(func=Lose().lose, args=(token, id, screenings)))
        for r in result:
            print(r.get())
