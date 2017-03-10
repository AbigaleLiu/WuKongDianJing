# _*_ coding:utf-8 _*_

"""
运行脚本文件
"""
from Scripts.APIScripts.Competition.ApplyCompetition import *
from Scripts.APIScripts.Competition.GameMemberID import *
from Scripts.APIScripts.Other.LoginReportData import *


class RunScript:
    def run_script(self):
        report = LoginReportData()
        GetReport().get_report("login")
        users = GetUsers()  # 获取用户列表
        for user_index in range(len(users.get_users())):
            try:
                time = GetCurrentTime().getCurrentTime()  # 获取当前时间
                mobile = GetUsers().get_mobile(user_index)  # 获取登录账号
                password = GetUsers().get_password(user_index)   # 获取登录密码
                login = Login().login(mobile, password)  # 登录
                id = GetReport().get_blank_row_id("login")  # 获取当前日志文件中共有多少条登录记录
                LoginReportData().get_login_report(login, id)  # 将登录记录写入日志文件
                if login['token']:
                    token = login['token']  # Login类返回token
                activity_id = ConfigFile().activity_id()
                member_game_id = GetGameMember().get_game_member_id(token)
                apply_competition = ApplyCompetition().apply(activity_id, member_game_id, mobile, token)
                if apply_competition[1] == 200:
                    print(time, mobile, "报名成功")
                else:
                    print(apply_competition[0], mobile, apply_competition[1], apply_competition[2])
            except urllib2.HTTPError as e:
                print(time, mobile, e.code, urllib.unquote(e.reason))


def main():
    r = RunScript()
    r.run_script()
if __name__ == "__main__":
    main()