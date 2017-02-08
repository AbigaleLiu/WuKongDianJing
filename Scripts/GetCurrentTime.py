#-*- coding: UTF-8 -*-
"""
获取当前时间
"""

import time


class GetCurrentTime:
    def getCurrentTime(self):
        currentTime = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        return currentTime
# getTime = GetCurrentTime()
# getTime.getCurrentTime()
