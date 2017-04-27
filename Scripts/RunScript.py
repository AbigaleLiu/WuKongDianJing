# _*_ coding:utf-8 _*_

"""
运行脚本文件
"""
from datetime import *
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.CreateMatch import *
from Scripts.APIScripts.Competition.ApplyMatch import *
from Scripts.APIScripts.PersonalCenter.RoleList import *
from Scripts.APIScripts.PersonalCenter.AddRole import *
from Scripts.APIScripts.Competition.Confirm import *
from Scripts.APIScripts.Competition.Pick import *


class RunScript:
    # def run_script(self, judge_login, post_data, id, game_id):
    #     # CreateMatch().create_match(judge_login, post_data)  # 创建比赛
    #     # print("创建比赛")
    #     users = GetUsers().get_users()
    #     # for user in range(len(users)):
    #     #     login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
    #     #     print("用户登录")
    #     #     if RoleList().role_list(login)["data"]:
    #     #         role_id = RoleList().role_list(login)["data"][-1]["id"]
    #     #         print("获取角色ID")
    #     #     else:
    #     #         print(AddRole().add_role(login, game_id))
    #     #         role_id = RoleList().role_list(login)["data"][-1]["id"]
    #     #     print(ApplyMatch().apply_match(login, id, role_id))
    #     login_try = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
    #     if Confirm().confirm(login_try, id)["info"] != "确认参赛成功":
    #         print("不能正常完成确认参赛")
    #         self.run_task(Confirm().confirm, minutes=1, login_try, id)
    #         print("定时执行")
    #     else:
    #         for user in range(len(users)):
    #             login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
    #             print("用户登录")
    #             print(Confirm().confirm(login, id))
    #
    # def run_task(self, func, minutes, *args):
    #     now_time = datetime.datetime.now()
    #     print(now_time)
    #     period = datetime.timedelta(minutes=minutes)
    #     next_time = period + now_time
    #     print("下一次执行", next_time.strftime('%Y-%m-%d %H:%M:%S'))
    #     while True:
    #         iter_now = datetime.datetime.now()
    #         iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
    #         if str(iter_now_time) == str(next_time.strftime('%Y-%m-%d %H:%M:%S')):
    #             print(iter_now_time)
    #             func(args)
    #             iter_time = iter_now + period
    #             next_time = iter_time
    #             continue
    def run(self, id):
        users = GetUsers().get_users()
        for user in range(len(users)):
            login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
            print(login)
            _run = Pick()
            print(_run.pick(login, id))


if __name__ == "__main__":
    judge_login = Login().login("13330944792", "123456")
    # print(judge_login)
    post_data = {"gameId": 1,
                 "activityType": 1,
                 "title": "自动运行脚本",
                 "activity_rule_id": 3,
                 "activity_people": 1,
                 "model": "common",
                 "timerule": ['2017-03-28 9:45', '2017-03-28 15:21', '2017-03-28 15:31', '2017-03-28 15:41'],
                 "password": None,
                 "remark": "1111",
                 "frozen": "100",
                 "common_rewardrule": {'1': 60, '2': 30, '3': 10}}
    _run = RunScript()
    print(_run.run_script(judge_login, post_data, 146, 1))