import configparser
from tools import project_path
class Readconfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
if __name__ == '__main__':
    res=eval(Readconfig.get_config(project_path.config_path,'MODE','mode'))
    for key in res:
        print(res[key])


