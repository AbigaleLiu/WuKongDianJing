# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
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
    def create_match(self, login, post_data):
        headers = {"Cache - Control": "no-cache",
                   "Content - Type": "application/json;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy-Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        create_match_url = "http://%s/activity" % ConfigFile().host()
        request = requests.post(create_match_url, json=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
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

    def post_data(self, login, game_id, model, password=None):
        type = random.choice(MatchType().match_type(login, game_id)["data"])["id"]
        rule = random.choice(MatchRule().match_rule(login, game_id)["data"])["id"]
        people_data = random.choice(MatchPeople().match_people(login, game_id)["data"])
        people_id = people_data["id"]
        people_num = people_data["count"]
        # print(type(people_num))
        time_rule = GetCurrentTime().rule_time(int(people_num))
        if game_id == 1:
            game = "炉石"
        elif game_id == 2:
            game = "英雄"
        else:
            game = "守望"
        if model == "common":
            model_name = "常规"
            frozen = random.choice([100, 200, 1000])
            reward = ConfigFile().raward(people_num, frozen)
            post_data02 = {"frozen": frozen,  # int，总蟠桃数
                           "common_rewardrule": reward}  # Array,奖金规则,数组的键一定不能变(1,2,3,4,8,16)
        else:
            model_name = "奖池"
            entry_fee = 10
            reward = ConfigFile().raward(people_num)
            post_data02 = {"apply_money": entry_fee,  # Int,报名费用.
                           "money_rewardrule": reward}  # Array,奖金规则.eg：{"1":50}
        match_time = GetCurrentTime().match_time()
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
                               ""))
        post_data01 = {"gameId": game_id,  # Int,游戏的Id
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
    login = Login().login(18712345600, "aaaaaa")
    _run = CreateMatch()
    post_data = _run.post_data(login, 1, "money", 111111)
    for i in range(100):
        # post_data = {"gameId": 1,
        #              "activityType": 1,
        #              "title": "自动创建比赛%d" % i,
        #              "activity_rule_id": 3,
        #              "activity_people": 3,
        #              "model": "common",
        #              # "timerule": ['2017-04-11 15:30', '2017-04-11 15:41', '2017-04-11 15:52', '2017-04-11 16:03','2017-04-11 16:14','2017-04-11 16:25','2017-04-11 16:36'],
        #              "timerule": ['2017-05-26 23:44', '2017-05-31 18:21', '2017-05-31 19:32', '2017-05-31 20:32'],
        #              # "timerule": ['2017-04-30 16:07', '2017-05-31 15:21', '2017-05-31 15:32', '2017-05-31 15:43'],
        #              # "timerule": ['2017-03-30 16:07', '2017-03-31 15:21', '2017-03-31 15:32', '2017-03-31 15:43','2017-03-31 15:54','2017-03-31 16:05','2017-03-31 16:16','2017-03-31 16:27','2017-03-31 16:38','2017-03-31 16:49','2017-03-31 17:41'],
        #              "password": 123456,
        #              "remark": "1111",
        #              "frozen": "100",
        #              "common_rewardrule": {'1': 50, '2': 30, '3': 20}}
        print(_run.create_match(login, post_data))



