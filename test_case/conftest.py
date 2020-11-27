# import os
# import allure
# import pytest
# from utils.connmysql import DB
# from utils.readyaml import yam
#
# # dbname = 'MYSQLDB'
# # sql = """select * from aset_bill_d;"""
#
#
# @pytest.fixture(scope="class", autouse=True)
# def sqlselect(dbname, sql):
#     """
#     mysql数据库操作
#
#     """
#     db = DB(
#         yam.host(dbname),
#         yam.port(dbname),
#         yam.database(dbname),
#         yam.user(dbname),
#         yam.password(dbname),
#         yam.charset(dbname)
#     )
#     db.select(sql)
#     db.closedb()
#
#
#
