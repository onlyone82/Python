import os
#专门用来读取路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
path=os.path.realpath(__file__)
# print(project_path)
#测试用例的路径
test_case=os.path.join(project_path,'test_data','test_data.xlsx')
print(test_case)
#测试报告的路径
test_result=os.path.join(project_path,'test_result','html_report','test_api.html')
#print(test_result)
#配置文件的路径
config_path=os.path.join(project_path,'conf','case.config')
print(config_path)
#配置日志路径
log_path=os.path.join(project_path,'log','test.log')