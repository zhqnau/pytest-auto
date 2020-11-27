import allure
import pymysql
from utils import logger
from utils.readyaml import yam
'''
数据库连接脚本，先建立连接，在建立游标，使用游标执行sql,执行完毕后关闭游标在关闭连接

close() 关闭
commit() 提交
cursor() 返回Cursor对象，用于执行sql语句并获得结果
execute(operation,[,parameters]) 执行语句，返回受影响的函数，主要用于执行insert，update，delete语句，也可用于执行create，alter，drop等
fetchone() 执行查询语句时，获取查询结果集的第一行数据，返回一个元祖
fetchall() 执行查询时，获取结果集的所有行数，一行构成一个元祖，再讲这些元组装一个元组返回
fetchmany(n) 执行查询时，要取的数据条数，n为要取的条数 ##### Cursor对象 
    功能：用于执行sql语句，常用的是增删改查，获取cursor对象，调用Connection对象的cursor()方法

'''


class MYDB:

    # 导入logger
    logger = logger.Logger.get_logger()

    def __init__(self, host, port, database, user, password, charset):
        # 链接database
        self.conn = pymysql.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            charset=charset,
        )

        # 游标对象，执行sql后返回结果元组显示
        self.cursor = self.conn.cursor()
        self.logger.info("创建游标")
        # 游标对象，执行sql后返回结果字典显示
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 定义sql语句
    # sql = ("select count(1) from aset_bill_d;")
    # logger.info("定义sql: %s" % sql)

    # @allure.step("数据库查询")
    def select(self, sql):
        try:
            # 执行sql
            curs = self.cursor.execute(sql)
            self.conn.commit()
            self.logger.info("执行sql:%s" % sql)

            for i in range(curs):
                result = self.cursor.fetchall()
                self.logger.info("返回执行结果: %s" % result)
                return result

        except:
            # 报错回滚
            self.conn.rollback()
            self.logger.info("执行未回滚数据")
            # 关闭光标对象
            self.cursor.close()
            self.logger.info("关闭游标")
            # 关闭数据库链接
            self.conn.close()
            self.logger.info("关闭数据库链接")

    # @allure.step("关闭数据库连接")
    def __del__(self):

        # 关闭光标对象
        self.cursor.close()
        self.logger.info("关闭游标")
        # 关闭数据库链接
        self.conn.close()
        self.logger.info("关闭数据库链接")


class DB:

    def db(self, dbhandler, sql):

        sqldb = MYDB(
                yam.host(dbhandler),
                yam.port(dbhandler),
                yam.database(dbhandler),
                yam.user(dbhandler),
                yam.password(dbhandler),
                yam.charset(dbhandler)
        )
        db_result = sqldb.select(sql)
        return db_result


if __name__ == '__main__':

    sql = """select * from aset_bill_d;"""
    A = DB()
    B = A.db('MYSQLDB', sql)
    print(type(B))
    print(B[0])
    print(type(B[0]))
    print(B[0].get('ASET_BILL_ID'))

