# _*_ coding:utf-8 _*_

"""
运行脚本文件
"""
from Scripts.APIScripts.Competition.ApplyMatch import *
from Scripts.APIScripts.Competition.Confirm import *
from Scripts.APIScripts.Competition.Pick import *
from Scripts.APIScripts.Competition.Ban import *
from Scripts.APIScripts.Competition.Win import *
from Scripts.APIScripts.Competition.Lose import *

class RunScript:
    def get_token(self):
        tokens = []
        workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\wk.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"wk")  # 根据索引获取工作表
        for i in sheet.col_values(0):
            tokens.append("Bearer " + i)
        return tokens

    def get_role_id(self):
        role_ids = []
        workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\wk.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"wk")  # 根据索引获取工作表
        for i in sheet.col_values(1):
            role_ids.append(int(i))
        return role_ids

    def competition(self, id, confirm_time, pick_time, screenings=1, pick_heros="11,12,13,14,15", ban_heros = "11,12"):
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
        for user in range(len(self.get_token())):
            token = self.get_token()[user]
            role_id = self.get_role_id()[user]
            if screenings == 1:
                ApplyMatch().apply_match(id, token, role_id)
        time.sleep(confirm_time)
        # 确认参赛
        for user in range(len(self.get_token())):
            token = self.get_token()[user]
            if screenings == 1:
                Confirm().confirm(token, id)
        time.sleep(pick_time)
        # Pick
        for user in range(len(self.get_token())):
            token = self.get_token()[user]
            Pick().pick_heros(token, id, screenings, pick_heros)
        # Ban
        for user in range(len(self.get_token())):
            token = self.get_token()[user]
            Ban().ban(token, id, screenings, ban_heros)
        # 提交结果，随机提交胜或负
        for user in range(len(self.get_token())):
            token = self.get_token()[user]
            random_num = random.randint(1, 2)
            if random_num == 1:
                Win().win(token, id, screenings)
            else:
                Lose().lose(token, id, screenings)

if __name__ == '__main__':
    _run = RunScript()
    _run.competition(447, 120, 300, 1)





