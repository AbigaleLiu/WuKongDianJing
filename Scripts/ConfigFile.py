# _*_ coding:utf-8 _*_
import os
import random
import math
import json
"""
配置文件
"""


class ConfigFile:
    def host(self):
        """
        请求接口主机
        :return:
        """
        host_local = "192.168.1.184:8015"  # v 2.0 测试服
        host_official = "http://api.gvgcn.com"  # 正式服
        return host_local

    def activity_id(self):
        """
        比赛ID
        :return: activity_id
        """
        activity_id = "10823"
        return activity_id

    def report_path(self):
        """
        测试日志文件路径
        :return: report_path
        """
        report_path = r"F:\wukogndianjing\Scripts\Reports\report.xls"
        return report_path

    def users_path(self):
        """
        已注册用户文件路径
        :return: users_path
        """
        users_path = r"F:\wukogndianjing\Scripts\users.xlsx"
        return users_path

    def case_path(self):
        """
        测试用例存放目录
        :return: case_path
        """
        case_path = r"F:\wukogndianjing\Scripts\Cases"
        return case_path

    def pictures(self):
        pictures = []
        for picture in os.listdir(r"F:\wukogndianjing\Scripts\Cases\cats"):
            pictures.append(r"F:\wukogndianjing\Scripts\Cases\cats"+picture)
        # print len(pictures)
        picture = pictures[random.randint(1, 82)]
        return picture

    def birthday(self):
        """
        随机生成出生日期
        :return: str
        """
        year = random.randint(1950, 2017)
        month = random.randint(1, 12)
        day = random.randint(1, 30)
        birthday = "%d-%d-%d" % (year, month, day)
        return birthday

    def nickname(self):
        """
        随机选择昵称
        :return: str
        """
        nickname = random.choice((u"海纳百川",
                                  u"迷雾沼泽",
                                  u"有理想的大师",
                                  u"夜色",
                                  u"蓝蓝蓝蓝",
                                  u"鱼儿水中游",
                                  u"梧桐木",
                                  u"清风道长",
                                  u"策马江湖",
                                  u"会开花的树"))
        return nickname

    def game_role_name(self, game_id):
        """
        随机选择游戏角色名
        :return: str
        """
        if game_id == 1:
            game_role_name = random.choice((u"海纳百川#12121",
                                            u"迷雾沼泽#14144",
                                            u"有理想的大师#122334",
                                            u"夜色#4414",
                                            u"蓝蓝蓝蓝#4532",
                                            u"鱼儿水中游#5223",
                                            u"梧桐木#1224",
                                            u"清风道长#5345",
                                            u"策马江湖#5678",
                                            u"会开花的树#9089"))
        else:
            game_role_name = random.choice((u"海纳百川",
                                            u"迷雾沼泽",
                                            u"有理想的大师",
                                            u"夜色",
                                            u"蓝蓝蓝蓝",
                                            u"鱼儿水中游",
                                            u"梧桐木",
                                            u"清风道长",
                                            u"策马江湖",
                                            u"会开花的树"))
        # game_role_name = u"清风道长"
        return game_role_name

    def raward(self, people_num, base_num=100):
        """
        创建比赛-奖金方案
        :param people_num: 报名人数
        :param base_num: 总奖金基数，若为常规赛则传frozen值；若为奖金池则使用默认值
        :return: 
        """
        reward = {}
        list = []
        reward_all = 0
        rounds = int(math.log2(int(people_num))) + 1
        for i in range(1, rounds):
            list.append(i)
        for i in range(1, rounds):
            per_reward = math.floor(base_num / sum(range(1, rounds)) * list[-i])
            reward["%d" % i] = "%d" % per_reward
            reward_all = reward_all + per_reward
        if reward_all != base_num:
            reward["1"] = str(int(reward["1"]) + base_num - reward_all)
        return reward


if __name__ == '__main__':
    _run = ConfigFile()
    print(_run.raward(8))