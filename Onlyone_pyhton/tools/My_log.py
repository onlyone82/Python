import logging
from tools import project_path
class MyLog:
    def mylog(self,message,level):
        #定义一个日志收集器my_loger
        my_loger=logging.getLogger("python")
        #设定级别
        my_loger.setLevel("DEBUG")
        #设置输出格式：
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        #创建一个我们自己的输出渠道
        ch=logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh=logging.FileHandler(project_path.log_path,encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)
        #两者对接
        my_loger.addHandler(ch)
        my_loger.addHandler(fh)
        #收集日志
        if level=="DEBUG":
            my_loger.debug(message)
        elif level=="INFO":
            my_loger.error(message)
        elif level=="WARNING":
            my_loger.warning(message)
        elif level=="ERROR":
            my_loger.error(message)
        else:
            my_loger.critical(message)
        #关闭日志收集器
        my_loger.removeHandler(ch)
        my_loger.removeHandler(fh)
    def debug(self,msg):
        self.mylog(msg,'DEBUG')
    def error(self,msg):
        self.mylog(msg,'ERROR')
    def warning(self,msg):
        self.mylog(msg,'WARNING')
    def info(self,msg):
        self.mylog(msg,'INFO')
    def critical(self,msg):
        self.mylog(msg,'CRITICAL')
if __name__ == '__main__':
    MyLog().debug("我要放假了！！！")