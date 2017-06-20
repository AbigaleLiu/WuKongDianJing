# _*_ coding:utf-8 _*_

"""
运行脚本文件
"""
import timeit
import math
import multiprocessing as mul_t
from Scripts.APIScripts.Competition.ApplyMatch import *
from Scripts.APIScripts.Competition.ApplyMatch import *
from Scripts.APIScripts.Competition.Confirm import *
from Scripts.APIScripts.Competition.Pick import *
from Scripts.APIScripts.Competition.Ban import *
from Scripts.ScriptGUI import *


class RunScript:

    def __init__(self):
        self.tokens = ConfigFile().get_token()
        self.role_ids = ConfigFile().get_role_id()
        self.match_id = int(input("赛事ID："))
        # self.match_id = ScriptGUI().match_id_GUI()

    def competition(self):
        """
        自动运行比赛脚本
        :param id: 比赛ID
        :param confirm_time: 距确认参赛开始时间（单位：s）
        :param pick_time: 距签到开始时间（单位：s）
        :param screenings: 当前轮次
        :param pick_heros: 签到选择的英雄
        :param ban_heros: Ban选择的英雄
        :return: 
        """
        # 报名
        start_apply = timeit.default_timer()
        pool_apply = mul_t.Pool(processes=100)
        result_apply = []
        for user in range(len(self.tokens)):
            token = self.tokens[user]
            role_id = int(self.role_ids[user])
            result_apply.append(pool_apply.apply_async(ApplyMatch().apply_match, args=(self.match_id, token, role_id)))
        for r in result_apply:
            print(r.get())
        end_apply = timeit.default_timer()
        execute_time = math.ceil(end_apply - start_apply)  # 程序执行耗费时间
        # time.sleep((confirm_time+1)*60)
        # # 确认参赛
        # # for user in range(len(self.get_token())):
        # #     token = self.get_token()[user]
        # #     if screenings == 1:
        # #         Confirm().confirm(token, id)
        # # time.sleep(pick_time)
        # # # Pick
        # # for user in range(len(self.get_token())):
        # #     token = self.get_token()[user]
        # #     Pick().pick_heros(token, id, screenings, pick_heros)
        # # # Ban
        # # for user in range(len(self.get_token())):
        # #     token = self.get_token()[user]
        # #     Ban().ban(token, id, screenings, ban_heros)
        # # # 提交结果，随机提交胜或负
        # # for user in range(len(self.get_token())):
        # #     token = self.get_token()[user]
        # #     random_num = random.randint(1, 2)
        # #     if random_num == 1:
        # #         Win().win(token, id, screenings)
        # #     else:
        # #         Lose().lose(token, id, screenings)

if __name__ == '__main__':
    _run = RunScript()
    _run.competition()




