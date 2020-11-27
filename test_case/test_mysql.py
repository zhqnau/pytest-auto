import pytest
import allure
from utils.connmysql import DB

from pagedata.cs_data import csData
from pageobject.basepage import BasePage


class TestMysql:

    # dbname = 'MYSQLDB'
    # sql = """select * from aset_bill_d;"""

    @pytest.mark.parametrize(
        'dbname, sql', csData.sqltest)
    def test_sql(self, login, dbname, sql):
        # driver = login  # 将登陆后获取的driver传递出来
        # self.driver = BasePage(driver)  # 脚本需要用到 basepage.py中BasePage类的方法，
        # 故把带有登录信息的driver传递给BasePage在赋值给self.driver
        result = DB().sqlselect(dbname, sql)
        print(result)
