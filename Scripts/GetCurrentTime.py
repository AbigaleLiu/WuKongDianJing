#-*- coding: UTF-8 -*-

import time
import datetime
import math
import json


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

    def match_time(self):
        """
        创建比赛时间，日 时：分
        :return: str
        """
        # day = time.strftime("%d")
        match_time = time.strftime("%d{d}%H:%M", time.localtime(time.time())).format(d="日")
        return match_time

    def rule_time(self, people_num):
        rounds = int(math.log2(people_num))
        rule_time = []
        print(rounds)
        time_round = datetime.datetime.now() + datetime.timedelta(minutes=31)
        print(time_round)
        for round in range(rounds+1):
            time_round = time_round + datetime.timedelta(minutes=10)
            time = time_round.strftime("%Y-%m-%d %H:%M:%S")
            rule_time.append(time)
        return rule_time


if __name__ == '__main__':
    _run = GetCurrentTime()
    # print(_run.getCurrentTime())
    # print(_run.sheet_time())
    # print(_run.getHeaderTime())
    # print(_run.match_time())
    # print(_run.rule_time(8))
