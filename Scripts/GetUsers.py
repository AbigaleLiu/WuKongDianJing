# _*_ coding:utf-8 _*_
""""
从users.xls文件中读取已注册用户mobile、password
"""
import xlrd  # 对excel文件读操作
from Scripts.ConfigFile import *


class GetUsers:
    def __init__(self):
        pass

    def sheet(self):
        workbook = xlrd.open_workbook(r"%s" % ConfigFile().users_path())  # 打开文件
        sheet = workbook.sheet_by_name(r"test_users")  # 根据索引获取工作表
        # print sheet.name, sheet.nrows, sheet.ncols  # 打印工作表名称、行数、列数
        return sheet

    def get_users(self):
        """
        获取单个用户信息：uid、mobile、password、nickname、game_name、peach_numbers、game_peach、signin_ways
        :return:单条用户信息列表组成的二维列表
        """
        users_list = []
        for row_num in range(1, self.sheet().nrows):
            users_list.append(self.sheet().row_values(row_num))
        return users_list

    def get_uid(self, index=0):
        """
        获取用户ID
        :return: uid
        """
        uid = str(int(self.get_users()[index][0]))
        print(uid)

    def get_mobile(self, index=0):
        """
        获取用户手机号码
        :return: mobile
        """
        mobile = str(int(self.get_users()[index][1]))
        return mobile

    def get_password(self, index=0):
        """
        获取登录密码
        :return: password
        """
        password = self.get_users()[index][2]
        return password

    def get_nickname(self, index):
        """
        获取用户昵称
        :return: nickname
        """
        nickname = self.get_users()[index][3]
        return nickname

    def get_game_name(self, index=0):
        """
        获取游戏角色名称
        :return: game_name
        """
        game_name = self.get_users()[index][4]
        return game_name

    def get_peach_numbers(self, index=0):
        """
        获取蟠桃数
        :return: peach_numbers
        """
        peach_numbers = str(int(self.get_users()[index][5]))
        return peach_numbers

    def get_game_peach(self, index=0):
        """
        获取赛事蟠桃
        :return: game_peach
        """
        game_peach = str(int(self.get_users()[index][6]))
        return game_peach

    def get_signin_ways(self, index):
        """
        获取注册方式：手机号注册、QQ和微信快捷登录
        :return: signin_ways
        """
        signin_ways = self.get_users()[index][7]
        return signin_ways


def main():
    r = GetUsers()
    r.get_uid()
if __name__ == "__main__":
    main()