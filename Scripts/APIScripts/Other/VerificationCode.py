# _*_ coding:utf-8 _*_
import os
import time


class VerificationCode:
    """
    获取短信验证码
    """
    def verification_code(self):
        os.system("adb logcat -c")  # 清空当前日志缓存
        cmd = "adb logcat -d |findstr E/SmsRec"  # 将日志发送到屏幕|查找文件中包含目标字符串的行
        time.sleep(30)
        while (1):
            ver_code = os.popen(cmd).read()
            print(ver_code)
            if ver_code:
                ver_code = ver_code.split("验证码：")[1].split("，")[0]
                break
        print(ver_code)


def main():
    r = VerificationCode()
    r.verification_code()
if __name__ == "__main__":
    main()