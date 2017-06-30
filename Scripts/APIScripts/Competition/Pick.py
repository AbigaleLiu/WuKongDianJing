# _*_ coding:utf-8 _*_
import requests
import random
import multiprocessing as mul_t
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.PickList import *
from Scripts.GetUsers import GetUsers
from Scripts.APIScripts.Other.Login import Login


class Pick:
    """
    提交选择的英雄/地图
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        self.screening = config_file.get_current_screening()

    def pick(self, token):
        post_data = {"screenings": "%d" % self.screening,
                     "heros": "%s" % self.pick_heros(token)}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        pick_url = "http://%s/activity/%d/bpsign" % (ConfigFile().host(), self.match_id)
        request = requests.post(pick_url, post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                return info
        finally:
            log_list = [u'提交选择的英雄或地图', u"post", pick_url, str(post_data), time, status_code, info]  # 单条日志记录
            print(log_list)
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def pick_heros(self, token):
        """
        获取要提交的Pick英雄列表
        :param token:
        :return:
        """
        pick_json = PickList().pick_list(token)
        # pick_data = pick_json["data"]
        if isinstance(pick_json, dict):
            pick_list = []
            pick_data = pick_json["data"]
            if pick_data:
                sign_num = int(pick_data["sign_num"])
                for i in range(len(pick_data["list"])):
                    pick_list.append(pick_data["list"][i]["id"])
                heros = random.sample(pick_list, sign_num)
                heros_str = ""
                for hero in heros:
                    heros_str = heros_str + str(hero) + ","
                heros_str = heros_str[:-1]
                return heros_str
            else:
                return pick_json
        else:
            return pick_json


if __name__ == '__main__':
    token = Login().login("14700000022", "aaaaaa")["data"]["auth_token"]
    _run = Pick()
    print(_run.pick(token))
    for token in ConfigFile().get_token():
        print(_run.pick(token))
    # result = []
    # pool = mul_t.Pool(processes=100)
    # for token in ConfigFile().get_token():
    #     result.append(pool.apply_async(func=_run.pick, args=(token,)))
    # for r in result:
    #     print(r.get())

