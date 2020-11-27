from utils.timenum import ts
from utils.timenum import dt1
from utils.timenum import dt2
from utils.timenum import dt3
# 修改timenum.py 增加dt1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
import time
'''
测试数据，每个页面需要多少个数据就在该页面维护多少个数据，数据顺序固定
'''


class csData(object):
    x = str(dt1)
    y = str(dt2)
    z = str(dt3)

    Testcs = [
        (
            "111" ,  # cssj
        )
    ]

    # 资产盘点
    TestAssetsTestA24 = [
        (
            "2020-09-30" ,  # intrtime 输入盘点日期
            "SERVMAT" ,  # asetname 资产名称
            "12",  # asetcnt 输入资产数量
            "500",  # intrcnt 输入盘点个数

        )
    ]

    sqltest = [
        (
            'MYSQLDB',
            """select * from aset_bill_d;"""
        )
    ]

