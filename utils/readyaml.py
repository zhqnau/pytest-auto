import yaml
import os
from utils.dir_config import db_dir

'''
读取yaml文件
数据库地址，用户账户秘密验证码
'''


class ReadYaml:

    def __init__(self):
        if not os.path.exists(db_dir):
            raise FileNotFoundError("数据库配置文件%s不存在！" % db_dir)

    def _read(self, section, option):
        f = open(db_dir, 'r', encoding="utf-8")
        data = f.read()
        f.close()
        # 将字符串转化为字典或列表
        return yaml.safe_load(data).get(section).get(option)

    # @property
    def host(self, dbname):
        return self._read(dbname, 'host')

    # @property
    def port(self, dbname):
        return self._read(dbname, 'port')

    # @property
    def user(self, dbname):
        return self._read(dbname, 'user')

    # @property
    def password(self, dbname):
        return self._read(dbname, 'password')

    # @property
    def database(self, dbname):
        return self._read(dbname, 'database')

    # @property
    def charset(self, dbname):
        return self._read(dbname, 'charset')


yam = ReadYaml()

if __name__ == '__main__':
    print(yam.host('MYSQLDB'))
    print(yam.port)
    print(yam.user)
    print(yam.password)
    print(yam.database)
    print(yam.charset)
