from utils.timenum import ts
from utils.timenum import dt1
from utils.timenum import dt2
from utils.timenum import dt3
# 修改timenum.py 增加dt1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
import time
'''
测试数据，每个页面需要多少个数据就在该页面维护多少个数据，数据顺序固定
'''


class mhData(object):
    x = str(dt1)
    y = str(dt2)
    z = str(dt3)

    txlglbz = [
        (
            "通讯录备注，备注时间"+x
        )
    ]
    txlzwh = [
        (
            "测试通讯录组"+x
        )
    ]
    znxxfw = [
        (
            "自动化消息",
            "自动化消息内容"+x

        )
    ]
    dxxxsp = [
        (
            "自动化消息",
            "自动化消息审批通过"

        )
    ]
    CMSmbbj = [
        (
            "自动化"+x,
            "11223344"

        )
    ]
    CMSmbsp = [
        (
            "自动化" + x,
            "11223344"

        )
    ]
    CMSlmbj = [
        (
            "自动化" + y,
            "11223344"

        )
    ]
    CMSlmnrbj = [
        (
            "自动化" + y,
            "11223344"

        )
    ]
    xmfb = [
        (
            "XM" + y,
            "自动化项目"+y,
            "10000",
            "自动化测试项目"+y,
            "自动化录入里程碑内容",
            "李明"

        )
    ]
    xmjtsq = [
        (
            "XM" + z

        )
    ]
    wjfw = [
        (
            "自动化添加文件备注" + y,
            "11223344"

        )
    ]
    xmjtps = [
        (
                "XM" + z,
                "李",
                "自动化评审通过" + y

        )
    ]
    xmjtsp = [
        (
            "XM" + z,
            "李",
            "自动化审批通过" + y

        )
    ]
    xmcg = [
        (
            "XM" + z,
            "李",
            "自动化审批通过" + y

        )
    ]
    xsbx = [
        (
            "10000",
            "18812345678",
            "622688124826895211"

        )
    ]
    xtgl1 = [
        (
            "123123123123",
            "13213123123",
            "13213123123"

        )
    ]
    xtgl2 = [
        (
            "110101198001010096",
            "张三",
            "test"+ y,
            "13122221111",
            "Gsc.12345"

        )
    ]

    xtgl3 = [
        (
            y,
            "/test/1",

        )
    ]
    xtgl4 = [
        (
            "子系统"+y,
            y,
            "/test/1",

        )
    ]
    xtgl5 = [
        (
            "自动化角色" + y
        )
    ]
    xtgl6 = [
        (
                "010-33"+y
        )
    ]
