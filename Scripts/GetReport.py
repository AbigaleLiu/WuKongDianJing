# _*_ coding:utf-8 _*_

import xlwt
import xlrd
from xlutils.copy import copy
from Scripts.GetUsers import *
from Scripts.GetCurrentTime import *


class GetReport:
    """
    日志文件相关操作
    """
    report_path = ConfigFile().report_path()
    sheet_name = GetCurrentTime().sheet_time()

    def get_report(self):
        """
        生成xls文件
        :param sheet_name:工作表名称
        """
        title = ["ID", "接口描述", "请求方式", "API", "参数", "执行时间", "状态码", "执行结果"]  # 定义表头
        if not os.path.exists(r"%s" % self.report_path):
            workbook = xlwt.Workbook(encoding="utf-8")  #
            worksheet = workbook.add_sheet(self.sheet_name)
            self.col_width(title, worksheet)
            workbook.save(r"%s" % self.report_path)
        else:
            open_xls = xlrd.open_workbook(r"%s" % self.report_path, formatting_info=True)
            workbook = copy(open_xls)
            if self.sheet_name not in open_xls.sheet_names():
                worksheet = workbook.add_sheet(self.sheet_name)
                self.col_width(title, worksheet)
                workbook.save(r"%s" % self.report_path)
            else:
                workbook.save(r"%s" % self.report_path)
                # print open_xls.sheet_names()

    def col_width(self, title, worksheet):
        """
        设置表格列宽、表头内容
        :param title: 表头
        :param worksheet: 工作表
        """
        worksheet.col(0).width = 3000  # ID列宽
        worksheet.col(1).width = 6000  # 接口描述列宽
        worksheet.col(2).width = 3000  # 请求方式列宽
        worksheet.col(3).width = 15000  # API列宽
        worksheet.col(4).width = 20000  # 参数列宽
        worksheet.col(5).width = 6000  # 执行时间列宽
        worksheet.col(6).width = 3000  # 状态码列宽
        worksheet.col(7).width = 10000  # 执行结果列宽
        for i in range(len(title)):
            worksheet.write(0, i, title[i], self.style()[0])

    def style(self):
        """
        设置单元格格式
        :return:[style_title, style_error, style_normal]
                  style_title：表头湖蓝色背景黑色宋体
                  style_error：红色字体
                  style_normal：黑色字体
        """
        # 设置表头背景色
        pattern_title = xlwt.Pattern()  # 创建一个模式
        pattern_title.pattern = xlwt.Pattern.SOLID_PATTERN  # 设置该模式为实型
        pattern_title.pattern_fore_colour = 0x1b  # 设置背景色为湖蓝色

        # 设置表头字体
        font_title = xlwt.Font()  # 创建字体对象
        font_title.name = 'SimSun'  # 设置字体：宋体
        font_title.colour_index = 8  # 设置字体颜色：黑色
        font_title.bold = True  # 设置边框

        # 设置错误记录字体
        font_error = xlwt.Font()  # 创建错误记录字体对象
        font_error.colour_index = 2  # 设置错误记录字体颜色：红色

        style_title = xlwt.XFStyle()  # 创建表头单元格格式对象
        style_title.font = font_title  # 设置表头字体
        style_title.pattern = pattern_title  # 设置表头背景色
        # style_title.alignment = 0x02  # 设置表头字体居中

        style_normal = xlwt.XFStyle()  # 创建普通单元格格式对象
        # style_normal.alignment = 0x01  # 设置普通单元格字体居左

        style_error = xlwt.XFStyle()  # 创建出错记录单元格格式对象
        style_error.font = font_error  # 设置错误记录字体
        # style_error.alignment = 0x01  # 设置错误记录字体居左

        return [style_title, style_error, style_normal]

    def get_blank_row_id(self):
        """
        获取当前工作表记录条数
        :param sheet_name: 工作表名称
        :return: 有内容的行数
        """
        workbook = xlrd.open_workbook(r"%s" % self.report_path)
        sheet = workbook.sheet_by_name(self.sheet_name)
        return sheet.nrows

    def record_into_report(self, api_data):
        """
        将本条日志写入文件
        :param api_data: list
        :return:
        """
        id = GetReport().get_blank_row_id()
        report_copy = copy(xlrd.open_workbook(r"%s" % ConfigFile().report_path(), formatting_info=True))
        sheet = report_copy.get_sheet(self.sheet_name)
        api_data.insert(0, id)
        if api_data[6] == 200:
            for i in range(len(api_data)):
                sheet.write(id, i, api_data[i], self.style()[2])
                report_copy.save(r"%s" % ConfigFile().report_path())
        else:
            for i in range(len(api_data)):
                sheet.write(id, i, api_data[i], self.style()[1])
                report_copy.save(r"%s" % ConfigFile().report_path())


if __name__ == "__main__":
    r = GetReport()
    r.get_report()
    print(r.style())