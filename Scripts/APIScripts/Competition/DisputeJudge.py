# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_t
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *


class DisputeJudge:
    """
    争议处理
    """
    def dispute_judge(self, token, id, dispute_id ,winner_id):
        """

        :param login:
        :param id:
        :param dispute_id:
        :param winner_id:获胜者id
        :return:
        """
        post_data = {"won": "%d" % winner_id}
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': token,
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        dispute_judge_url = "http://%s/activity/%d/dispute/%d/judgment" % (ConfigFile().host(), id, dispute_id)
        request = requests.post(dispute_judge_url, post_data, headers=headers)
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
            log_list = [u'争议处理', u"post", dispute_judge_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志


if __name__ == '__main__':
        id = 241  # 赛事ID
        screenings = 1  # 轮次
        pool = mul_t.Pool(processes=10)
        result = []
        for token in Lose().get_data():
            result.append(pool.apply_async(func=Lose().lose, args=(token, id, screenings)))
        for r in result:
            print(r.get())
