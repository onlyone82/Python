import requests
from tools.My_log import MyLog
my_log=MyLog()
class Httprequest:
    @staticmethod
    def http_quest(url,data,http_method,cookie=None):
        try:
            if http_method.upper()=="GET":
                res=requests.get(url,data,cookies=cookie)
            elif http_method.upper()=="POST":
                res=requests.post(url,data,cookies=cookie)
            else:
                MyLog.info("输入的方法不对")
        except Exception as e:
            MyLog.error("请求报错了：{0}".format(e))
            raise e
        return res #返回结果
if __name__ == '__main__':
    url="http://test.lemonban.com/futureloan/mvc/api/member/login"
    data={"mobilephone":18688773467,"pwd":"123456"}
    login_url="http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    login_data={"mobilephone":18201156418,"amount":"1000"}
    login_ret=Httprequest().http_quest(url,data,'get')
    print(login_ret.json())
    ret=Httprequest().http_quest(login_url,login_data,"get",login_ret.cookies)
    print(ret.json())