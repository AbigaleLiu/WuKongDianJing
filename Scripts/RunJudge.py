from Scripts.ConfigFile import *
from Scripts.APIScripts.Competition.Dispute import *
from Scripts.APIScripts.Competition.DisputeInfo import *
from Scripts.APIScripts.Competition.DisputeInto import *
from Scripts.APIScripts.Competition.DisputeJudge import *


class RunJudge:
    def __init__(self, judgement_token):
        self.judgement_token = judgement_token
        self.match_id = ConfigFile().activity_id()

    def run_judge(self):
        dispute_id_list = self.get_dispute_id(self.judgement_token, self.match_id)
        pairs = self.get_dispute_pair(self.judgement_token)
        for i in range(len(dispute_id_list)):
            result_code = random.randint(0, 1)
            winner_id = int(pairs[i][result_code])
            print(DisputeJudge().dispute_judge(self.judgement_token, self.match_id, dispute_id_list[i], winner_id))

    def get_dispute_id(self, judgement_token, match_id):
        dispute_json = Dispute().dispute(judgement_token, match_id)
        dispute_list = []
        for i in dispute_json["data"]["untreated"]:
            dispute_list.append(i["id"])
        return dispute_list

    def get_dispute_pair(self, judgement_token):
        dispute_id_list = self.get_dispute_id(judgement_token, self.match_id)
        print(dispute_id_list)
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

