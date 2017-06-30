from Scripts.ConfigFile import *
from Scripts.APIScripts.Competition.Dispute import *
from Scripts.APIScripts.Competition.DisputeInfo import *
from Scripts.APIScripts.Competition.DisputeInto import *
from Scripts.APIScripts.Competition.DisputeJudge import *


class RunJudge:
    def __init__(self):
        config_file = ConfigFile()
        self.judgement_token = Login().login(config_file.judgement()[0], config_file.judgement()[1])["data"]["auth_token"]
        self.match_id = ConfigFile().activity_id()

    def run_judge(self):
        """
        随机选择争议中的一方为胜
        :return: 判决结果
        """
        dispute_id_list = self.get_dispute_id(self.judgement_token, self.match_id)
        pairs = self.get_dispute_pair(self.judgement_token)
        for i in range(len(dispute_id_list)):
            result_code = random.randint(0, 2)
            if result_code == 2:
                pass
            else:
                winner_id = int(pairs[i][result_code])
                print(DisputeJudge().dispute_judge(self.judgement_token, self.match_id, dispute_id_list[i], winner_id))

    def get_dispute_id(self, judgement_token, match_id):
        """
        获取争议ID列表
        :param judgement_token: 裁判token
        :param match_id: 比赛ID
        :return: 争议ID列表
        """
        dispute_json = Dispute().dispute(judgement_token, match_id)
        dispute_list = []
        for i in dispute_json["data"]["untreated"]:
            dispute_list.append(i["id"])
        return dispute_list

    def get_dispute_pair(self, judgement_token):
        """
        根据争议ID获取争议用户ID
        :param judgement_token:裁判token
        :return:争议用户二维列表
        """
        dispute_id_list = self.get_dispute_id(judgement_token, self.match_id)
        dispute_pair = []
        for dispute_id in dispute_id_list:
            DisputeInto().dispute_into(judgement_token, self.match_id, dispute_id)
            dispute_json = DisputeInfo().dispute_info(judgement_token, self.match_id, dispute_id)
            pair = []
            for i in dispute_json["data"]["users"]:
                pair.append(i["uid"])
            dispute_pair.append(pair)
        return dispute_pair

if __name__ == '__main__':
    judgement_token = Login().login('14700000001', 'aaaaaa')["data"]["auth_token"]
    _run = RunJudge(judgement_token)
    _run.run_judge()

