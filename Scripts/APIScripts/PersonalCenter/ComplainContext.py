# _*_ coding:utf-8 _*_
from Scripts.APIScripts.Other.Login import *
from Scripts.GetReport import *
import multiprocessing as mul_p  # 导入模块并使用别名


class ComplainContext(mul_p.Process):
    """
    提交用户反馈
    """
    # def __init__(self):
    #     """
    #     构造函数
    #     """
    #     print "Constructor ... %s" % mul_p.current_process().name
    #
    # def __del__(self):
    #     """
    #     析构函数
    #     :return:
    #     """
    #     print "... Destructor %s" % mul_p.current_process().name
    #
    # def __call__(self, login, content=""):
    #     """
    #     参考：https://blog.tankywoo.com/2015/09/06/cant-pickle-instancemethod.html
    #     当想让一个类中的方法多进程并发运行报错原因：
    #     multiprocessing会对调用的函数做序列化, 然后method不可被序列化。
    #     解决方案：
    #     1.将方法提为global：
    #         i.设置代理函数
    #         ii.定义__call__，可以将类实例传给pool，因为顶层定义的类是可被序列化的
    #     2.用copy_reg将MethodType注册为可序列化
    #     :param content:
    #     :return:
    #     """
    #     return self.complain_context(content)

    def complain_context(self, content, type):
        """
        提交用户反馈
        :param content: 反馈内容
        :return:
        """
        post_data = {"content": "%s" % content,
                     "type": "%d" % type}  # 1：功能建议；2：产品BUG
        headers = {"Cache - Control": "no - cache",
                   "Content - Type": "text / html;charset = UTF - 8",
                   'Accept': 'application/json',
                   'Authorization': Login().login("18708125570", "aaaaaa")["data"]["auth_token"],
                   "Date": "%s" % GetCurrentTime().getHeaderTime(),
                   "Proxy - Connection": "Keep - alive",
                   "Server": "nginx / 1.9.3(Ubuntu)",
                   "Transfer - Encoding": "chunked"}
        complain_type_url = "http://%s/complaint/opinion" % ConfigFile().host()
        request = requests.post(complain_type_url, data=post_data, headers=headers)
        time = GetCurrentTime().getCurrentTime()
        status_code = request.status_code
        try:
            if status_code in (200, 422):
                json = request.json()
                info = json["info"]
                return json
            else:
                info = request.reason
        finally:
            log_list = [u'提交用户反馈', u"post", complain_type_url, str(post_data), time, status_code, info]  # 单条日志记录
            GetReport().get_report()  # 生成或打开日志文件
            GetReport().record_into_report(log_list)  # 逐条写入日志

    # def run(self):
    #     pool = mul_p.Pool(processes=10)
    #     for i in range(10):
    #         text01 = "石室诗士施氏，嗜狮，誓食十狮，氏时时适市视狮，十时，适十狮适市。是时，适施氏适市，氏视是十狮，恃矢势，" \
    #                 "使是十狮逝世，氏拾是十狮尸，适石室，石室湿，氏使侍拭石室，石室拭，氏始试食十狮尸，食时，始识是十狮尸，" \
    #                 "实十石狮尸。试释是事。"
    #         text02 = "季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。鸡既济，跻姬笈，季姬忌，急咭鸡，鸡急，继圾几，" \
    #                  "季姬急，即籍箕击鸡，箕疾击几伎，伎即齑，鸡叽集几基，季姬急极屐击鸡，鸡既殛，季姬激，即记《季姬击鸡记》"
    #         text03 = "芝之稚侄郅，至智，知制纸，知织帜。芝痔，炙痔，痔殖，郅至芝址，知之，知芷汁治痔，至芷址执芷枝，狾至，" \
    #                  "踯，郅执直枝掷之，枝至狾趾，狾止。郅执芷枝致芝，芝执芷治痔，痔止。芝炙脂雉肢致郅。"
    #         text04 = "羿裔熠①,邑②彝,义医,艺诣。 熠姨遗一裔伊③,伊仪迤,衣旖,异奕矣。熠意④伊矣,易衣以贻伊,伊遗衣," \
    #                  "衣异衣以意异熠,熠抑矣。 伊驿邑,弋一翳⑤,弈毅⑥，毅仪奕,诣弈,衣异,意 逸。毅诣伊,益伊,伊怡," \
    #                  "已臆⑦毅矣,毅亦怡伊。翌,伊亦弈毅。毅以蜴贻伊,伊亦贻衣以毅。伊疫,呓毅,癔异矣,倚椅咿咿,毅亦咿咿。" \
    #                  "毅诣熠,意以熠,议熠医伊,熠懿⑧毅,意役毅逸。毅以熠宜伊,翼逸。熠驿邑以医伊,疑伊胰痍⑨,以蚁医伊," \
    #                  "伊遗异,溢,伊咦。熠移伊,刈薏⑩以医,伊益矣。 伊忆毅,亦呓毅矣,熠意伊毅已逸,熠意役伊。伊异,噫,缢。 " \
    #                  "熠癔,亦缢。"
    #         content = random.choice((text01, text02, text03, text04))
    #         # pool.apply_async(self, args=(content,))
    #         # pool.map(self, (content,))
    #         pool.map_async(self, content)
    #     pool.close()
    #     pool.join()
