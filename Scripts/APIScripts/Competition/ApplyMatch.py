# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_p
from Scripts.GetCurrentTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.PersonalCenter.RoleList import *
from Scripts.APIScripts.Other.Login import *


class ApplyMatch:
    """
    报名比赛
    """
    def apply_match(self, id, token, role_id):
        """
        报名比赛
        :param login: json，获取token
        :param id: 赛事ID
        :param role_id: 角色ID
        :param password: 房间密码
        :return: json
        """
        post_data = {"id": "%d" % id,
                    "roleId": "%d" % role_id,
                    "password": "%s" % ""}
        headers = {"Cache - Control": "no - cache",
                    "Content - Type": "text / html;charset = UTF - 8",
                    'Accept': 'application/json',
                    'Authorization': token,
                    "Date": "%s" % GetCurrentTime().getHeaderTime(),
                    "Proxy - Connection": "Keep - alive",
                    "Server": "nginx / 1.9.3(Ubuntu)",
                    "Transfer - Encoding": "chunked"}
        apply_match_url = "http://%s/activity/%s/sign" % (ConfigFile().host(), id)
        request = requests.post(apply_match_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
                print(info)
        finally:
            log_list = [u'报名比赛', u"post", apply_match_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志

    # def get_data(self):
    #     users = GetUsers().get_users()
    #     datas = {}
    #     for user in range(len(users)):
    #         login = Login().login(GetUsers().get_mobile(user), GetUsers().get_password(user))
    #         token = login["data"]["auth_token"]
    #         role_id = RoleList().role_list(login)["data"][-1]["id"]
    #         datas[token] = role_id
    #      # print(datas)
    #     return datas
    def get_data(self):
        datas = {}
        workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\wk.xlsx")  # 打开文件
        sheet = workbook.sheet_by_name(r"wk")  # 根据索引获取工作表
        for row_num in range(sheet.nrows):
            row = sheet.row_values(row_num)
            datas[row_num+1] = "Bearer " + row[0]
        return datas


if __name__ == "__main__":
    pool = mul_p.Pool(processes=10)
    result = []
    instance = ApplyMatch()
    user_datas = instance.get_data()
    for role_id in user_datas:
        result.append(pool.apply_async(func=instance.apply_match, args=(104, user_datas[role_id], role_id)))
    pool.close()
    pool.join()
    for r in result:
        print(r.get())



