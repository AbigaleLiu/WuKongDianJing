# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_p
from Scripts.GetReport import *
from Scripts.GetCurrentTime import *
import random


class Banner:
    """
    获取banner列表
    """
    def banner(self):
        """
        获取banner列表
        :return: 接口返回的json数据
        """
        post_data = {"delivery": "%s" % random.randint(1, 7)}  # 1-首页弹窗 2-资讯 3-蟠桃园 4-赛事 5-附近 6- new-投票 7-启动页
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        banner_url = "http://%s/banner/list" % ConfigFile().host()
        request = requests.get(banner_url, post_data, headers=headers)
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
            # print(info)
            log_list = [u'获取banner', u"get", banner_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志

    # def run(self):
    #     pool = mul_p.Pool(processes=10)
    #     for i in range(10):
    #         pool.map_async(self,() ,)
    #     pool.close()
    #     pool.join()
if __name__ == "__main__":
    # _run = Banner()
    # _run.run()
    b = Banner()
    print(b.banner())
