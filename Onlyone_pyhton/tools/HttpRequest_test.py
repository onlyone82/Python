import unittest
from tools.http_request import Httprequest
from tools.Get_Testdata import Get_data
from ddt import ddt,data
from tools.Do_excle import Do_excle
from tools import project_path
from tools.My_log import MyLog
my_log=MyLog()
test_data=Do_excle.get_data(project_path.test_case)
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    @data(*test_data)
    def test_api(self,item):
        #请求之前完成load_id替换

        res=Httprequest.http_quest(item['url'],eval(item['data']),item['http_method'],getattr(Get_data,"Cookie"))
        if res.cookies:  #设置cookies值,登录成功后，产生cookies
            setattr(Get_data,"Cookie",res.cookies)
        try:
            self.assertEqual(str((item['expected'])),res.json()['code'])  #添加断言
            Testresult="成功"
        except AssertionError as e:
            my_log.info("执行用例出错了{}".format(e))
            Testresult="失败"
            raise e
        finally:
            Do_excle().write_back(project_path.test_case,item['sheet_name'],item['case_id']+1,str(res.json()),Testresult)
            my_log.info("获取的结果是：{}".format(res.json()))
    def tearDown(self) -> None:
        pass