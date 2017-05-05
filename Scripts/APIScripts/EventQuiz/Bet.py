# _*_ coding:utf-8 _*_
import multiprocessing as mul_p
from Scripts.APIScripts.Other.Login import *


class Bet:
    """
    下注
    """
    def bet(self, guess_id, item_id, player, gold, token):
        """
        下注
        :param guess_id: 竞猜比赛ID
        :param item_id: 竞猜项ID
        :param player: 下注方ID
        :param gold: 蟠桃数
        :param token:
        :return:
        """
        post_data = {"guessId": "%d" % guess_id,
                    "guessingItemId": "%d" % item_id,
                    "player": "%d" % player,
                     "gold": "%d" % gold}
        headers = {"Cache - Control": "no - cache",
                    "Content - Type": "text / html;charset = UTF - 8",
                    'Accept': 'application/json',
                    'Authorization': token,
                    "Date": "%s" % GetCurrentTime().getHeaderTime(),
                    "Proxy - Connection": "Keep - alive",
                    "Server": "nginx / 1.9.3(Ubuntu)",
                    "Transfer - Encoding": "chunked"}
        bet_url = "http://%s/guessing/bet" % (ConfigFile().host())
        request = requests.post(bet_url, data=post_data, headers=headers)
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
            log_list = [u'下注', u"post", bet_url, str(post_data), time, status_code, info]  # 单条日志记录
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
    item_id = 53
    player =
    instance = Bet()
    user_datas = instance.get_data()
    for token in user_datas:
        result.append(pool.apply_async(func=instance.bet,
                                       args=(31, item_id, player,random.choice(100, 50, 0 ,20,1.0), token)))
    pool.close()
    pool.join()
    for r in result:
        print(r.get())


