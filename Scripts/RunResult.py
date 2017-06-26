from Scripts.APIScripts.Competition.Against import *
from Scripts.ConfigFile import *
from Scripts.APIScripts.Competition.Result import *


class RunResult:
    def __init__(self, match_id, screening):
        self.tokens = ConfigFile().get_token()
        self.judgement_token = Login().login("14700000001", "aaaaaa")["data"]["auth_token"]
        self.match_id = ConfigFile().activity_id()
        self.screening = screening

    def run_result(self):
        choice = input("是否需要指定争议数目（Y/N）")
        if choice == "Y":
            dispute_num = int(input("输入需要的争议数："))
            self.run_result_limit(dispute_num)
        else:
            self.run_result_random()

    def run_result_random(self):
        """
        随机提交比赛结果
        :return:
        """
        for pair in self.against_pair_token():
            for token in pair:
                result_num = random.choice((1, 2))
                if result_num == 1:
                    Result().win(token, self.match_id, self.screening)
                elif result_num == 2:
                    Result().lose(token, self.match_id, self.screening)

    def run_result_limit(self, dispute_num):
        against_pair_token = self.against_pair_token()
        if dispute_num <= len(against_pair_token):
            for i in range(dispute_num):
                Result().win(against_pair_token[i][0], self.match_id, self.screening)
                Result().win(against_pair_token[i][1], self.match_id, self.screening)
            for i in range(dispute_num, len(against_pair_token)):
                for token in against_pair_token[i]:
                    result_num = random.choice((1, 2))
                    if result_num == 1:
                        Result().win(token, self.match_id, self.screening)
                    elif result_num == 2:
                        Result().lose(token, self.match_id, self.screening)

    def against_pair_token(self):
        """
        按照对阵表排列token
        :return:
        """
        pair_list = Against().against(self.judgement_token, self.match_id, self.screening)
        uid_token_bonds = ConfigFile().uid_token_bonds()
        against_pair_token = []
        for pair in pair_list:
            token0 = uid_token_bonds[int(pair[0])]
            token1 = uid_token_bonds[int(pair[1])]
            against_pair_token.append([token0, token1])
        return against_pair_token

if __name__ == '__main__':
    _run = RunResult(66, 2)
    print(_run.run_result())

