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
from Scripts.APIScripts.Competition.MatchStatus import *


class RunScript:

    def __init__(self):
        config_file = ConfigFile()
        self.tokens = config_file.get_token()
        self.judgement_token = Login().login(config_file.judgement()[0], config_file.judgement()[1])["data"]["auth_token"]
        self.role_ids = config_file.get_role_id()
        self.match_id = config_file.activity_id()
        self.process_num = config_file.process_num()

    def run_script(self):

        # match_status = MatchStatus(self.judgement_token).get_match_status()  # 获取比赛当前状态
        # if match_status == 2:
        pass

    def run_apply(self):
        start_apply = timeit.default_timer()
        pool_apply = mul_t.Pool(processes=self.process_num)
        result_apply = []
        for user in range(len(self.tokens)):
            token = self.tokens[user]
            role_id = int(self.role_ids[user])
            result_apply.append(pool_apply.apply_async(ApplyMatch().apply_match, args=(token, role_id)))
        for r in result_apply:
            print(r.get())
        end_apply = timeit.default_timer()
        execute_time = math.ceil(end_apply - start_apply)  # 程序执行耗费时间
        print("报名结束，程序运行时间（s）：" + str(execute_time))

if __name__ == '__main__':
    _run = RunScript()
    _run.run_apply()