class MhData(object):

    # 获取时间戳作为数据编号，防止数据唯一性导致运行出错
    x = str(ts)

    #
    # 资产购置需求数据
    TestAssetsTestA01 = [
        (
            "SERVMAT" + x,  # asetname 资产名称
            "2" ,  # asetcnt 输入资产数量
            "个",  # asetmtrUnt 输入计量单位
            "SERVMAT" + x,  # appyrea 输入使用原因
        )
    ]
    # 资产购置计划
    TestAssetsTestA02 = [
        (
            "SERVMAT" + x,  # purcplanname 购置计划名称
            "2020-09-25",  # planTimeks 开始时间
            "2020-09-29",  # planTimejs 结束时间
            "SERVMAT" + x,  # asetname 资产名称
            "5" ,  # asetcnt 资产数量
            "个" ,  # asetmtrUnt 资产单位
            "233",  # budgpric 资产单价
            "SERVMAT" + x,  # palnname 购置计划名称

        )
    ]
    # 资产购置计划审批
    TestAssetsTestA03 = [
        (
            "SERVMAT" ,  # palnname 计划名称
            # "2" ,  # asetcnt 输入资产数量
            # "个",  # asetmtrUnt 输入计量单位
            "SERVMAT" + x,  # apprOpnnxx 输入sp原因
        )
    ]
    # 供应商管理
    TestAssetsTestA04 = [
        (
            "SERVMAT" + x ,  # splername 录入供应商名称
            "SERVMAT" ,  # conername 录入联系人
            "13244332211",  # telno 录入联系方式
            "SERVMAT" + x,  # spleraddr 录入供货商地址
            "6217991123221234212",  # bankcardno 录入银行卡号

        )
    ]
    # 资产预算询价管理
    TestAssetsTestA05 = [
        (
            "SERVMAT"  ,  # planname 计划名称
            "SERVMAT" ,  # splername 供应商名称
            "132",  # rpuppric 单价
            "SERVMAT",  # bradmol 品牌
            # "6217991123221234212",  # bankcardno 录入银行卡号

        )
    ]
    # 资产预算申报管理
    TestAssetsTestA06 = [
        (
            "SERVMAT"  ,  # planame 购置计划名称
            "SERVMAT" ,  # inquiryname 资产名称
            "SERVMAT",  # name 计划名称
        )
    ]
    # 资产预算申报审批
    TestAssetsTestA07 = [
        (
            "SERVMAT" ,  # name 计划名称
            "SERVMAT" + x,  # appropnn 审批意见
        )
    ]
    # 资产预算申报审批
    TestAssetsTesta08 = [
        (
            "SERVMAT" ,  # splername 计划名称
            "SERVMAT" ,  # planname 审批意见
        )
    ]
    # 资产采购付款管理
    TestAssetsTestA09 = [
        (
            "SERVMAT" ,  # splername 计划名称
            # "SERVMAT" ,  # planname 审批意见
        )
    ]
    # 资产入库管理
    TestAssetsTestA10 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            # "SERVMAT" ,  # planname 审批意见
            "SERVMAT",  # wrhsloc 输入仓库位置
            "SERVMAT",  # regerinput 输入登记人

        )
    ]
    # 资产入库管理
    TestAssetsTestA11 = [
        (
            "SERVMAT" ,  # ordername 资产名称
            "1" ,  # asetcnt 出库数量
            "测试二",  # recername 用户姓名
            "测试二",  # regerinput 登记人

        )
    ]
    # 资产入库管理
    TestAssetsTest12 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            "1" ,  # assetcnt 出库数量
            "SERVMAT" + x,  # usedtextarea 用户姓名

        )
    ]
    # 资产入库管理
    TestAssetsTest13 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            # "1" ,  # assetcnt 出库数量
            "SERVMAT" + x,  # appropnn 输入审批意见

        )
    ]
    # 资产分配管理
    TestAssetsTest14 = [
        (
            "0924测试" ,  # asetname 资产名称
            # "1" ,  # assetcnt 出库数量
            "测试二" ,  # ownrname 输入审批意见

        )
    ]
    # 资产分配管理
    TestAssetsTestA15 = [
        (
            "测试二" ,  # volauser 用户姓名
            "SERVMAT" + x ,  # volaReatextarea 输入违规原因
            "SERVMAT" + x ,  # dspoRslttextarea 输入资产处置结果
            "SERVMAT" + x,  # memotextarea 输入备注

        )
    ]
    # 资产分配管理
    TestAssetsTestA16 = [
        (
            "0924测试" + x  ,  # invdReatextarea 填写报废原因
            # "1" ,  # assetcnt 出库数量
            "0924测试" ,  # asetname 资产名称

        )
    ]
    # 资产折旧摊销
    TestAssetsTestA17 = [
        (
            "水杯0925"   ,  # asetname 资产名称
            "0.9" ,  # resrinput 残值率
            "2020" ,  # yeartime 输入折旧开始年份
            "2",  # usedyears 输入预计使用年限
            "测试" + x,  # memotextarea 输入备注
            # "水杯0925",  # asetname 资产名称

        )
    ]
    # 资产折旧摊销审核
    TestAssetsTestA18 = [
        (
            "测试二"  ,  # submituser 提交人
            "测试" + x,  # appropnn 输入审批意见

        )
    ]
    # 资产回收
    TestAssetsTestA19 = [
        (
            "水杯0925"  ,  # asetname 资产名称
            "测试二" + x,  # retnerinput 输入返还人

        )
    ]
    # 资产回收
    TestAssetsTestA20 = [
        (
            "SERVMAT" ,  # billname 点击票据名称
            "测试二" ,  # billerinput 开票人

        )
    ]
    # 资产损坏赔付管理
    TestAssetsTestA21 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            "测试二" ,  # payername 输入赔付人姓名
            "54",  # payamt 输入付款金额

        )
    ]
    # 资产处置收益管理
    TestAssetsTestA22 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            "1" ,  # asetcntinput 点击资产数量
            "SERVMAT",  # dstnempinput 输入去向单位
            "500",  # amtinput 输入赔付金额

        )
    ]
    # 资产审批
    TestAssetsTestA23 = [
        (
            "SERVMAT" ,  # asetname 资产名称
            "SERVMAT" + x,  # appropnn 审批意见

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
    # 资产盘点结果审核
    TestAssetsTestA25 = [
        (
            "0924" ,  # asetname 资产名称
            "SERVMAT" + x,  # appropnn 审批意见

        )
    ]
    # 资产登记
    TestAssetsTestA32 = [
        (
            "SERVMAT"  ,  # asetName 资产名称
            "测试二" ,  # username 查询用户姓名
            "个",  # asetmtrunt 资产计量单位
            "SERVMAT",  # bradmol 点品牌型号
            "500",  # asetval 输入资产价值

        )
    ]
    # 资产处置备案
    TestAssetsTestA33 = [
        (
            "0924"  ,  # asetName 资产名称
            "测试二" ,  # rentname 租用/借用方名称
            "SERVMAT",  # lsrname 被租用/借用方名称
            "2020-09-29",  # usedtime 开始日期
            "2020-09-30",  # exprtime 结束日期

        )
    ]


if __name__ == '__main__':
    t = mhData
    z = t.znxxfw
    print(z)
    time.sleep(3)
    print(type(z))
