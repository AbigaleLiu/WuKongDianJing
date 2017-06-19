# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.Lose import *
from Scripts.ConfigFile import *


class Result:
    """
    提交选择“胜”或者“负”
    """
    def win(self, token, id=ConfigFile().activity_id(), screenings=1):
        post_data = {"screenings": "%d" % screenings}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        win_url = "http://%s/activity/%d/win" % (ConfigFile().host(), id)
        request = requests.post(win_url, post_data, headers=headers)
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
            log_list = [u'提交结果为胜', u"post", win_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

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


if __name__ == '__main__':
        id = 36  # 赛事ID4
        screenings = 1  # 轮次
        pool = mul_t.Pool(processes=100)
        result = []
        for token in ConfigFile().get_token():
            result_num = random.choice((1, 2))
            if result_num == 1:
                result.append(pool.apply_async(func=Result().win, args=(token, id, screenings)))
            elif result_num == 2:
                result.append(pool.apply_async(func=Result().lose, args=(token, id, screenings)))
        for r in result:
            print(r.get())