if __name__ == "__main__":
    # _run = ComplainContext()
    # _run.run()
    text01 = "石室诗士施氏，嗜狮，誓食十狮，氏时时适市视狮，十时，适十狮适市。是时，适施氏适市，氏视是十狮，恃矢势，" \
            "使是十狮逝世，氏拾是十狮尸，适石室，石室湿，氏使侍拭石室，石室拭，氏始试食十狮尸，食时，始识是十狮尸，" \
            "实十石狮尸。试释是事。"
    text02 = "季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。鸡既济，跻姬笈，季姬忌，急咭鸡，鸡急，继圾几，" \
            "季姬急，即籍箕击鸡，箕疾击几伎，伎即齑，鸡叽集几基，季姬急极屐击鸡，鸡既殛，季姬激，即记《季姬击鸡记》"
    text03 = "芝之稚侄郅，至智，知制纸，知织帜。芝痔，炙痔，痔殖，郅至芝址，知之，知芷汁治痔，至芷址执芷枝，狾至，" \
                     "踯，郅执直枝掷之，枝至狾趾，狾止。郅执芷枝致芝，芝执芷治痔，痔止。芝炙脂雉肢致郅。"
    text04 = "羿裔熠①,邑②彝,义医,艺诣。 熠姨遗一裔伊③,伊仪迤,衣旖,异奕矣。熠意④伊矣,易衣以贻伊,伊遗衣," \
            "衣异衣以意异熠,熠抑矣。 伊驿邑,弋一翳⑤,弈毅⑥，毅仪奕,诣弈,衣异,意 逸。毅诣伊,益伊,伊怡," \
            "已臆⑦毅矣,毅亦怡伊。翌,伊亦弈毅。毅以蜴贻伊,伊亦贻衣以毅。伊疫,呓毅,癔异矣,倚椅咿咿,毅亦咿咿。" \
            "毅诣熠,意以熠,议熠医伊,熠懿⑧毅,意役毅逸。毅以熠宜伊,翼逸。熠驿邑以医伊,疑伊胰痍⑨,以蚁医伊," \
            "伊遗异,溢,伊咦。熠移伊,刈薏⑩以医,伊益矣。 伊忆毅,亦呓毅矣,熠意伊毅已逸,熠意役伊。伊异,噫,缢。 " \
            "熠癔,亦缢。"
    content = random.choice((text01, text02, text03, text04))
    _run = ComplainContext()
    print(_run.complain_context(content, type=1))
