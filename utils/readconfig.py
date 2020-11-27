# -*- coding:utf-8 -*-
import os
import configparser
from utils.dir_config import ini_path

'''
读取config文件
测试地址，用户账户秘密验证码
'''

HOST = 'HOST'
username = 'username'
password = 'password'
verificationCode = 'verificationCode'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(ini_path):
            raise FileNotFoundError("配置文件%s不存在！" % ini_path)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(ini_path, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(ini_path, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @property
    def username(self):
        return self._get(username, username)

    @property
    def password(self):
        return self._get(password, password)

    @property
    def verificationCode(self):
        return self._get(verificationCode, verificationCode)


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.url)
    print(ini.username)
    print(ini.password)
    print(ini.verificationCode)

