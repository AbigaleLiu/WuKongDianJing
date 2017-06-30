# _*_ coding:utf-8 _*_
import requests
import multiprocessing as mul_p
from Scripts.GetTime import *
from Scripts.GetReport import *
from Scripts.GetUsers import *
from Scripts.APIScripts.PersonalCenter.RoleList import *
from Scripts.APIScripts.Other.Login import *


class ApplyMatch:
    """
    报名比赛
    """
    def __init__(self):
        config_file = ConfigFile()
        self.match_id = config_file.activity_id()
        # self.password = config_file.activity_password()

    def apply_match(self, token, role_id, password=None):
        """
        报名比赛
        :param login: json，获取token
        :param role_id: 角色ID
        :param password: 房间密码
        :return: json
        """
        post_data = {"id": "%d" % self.match_id,
                    "roleId": "%d" % role_id,
                    "password": "%s" % password}
        headers = {"Cache - Control": "no - cache",
                    "Content - Type": "text / html;charset = UTF - 8",
                    'Accept': 'application/json',
                    'Authorization': token,
                    "Date": "%s" % GetTime().getHeaderTime(),
                    "Proxy - Connection": "Keep - alive",
                    "Server": "nginx / 1.9.3(Ubuntu)",
                    "Transfer - Encoding": "chunked"}
        apply_match_url = "http://%s/activity/%s/sign" % (ConfigFile().host(), self.match_id)
        request = requests.post(apply_match_url, data=post_data, headers=headers)
        time = GetTime().getCurrentTime()
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
    #         GetReport().get_report()  # 生成或打开日志文件
    #         GetReport().record_into_report(log_list)  # 逐条写入日志






