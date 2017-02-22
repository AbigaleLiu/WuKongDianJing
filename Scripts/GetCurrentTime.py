#-*- coding: UTF-8 -*-

import time
import datetime


class GetCurrentTime:
    """
    获取当前时间、headers时间、日志文件工作表名（当前日期）
    """
    def getCurrentTime(self):
        """
        当前时间
        :return: str
        """
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def getHeaderTime(self):
        """
        headers时间
        :return: str
        """
        dict_week = {0: "Mon",
                     1: "Tue",
                     2: "Wed",
                     3: "Thu",
                     4: "Fri",
                     5: "Sat",
                     6: "Sun"}
        dict_month = {1: "Jan",
                      2: "Feb",
                      3: "Mar",
                      4: "Apr",
                      5: "May",
                      6: "Jun",
                      7: "Jul",
                      8: "Aug",
                      9: "Sep",
                      10: "Oct",
                      11: "Nov",
                      12: "Dec"}
        weekday = dict_week[datetime.datetime.now().weekday()]
        day = datetime.datetime.now().day
        month = dict_month[datetime.datetime.now().month]
        year = datetime.datetime.now().year
        hour_minute_second = time.strftime('%H:%M:%S', time.localtime(time.time()))
        header_time = "%s, %s %s %s %s GMT" % (weekday, day, month, year, hour_minute_second)
        return header_time

    def sheet_time(self):
        """
        日志文件工作表名（当前日期）
        :return: str
        """
        sheet_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return sheet_name
