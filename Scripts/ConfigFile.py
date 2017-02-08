# _*_ coding:utf-8 _*_
"""
配置文件
"""


class ConfigFile:
    def host(self):
        """
        请求接口主机
        :return:
        """
        host_local = "http://192.168.1.184:8012"  # 测试服
        host_official = "http://api.gvgcn.com"  # 正式服
        return host_local

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
        report_path = r"F:\app_Script\Scripts\Reports\report.xls"
        return report_path

    def users_path(self):
        """
        已注册用户文件路径
        :return: users_path
        """
        users_path = r"F:\app_Script\Scripts\users.xlsx"
        return users_path

    def case_path(self):
        """
        测试用例存放目录
        :return: case_path
        """
        case_path = r"F:\app_Script\Scripts\Cases"
        return case_path
