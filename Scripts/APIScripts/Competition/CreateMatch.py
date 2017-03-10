# _*_ coding:utf-8 _*_
import requests
from Scripts.GetCurrentTime import *
from Scripts.ConfigFile import *
from Scripts.GetReport import *
from Scripts.APIScripts.Other.Login import *

class CreateMatch:
    """
    创建比赛
    """
    def create_match(self, login):
        post_data = self.post_data()
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        create_match_url = "http://%s/creatematch" % ConfigFile().host()
        request = requests.post(create_match_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取角色列表', u"get", create_match_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json

    def post_data(self):
        game_id = random.randint(1, 3)  # 1：炉石；2：英雄联盟；3：守望
        type = ""
        model = ""
        if game_id == 1:
            game = "炉石"
        elif game_id == 2:
            game = "英雄"
        else:
            game = "守望"
        if model == "common":
            model_name = "常规"
        else:
            model_name = "奖池"
        match_time = GetCurrentTime().match_time()
        title= game + model_name + match_time
        password = random.choice(["","121314"])

        post_data = {"gameId": "%d" % game_id,  # Int,游戏的Id
                     "activityType":	"%s" % type,  # String,类型的ID
                     "title": "%s" % title,  # String,赛事标题
                     "activity_rule_id": "%d" % rule,  # Int,赛事规则的ID
                     "activity_people": "%d" % people,  # Int,选择人数的ID
                     "model": "%s" % model,  # String,常规模式(common),奖金池模式(money)
                     "timerule": "%s" % timerule,  # Array,时间规则(eg:["2017-03-02 00:00:00"])
                     "password": "%d" % password,  # Int,赛事的房间密码,非必填
                     "remark": "%s" % remark,  # String,比赛的介绍,非必填
                     # 常规模式必填
                     "frozen": "%d" % frozen,  # int，总蟠桃数
                     "common_rewardrule": "%s" % reward,  # Array,奖金规则,数组的键一定不能变(1,2,3,4,8,16).
                     # 奖金池模式必填
                     "apply_money": "%d" % entry_fee,  # Int,报名费用.
                     "money_rewardrule": "%s" % reward}  # Array,奖金规则.eg：{"1":50%}
        return post_data


if __name__ == '__main__':
    login = Login().login(GetUsers().get_mobile(), GetUsers().get_password())
    _run = CreateMatch()
    _run.create_match(login)




