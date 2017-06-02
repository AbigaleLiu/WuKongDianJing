# _*_ coding:utf-8 _*_
import os
import random
import math
import time
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
        host_local = "192.168.5.184:8015"  # v 2.0 测试服
        host_official = "apiv2.gvgcn.com"  # 正式服
        # return host_local
        return host_official

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
        # users_path = r"F:\wukogndianjing\Scripts\users.xlsx"
        users_path = r"F:\wukogndianjing\Scripts\User.xlsx"
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
        随机生成出生日期的时间戳
        :return: str
        """
        year = random.randint(1970, 2016)
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 28)).zfill(2)
        birthday = "%d-%s-%s" % (year, month, day)
        timestamp = int(time.mktime(time.strptime(birthday, '%Y-%m-%d')))
        return timestamp

    def nickname(self):
        """
        随机选择昵称
        :return: str
        """
        sub01 = ['温柔', '内向', '腼腆', '害羞', '多疑', '直率', '活泼', '开朗', '滑稽', '可笑', '古怪', '怪异',
                 '狭窄', '宽容', '多情', '冷淡', '热情', '拘谨', '谨慎', '严格', '严厉', '凶残', '开朗', '随和',
                 '健谈', '狡猾', '老实', '稳重', '幼稚', '调皮', '活泼', '内向', '善良', '足智多谋', '木讷寡言',
                 '心胸狭窄', '忠厚老实', '阴险狡诈', '乐天达观', '成熟稳重', '幼稚调皮', '温柔体贴', '活泼可爱',
                 '普普通通', '内向害羞', '外向开朗', '心地善良', '聪明伶俐', '善解人意', '风趣幽默', '思想开放',
                 '积极进取', '小心谨慎', '郁郁寡欢', '正义正直', '悲观失意', '好吃懒做', '处事洒脱', '多愁善感']
        sub02 = ['的', '', '滴', '哒']
        sub03 = ['科姆', '琼', '尼基', '贝蒂', '琳达', '特尼', '丽丽', '芭芭', '丽莎', '海伦', '凯瑟',
                 '李', '凯丽', '玫', '朱莉', '曼达', '菲奥', '爱米', '里塔', '杰西', '里莎',
                 '安', '戴安', '菲奥', '朱迪', '杜丽', '鲁迪', '阿达', '雪莉', '琼', '特西', '雪莉',
                 '索菲', '维安', '莉莉', '乔埃', '罗丝', '朱莉', '格亚', '卡萝', '泰勒', '温迪', '格里',
                 '维维', '罗琳', '萨曼', '利亚', '凯特', '戴米', '萨妮', '温迪', '阿瓦', '克里', '蒂娜', '朱迪',
                 '苏珊', '里斯', '丽丝', '乔西', '萨丽', '玛莉', '贝卡']
        nickname = random.choice(sub01) + random.choice(sub02) + random.choice(sub03)
        return nickname

    def game_role_name(self, game_id):
        """
        随机选择游戏角色名
        :return: str
        """
        if game_id == 1:
            game_role_name = self.nickname() + "#" + "51422"
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
        third_reward = base_num / sum(range(1, rounds)) * list[-i]
        reward["3"] = int(third_reward)
        for i in range(1, rounds):
            per_reward = math.floor((base_num-third_reward) / sum(range(1, rounds)) * list[-i])
            reward["%d" % 2**(i-1)] = "%d" % per_reward
            reward_all = reward_all + per_reward
        if (reward_all+third_reward) != base_num:
            reward["1"] = str(int(reward["1"]) + base_num - reward_all - int(third_reward))
        return reward


if __name__ == '__main__':
    _run = ConfigFile()
    print(_run.birthday())