# _*_coding:utf-8 _*_
from Scripts.APIScripts.PersonalCenter.AddRole import *
import requests
from Scripts.GetReport import *
class GameBackgroudImage:
    """
    获取游戏背景图片（切换游戏时）
    """
    def game_backgroud_image(self, login, game_id):
        """
        获取游戏背景图
        :param login:
        :return:
        """
        post_data = {"gameId": "%d" % game_id}  # 选填，填写后选择的游戏优先显示
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': login["data"]["auth_token"],
                   "page": "",  # 分页，有默认值
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        game_backgroud_image_url = "http://%s/games/image" % ConfigFile().host()
        request = requests.get(game_backgroud_image_url, post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        if status_code == 200 or 422:
            info = request.json()["info"]
        else:
            info = request.reason
        json = request.json()
        log_list = [u'获取游戏背景图', u"get", game_backgroud_image_url, str(post_data), time, status_code, info]  # 单条日志记录
        GetReport().get_report()  # 生成或打开日志文件
        GetReport().record_into_report(log_list)  # 逐条写入日志
        return json


if __name__ == '__main__':
    login = Login().login("18708125570", "aaaaaa")
    r = GameBackgroudImage()
    print(r.game_backgroud_image(login, 1))
