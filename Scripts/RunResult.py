from Scripts.APIScripts.Competition.Against import *
from Scripts.ConfigFile import *
from Scripts.APIScripts.Competition.Result import *


class RunResult:
    def __init__(self):
        config_file = ConfigFile()
        self.tokens = config_file.get_token()
        self.judgement_token = Login().login(config_file.judgement()[0], config_file.judgement()[1])["data"]["auth_token"]
        self.match_id = config_file.activity_id()
        self.screening = config_file.screening()

    def run_result(self):
        """
        根据输入内容判断是否指定争议数
        :return:
        """
        against_pair_token = self.against_pair_token()
        choice = input("是否需要指定争议数目（Y/N）")
        if choice == "Y":
            dispute_num = int(input("输入需要的争议数："))
            self.run_result_limit(dispute_num, against_pair_token)
        else:
            self.run_result_random(against_pair_token)

    def run_result_random(self, against_pair_token):
        """
        随机提交比赛结果
        :return:
        """
        for pair in against_pair_token:
            for token in pair:
                if token != "0":
                    result_num = random.choice((1, 2, 3))
                    if result_num == 1:
                        Result().win(token, self.match_id, self.screening)
                    elif result_num == 2:
                        Result().lose(token, self.match_id, self.screening)
                    else:
                        pass

    def run_result_limit(self, dispute_num, against_pair_token):
        """
        根据指定的争议数提交结果，轮空用户自动提交胜，其他用户随机提交
        :param dispute_num:
        :param against_pair_token:
        :return:
        """
        # 筛选出有对手的对阵用户ID，轮空用户自动提交胜
        dispute_pair_token = []
        for pair in against_pair_token:
            if pair[0] != "0" and pair[1] != "0":
                dispute_pair_token.append(pair)
            elif pair[0] == "0" and pair[1] != "0":
                Result().win(pair[1], self.match_id, self.screening)
            elif pair[0] != "0" and pair[1] == "0":
                Result().win(pair[0], self.match_id, self.screening)

        # 生成指定数争议
        if dispute_num <= len(dispute_pair_token):
            for i in range(dispute_num):
                Result().win(dispute_pair_token[i][0], self.match_id, self.screening)
                Result().win(dispute_pair_token[i][1], self.match_id, self.screening)
            for i in range(dispute_num, len(dispute_pair_token)):
                # for token in dispute_pair_token[i]:
                #     result_num = random.choice((1, 2))
                #     if result_num == 1:
                #         Result().win(token, self.match_id, self.screening)
                #     elif result_num == 2:
                #         Result().lose(token, self.match_id, self.screening)
                Result().win(random.choice(dispute_pair_token[i]), self.match_id, self.screening)
        else:
            return "争议数大于实际"

    def against_pair_token(self):
        """
        按照对阵表排列token
        :return:
        """
        pair_list = Against().against(self.judgement_token, self.match_id, self.screening)
        uid_token_bonds = ConfigFile().uid_token_bonds()
        against_pair_token = []
        for pair in pair_list:
            if pair[0] == 0:
                token0 = "0"
                token1 = uid_token_bonds[int(pair[1])]
            elif pair[1] == 0:
                token0 = uid_token_bonds[int(pair[0])]
                token1 = "0"
            else:
                token0 = uid_token_bonds[int(pair[0])]
                token1 = uid_token_bonds[int(pair[1])]
            against_pair_token.append([token0, token1])
        return against_pair_token

if __name__ == '__main__':
    _run = RunResult()
    print(_run.run_result())

