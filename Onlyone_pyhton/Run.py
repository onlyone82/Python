import unittest
import HTMLTestRunnerNew
from tools import project_path
from tools.HttpRequest_test import TestHttpRequest
suite=unittest.TestSuite()
# suit.addTest(TestHttpRequest('test_api'))
#执行测试用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(project_path.test_result,"wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
    stream=file,
    title='测试报告',
    description='这个是单元测试报告',
    tester='onlyone')
    runner.run(suite)