# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.BanList import *


class Ban:
    """
    提交禁选的英雄/地图
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        self.screening = config_file.get_current_screening()

    def ban(self, token):
        post_data = {"screenings": "%d" % self.screening,
                     "heros": "%s" % self.ban_heros(token)}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        ban_url = "http://%s/activity/%d/ban" % (ConfigFile().host(), self.match_id)
        request = requests.put(ban_url, post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        # print(ban_url)
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交禁选的英雄或地图', u"put", ban_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def ban_heros(self, token):
        pick_json = BanList().ban_list(token)
        if pick_json["data"]:
            if type(pick_json["data"]) is dict:
                pick_list = []
                sign_num = pick_data["sign_num"]
                for i in range(len(pick_data["list"])):
                    pick_list.append(pick_data["list"][i]["id"])
                heros_list = [random.choice(pick_list) for i in range(int(sign_num))]
                heros = ""
                for hero in heros_list:
                    heros = heros + str(hero) + ","
                return heros


if __name__ == '__main__':
    token = Login().login("14700000003", "aaaaaa")["data"]["auth_token"]
    Ban().ban_heros(token)
    # pool = mul_t.Pool(processes=100)
    # result = []
    # for token in ConfigFile().get_token():
    #     # heros = Ban().ban_heros(token, id, screenings)
    #     result.append(pool.apply_async(func=Ban().ban, args=(token, id, screenings, "1,10")))
    # for r in result:
    #     print(r.get())
