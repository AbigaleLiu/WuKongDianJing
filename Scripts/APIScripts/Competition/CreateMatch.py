# _*_ coding:utf-8 _*_
import requests
from Scripts.GetTime import *
from Scripts.ConfigFile import *
from Scripts.GetReport import *
from Scripts.APIScripts.Other.Login import *
from Scripts.APIScripts.Competition.MatchType import *
from Scripts.APIScripts.Competition.MatchRule import *
from Scripts.APIScripts.Competition.MatchPeople import *


class CreateMatch:
    """
    创建比赛
    """
    def __init__(self, judgement_token):
        self.config_file = ConfigFile()
        self.judgement_token = judgement_token
        self.game_id = self.config_file.game_id()
    def create_match(self, post_data):
        headers = {"Cache - Control": "no-cache",
                   "Content - Type": "application/json;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': self.judgement_token,
                   "Date": "%s" % GetTime().getHeaderTime(),
                   "Proxy-Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        create_match_url = "http://%s/activity" % self.config_file.host()
        request = requests.post(create_match_url, json=post_data, headers=headers)
        time = GetTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json_ = request.json()
                info = json_["info"]
                return json_
            else:
                info = request.reason
        finally:
            log_list = [u'发布比赛', u"post", create_match_url, str(post_data), time, status_code, info]  # 单条日志记录
            # GetReport().get_report()  # 生成或打开日志文件
            # GetReport().record_into_report(log_list)  # 逐条写入日志

    def post_data(self, model, password=None):
        type = random.choice(MatchType().match_type(self.judgement_token, self.game_id)["data"])["id"]
        rule = random.choice(MatchRule().match_rule(self.judgement_token, self.game_id)["data"])["id"]
        people_data = random.choice(MatchPeople().match_people(self.judgement_token, self.game_id)["data"])
        people_id = people_data["id"]
        people_num = people_data["count"]
        # print(type(people_num))
        time_rule = GetTime().rule_time(int(people_num))
        if self.game_id == 1:
            game = "炉石"
        elif self.game_id == 2:
            game = "英雄"
        else:
            game = "守望"
        if model == "common":
            model_name = "常规"
            frozen = self.config_file.frozen()
            reward = self.config_file.raward(people_num, frozen)
            post_data02 = {"frozen": frozen,  # int，总蟠桃数
                           "common_rewardrule": reward}  # Array,奖金规则,数组的键一定不能变(1,2,3,4,8,16)
        else:
            model_name = "奖池"
            entry_fee = self.config_file.entry_fee()
            reward = self.config_file.raward(people_num)
            post_data02 = {"apply_money": entry_fee,  # Int,报名费用.
                           "money_rewardrule": reward}  # Array,奖金规则.eg：{"1":50}
        match_time = GetTime().match_time()
        title = game + model_name + match_time
        print(title)
        remark = random.choice(("""战城南，死郭北，野死不葬乌可食。\n
　　                              为我谓乌：“且为客豪，野死谅不葬，
　　                              腐肉安能去子逃？”\n
　　                              水深激激，蒲苇冥冥。\n
　　                              枭骑战斗死，驽马独徘徊。\n
　　                              梁筑室，何以南，何以北，\n
　　                              禾黍不获君何食？\n
　　                              愿为忠臣安可得？\n
　　                              思子良臣，良臣诚可思：\n
　　                              臣朝行出攻，暮不夜归。""",
                               """有所思，乃在大海南。\n
　　                              何用问遗君，双珠玳瑁簪，用玉绍缭之。\n
　　                              闻君有他心，拉杂摧烧之。\n
　　                              摧烧之，当风扬其灰。\n
　　                              从今以往，勿复相思！\n
　　                              相思与君绝，鸡鸣狗吠，\n
　　                              兄嫂当知之。\n
　　                              妃呼豨！\n
　　                              秋风肃肃晨风飔，东方须臾高知之。""",
                               " "))
        post_data01 = {"gameId": self.game_id,  # Int,游戏的Id
                       "activityType": type,  # String,类型的ID
                       "title": title,  # String,赛事标题
                       "activity_rule_id": rule,  # Int,赛事规则的ID
                       "activity_people": people_id,  # Int,选择人数的ID
                       "model": model,  # String,常规模式(common),奖金池模式(money)
                       "timerule": time_rule,  # Array,时间规则(eg:["2017-03-02 00:00:00"])
                       "password": password,  # Int,赛事的房间密码,非必填
                       "remark": remark}  # String,比赛的介绍,非必填
        post_data = dict(post_data01, **post_data02)
        print(post_data)
        return post_data


if __name__ == '__main__':
    judgement_token = Login().login(14700000001, "aaaaaa")["data"]["auth_token"]
    _run = CreateMatch(judgement_token)
    for i in range(10):
        post_data = _run.post_data(login, 1, "money", 111111)
        print(_run.create_match(login, post_data))
# {'gameId': 1,
#  'activityType': 1,
#  'title': '炉石奖池28日13:49',
#  'activity_rule_id': 6,
#  'activity_people': 6,
#  'model': 'money',
#  'timerule': ['2017-06-28 14:35:13', '2017-06-28 14:50:13'],
#  'password': 111111,
#  'remark': '',
#  'apply_money': 10,
#  'money_rewardrule': {'3': 100, '1': '0'}}



