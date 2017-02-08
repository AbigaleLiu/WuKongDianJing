# _*_ coding:utf-8 _*_
from Scripts.ConfigFile import *
from Scripts.GetReport import *

class LoginReportData:
    def get_login_data(self, login):
        """
        整理登录数据格式
        :param login:
        :return: data
        """
        id = GetReport().get_blank_row_id("login")
        login_request_mode = "post"
        api = "%s/api/member/login" % ConfigFile().host()
        data = [id, login["description"], login_request_mode,
                api, login["mobile"], login["time"], login["status_code"], login["msg"]]
        return data

    def get_login_report(self, login, id):
        """
        逐行写入数据并保存文件
        :param login:
        :param id: 写入行
        """
        report_copy = copy(xlrd.open_workbook(r"%s" % ConfigFile().report_path(), formatting_info=True))
        login_sheet = report_copy.get_sheet("login")
        data = self.get_login_data(login)
        if data[6] == 200:
            for i in range(len(data)):
                login_sheet.write(id, i, data[i], GetReport().style()[2])
                report_copy.save(r"%s" % ConfigFile().report_path())
        else:
            for i in range(len(data)):
                login_sheet.write(id, i, data[i], GetReport().style()[1])
                report_copy.save(r"%s" % ConfigFile().report_path())
def main():
    users = GetUsers()
    r = LoginReportData()
    GetReport().get_report("login")
    for i in range(len(users.get_users())):
        login = Login().login(users.get_mobile(i), users.get_password(i))
        id = GetReport().get_blank_row_id("login")
        r.get_login_report(login, id)
if __name__ == "__main__":
    main()