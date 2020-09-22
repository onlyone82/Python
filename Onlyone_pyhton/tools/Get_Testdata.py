from tools import project_path
import pandas as pd
class Get_data:
    Cookie=None
    load_id=None
    df=pd.read_excel(project_path.test_case,sheet_name='init')
    tel=df.iloc[0,0]
    login_tel=df.iloc[1,0]
    normal_tel=df.iloc[2,0]
    loan_member_id=df.iloc[3,0]
    memberID=df.iloc[4,0]
if __name__ == '__main__':
    #setattr(Get_data,'Cookie','12346') #设置这个属性值
    hasattr(Get_data,'Cookie') #判断是否有属性值
    #tel=getattr(Get_data,'Cookie')#获取属性值
    print(getattr(Get_data,'tel'))
    print(getattr(Get_data,'login_tel'))
    print(getattr(Get_data,'normal_tel'))
    print(getattr(Get_data,'loan_member_tel'))