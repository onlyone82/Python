import mysql.connector
from tools import project_path
from tools.read_config import Readconfig
class DoMysql:
    def do_mysql(self,query_sql,state='all'): #query_sql查询语句;status 执行的条数
        db_config=eval(Readconfig.get_config(project_path.config_path,'DB','db_config'))
        #创建一个数据库连接
        cnn=mysql.connector.connect(**db_config)
        #游标cursor
        cursor=cnn.cursor()
        #写sql语句

        #执行语句
        cursor.execute(query_sql)
        #获取结果 打印结果
        if state==1:
            res=cursor.fetchone() #针对一条数据
        else:
            res=cursor.fetchall() #列表，针对多行数据  列表嵌套元祖
        cursor.close()
        cnn.close()
        return res
if __name__ == '__main__':
    print(

    DoMysql().do_mysql("select max(MobilePhone) from member")[0][0])
    print(DoMysql().do_mysql("show databases"))

