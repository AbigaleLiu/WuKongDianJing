# _*_ coding:utf-8 _*_
import requests
import random
import multiprocessing as mul_t
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.PickList import *
from Scripts.GetCurrentTime import GetCurrentTime
from Scripts.GetUsers import GetUsers
from Scripts.APIScripts.Other.Login import Login


class Pick:
    """
    提交选择的英雄/地图
    """
    def pick(self, token, id, screenings, heros):
        post_data = {"screenings": "%d" % screenings,
                     "heros": "%s" % heros}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        pick_url = "http://%s/activity/%d/bpsign" % (ConfigFile().host(), id)
        request = requests.post(pick_url, post_data, headers=headers)
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
            log_list = [u'提交选择的英雄或地图', u"post", pick_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def pick_heros(self, token, id, screenings):
        """
        获取可选英雄列表
        :param token:
        :param id:
        :param screenings:
        :return:
        """
        pick_data = PickList().pick_list(token, id, screenings)["data"]
        if type(pick_data) is dict:
            pick_list = []
            sign_num = pick_data["sign_num"]
            for i in range(len(pick_data["list"])):
                pick_list.append(pick_data["list"][i]["id"])
            heros_list = [random.choice(pick_list) for i in range(int(sign_num))]
            heros = ""
            for hero in heros_list:
                heros = heros + str(hero) + ","
            return heros

    def get_data(self):
        """
        获取xml文件中保存的token
        :return:
        """
        tokens = []
        workbook = xlrd.open_workbook(r"F:\wukogndianjing\Scripts\token&others(local).xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"tokens")  # 根据索引获取工作表
        for row_num in range(sheet.nrows):
            row = sheet.row_values(row_num)
            token = "Bearer " + row[0]
            tokens.append(token)
        return tokens  # 返回token


if __name__ == '__main__':
    result = []
    id = 48  # 赛事ID
    screenings = 1  # 轮次
    pool = mul_t.Pool(processes=100)
    for token in Pick().get_data():
        result.append(pool.apply_async(func=Pick().pick, args=(token, id, screenings, "1,10,2,8,9")))
    for r in result:
        print(r.get())
