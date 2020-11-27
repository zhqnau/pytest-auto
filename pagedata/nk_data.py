from utils.timenum import ts
import time
'''
测试数据，每个页面需要多少个数据就在该页面维护多少个数据，数据顺序固定
'''

class NkData(object):

    # 获取时间戳作为数据编号，防止数据唯一性导致运行出错
    x = str(ts)

    # 服务事项维护模块数据

    TestServiceMaintenance = [
        (
            "SERVMAT" + x,  # 输入服务事项编号
            "SERVMAT" + x,  # 输入服务事项名称
            "内部控制",  # 输入子系统名称
            "1",  # 输入经办时限
            "服务事项说明"  # 输入服务事项说明
        )
    ]
    # 服务事项环节数据信息
    TestEventMaintenance = [
        (
            "SERVMAT" + x,  # 查询服务事项名称
            "SERVMAT" + x,  # 输入服务事项环节编号
            "SERVMAT" + x,  # 输入服务事项环节名称
            "1",  # 点击经办时限
            "1",  # 输入每月要求处理疑点数量
            "1",  # 输入每月要求处理任务数量
            "服务事项环节说明"  # 输入服务事项环节说明
        )
    ]
    # 业务环节经办规则维护数据信息
    TestEventRuleMaintenance = [
        (
            "SERVMAT" + x,  # 查询服务事项名称
            # "SERVMAT" + x,  # 输入经办规则编号
            "SERVMAT" + x,  # 输入经办规则名称
            "经办规则说明",  # 输入经办规则说明
        )
    ]
    # 事件事项维护数据信息
    TestItemEventMaintenance = [

        (
            "SERVMAT" + x,  # 查询服务事项信息
            "SERVMAT" + x,  # 输入事件编号
            "SERVMAT" + x,  # 输入事件名称
            "事件描述",  # 输入事件描述
        )
    ]
    #　政策信息维护数据信息
    TestPolicyInformationMaintenance = [
        (
            "POLREGL" + x,  # 输入政策法规编号
            "2020",  # 输入年份
            "POLREGL" + x,  # 输入索引号
            "关于扩大长期护理保险制度试点的指导意见" + x,  # 输入标题
            "国家医保局",  # 输入政策法规来源
            "医保发〔2020〕37号" + x,  # 输入发文字号
            "制度试点" + x,  # 输入主题词
            "POLREGL" + x,  # 输入法规摘要
        )
    ]
    # 档案规范维护数据信息
    TestArchivesStandardMaintenance = [
        (
            "SERVMAT" + x,  # 查询服务事项信息
            "档案材料名称" + x,  # 输入档案材料名称
            2,  # 输入档案材料数量
            "档案材料说明",  # 输入档案材料说明
        )
    ]
    # 不相容角色维护数据信息
    TestIncompatibleRoleMaintenance = [
        (
            "互斥角色" + x,  # 输入互斥角色规范名称
            "内控业务整改人",  # 查询业务角色1名称
            "内控负责人",  # 查询业务角色2名称
            "业务角色和审批角色互斥",  # 输入互斥原因
        )
    ]
    # 内控风险规则登记
    TestRiskControlRules = [
        (
            "SERVMAT",
            "SERVMAT",
            "SERVMAT" + x,
            "SERVMAT" + x,
            "内控规则描述",
            "内控规则描述提示信息",
            "SERVMAT" ,
        )
    ]
    # 内控风险规则审批
    TestRiskRulesApproval = [
        (
            "SERVMAT" ,
            "SERVMAT" + x,
        )
    ]
    # 内控风险规则作废
    TestRiskRulesInvalid = [
        (
            "SERVMAT" ,
            "SERVMAT" + x,
        )
    ]
    # 受控模块登记
    TestControlledModuleRegistration = [
        (
            "SERVMAT" ,
            "内控参数设置",
            "内控参数设置" + x,
        )
    ]
    # 受控模块生效申请
    TestControlledModuleEffective = [
        (
            "内控" ,
            "内控参数设置生效申请" + x,
        )
    ]
    # 受控模块作废申请
    TestControlledModuleInvalid = [
        (
            "内控" ,
            "内控参数设置生效申请" + x,
        )
    ]
    # 受控模块审批
    TestControlledModuleApproval = [
        (
            "内控" ,
            "同意内控参数设置生效申请" + x,
        )
    ]
    # 内控参数设置
    TestRiskControlParameters = [
        (
            "SERVMAT" ,
            x,
            "内控参数",
            x,
            "内控参数" + x,
        )
    ]
    # 内控采集范围设置数据
    TestAcquisitionRange = [
        (
            "SERVMAT" ,
            """SELECT count(*) AS count_num FROM ( SELECT *, count(*) AS num FROM sys_pwd_chg_evt_c b 
            WHERE opt_time > timestampadd( DAY, - 2, now()) GROUP BY UACT ) a 
            WHERE num >= 2;""",

        )
    ]

    TestAcquisitionRangeModification = [
        (
            "SERVMAT" ,
            "我是一个备注",

        )
    ]

    TestCollectionSampling = [
        (
            "SERVMAT" ,
            "1",
            "50",
        )
    ]
    # 内控统计任务登记
    TestStatisticsTaskRegistration = [
        (
            "SERVMAT" + x ,  # 统计任务名称
            "SERVMAT",  # 服务事项信息
            "SERVMAT",  # 服务事项环节
            "SERVMAT" + x,  # 统计任务
        )
    ]
    # 内控统计任务审批
    TestStatisticalTaskApproval = [
        (
            "SERVMAT"  ,  # 内控统计任务
            "SERVMAT",  # 审批意见
        )
    ]
    # 内控统计任务作废
    TestStatisticalTaskInvalid = [
        (
            "SERVMAT"  ,  # 内控统计任务
        )
    ]
    # 内控规则模版设置
    TestRuleTemplateSetting = [
        (
            "SERVMAT"  ,  # 内控规则信息
            """SELECT OPTINS_NO AS BIZ_OPTINS, OPTER_ID AS BIZ_OPTER_ID, OPTER_NAME AS BIZ_OPTER_NAME, 
                OPT_TIME AS BIZ_OPT_TIME, '110000' AS BIZ_POOLAREA,OPTER_ID AS INSU_PSN_NO,NULL AS INSU_EMP_NO,
                NULL AS EMP_NAME,NULL AS EMP_TYPE,NULL AS EMP_ABBR,OPTER_NAME AS INSU_NAME,NULL AS GEND,NULL AS BRDY,
                OPTER_ID AS CERTNO,ADMDVS,UACT AS STR_COND_1,
                ( SELECT UACT_ID FROM SYS_UACT_D WHERE sys_pwd_chg_evt_c.UACT = SYS_UACT_D.UACT ) AS STR_COND_2,
                '202006301453390000059100000000' AS STR_COND_3 
                FROM ( SELECT *, count( * ) AS num FROM sys_pwd_chg_evt_c WHERE opt_time > timestampadd( DAY, - 2, now()) 
                GROUP BY UACT ) sys_pwd_chg_evt_c WHERE num >= 2;
            """,  # 条件模型
            "SERVMAT" + x,  # 备注信息
        )
    ]
    TestDisplayThemeSettings = [
        (
            "SERVMAT" + x,  # 主题名称
            "SERVMAT" + x,  # 主题描述
            """SELECT a.uact_id AS strCond1, a.uact as 帐号, a.user_id as 用户ID, b.uact_name as 用户名,
                 a.crte_time as 创建时间 FROM (SELECT UACT_id AS uact_id, uact as uact, crte_time as crte_time,
                 USER_ID AS USER_ID FROM SYS_UACT_D ) a LEFT JOIN (SELECT USER_ID AS USER_ID, uact_name AS uact_name
                 FROM sys_user_d ) b ON a.user_id = b.user_id"""  # 展现配置
        )
    ]
    # 内控展现设置
    TestControlDisplaySetting = [
        (
            "SERVMAT"  ,  # mattnodename 内控统计任务
        )
    ]
    # 采集执行结果查询
    TestExecuteResultQuery = [
        (
            "SERVMAT"  ,  # 统计任务信息
        )
    ]
    # 内控采集时限设置
    TestCollectionTimeSetting = [
        (
            "SERVMAT"  ,  # 业务环节信息
            "3",  # 预警时限（天）
            "5",  # 截止时限（天）
        )
    ]
    # 内控采集时限修改
    TestCollectionTimeModify = [
        (
            "SERVMAT",  # 业务环节信息
            "2",  # 预警时限（天）
            "5",  # 截止时限（天）
        )
    ]
    # 内控风险询问
    TestControlRiskInquiry= [
        (
            "SERVMAT",  # 服务事项名称
            "develop",  # 用户帐号
            "SERVMAT" + x,  # 询问内容
        )
    ]
    # 内控风险询问回复
    TestControlRiskAsk = [
        (
            "密码",  # 服务事项名称
            # "develop",  # 用户帐号
            "SERVMAT" + x,  # 询问内容
        )
    ]
    # 内控风险询问回复
    TestManualRiskAdditional = [
        (
            "SERVMAT",  # 服务事项编号 mattno
            "SERVMAT",  # 环节编号 nodeno
            "SERVMAT",  # 内控规则编号 rulecode
            x,  # 个人编号 psnno
            "测试",  # 姓名  insname
            "21122420" + x,  # 身份证号 certno
            x,  # 单位编号 insemp
            "密码" + x ,  # 单位名称 empname
            "测试二",  # 业务经办人 username
            "2020-09-01",  # 业务经办时间 biztime
            "密码" + x ,  # 疑点说明 describetxt
            "SERVMAT",  # sermattname
        )
    ]
   # 内控风险询问回复
    TestControlRiskSuspended = [
        (
            "密码",  # 服务事项名称
            # "develop",  # 用户帐号
            "SERVMAT" + x,  # 输入意见
        )
    ]
    # 内控风险询问回复
    TestControlRemindFeedback = [
        (
            "密码",  # 服务事项名称
            # "develop",  # 用户帐号
            "SERVMAT" + x,  # 输入意见
        )
    ]
    # 内控任务生成
    TestControlTaskGeneration = [
        (
            "2020-09",  # 考核月份 monthdata
            "SERVMAT",  # 服务事项名称 mattname
            "SERVMAT" + x,  # 疑点确认说明 prbdescribe
            "SERVMAT" + x,  # 检查任务名称 bizname
            "SERVMAT" + x,  # 内控任务目标 taskobjective
        )
    ]
    # 内控任务分派
    TestTaskAssignment = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            "develop",  # 经办人员信息 useraccount
            "SERVMAT" + x,  # 输入整改要求 memotxt
        )
    ]
    # 内控任务分派审批
    TestAssignmentApproval = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            "develop" + x,  # 输入审批意见 appopinion
        )
    ]
    # 内控佐证材料录入
    TestControlSupportMaterial = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            "develop" + x,  # 佐证材料名称 docname
            "develop" + x,  # 佐证材料描述 docdescribe
        )
    ]
    # 内控整改录入
    TestRectificationResult = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            "2020-10-01",  # 整改时间 rectificationtime
            "SERVMAT" + x,  # 输入整改详情 rectificationdetail
        )
    ]
    # 内控任务结果录入
    TestTaskResult = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            # "2020-10-01",  # 整改时间 rectificationtime
            "SERVMAT" + x,  # 输入整改确认意见 opiniondata
        )
    ]
    # 内控任务结果审批
    TestTaskResultApproval = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            # "2020-10-01",  # 整改时间 rectificationtime
            "SERVMAT" + x,  # 输入审批意见 approvalopinion
        )
    ]
    # 内控任务结果审批
    TestControlTaskAuthorization = [
        (
            "SERVMAT",  # 查询服务事项名称 mattname
            "develop",  # 查询经办人员 useraccount
            "SERVMAT" + x,  # 输入整改要求 memodata
            "develop" ,  # 用户帐号 accountid

        )
    ]
    # 风险上报
    TestRiskInformationReport = [
        (
            "SERVMAT" + x,  # 风险上报标题 reporttitle
            "develop",  # textarea文本框输入 reportcontent
            "SERVMAT" + x,  # 风险上报标题 riskreporttitle

        )
    ]
    # 风险信息上报审批
    TestRiskInformationReportApproval = [
        (
            "SERVMAT" ,  # 风险上报标题 reporttitle
            "SERVMAT" + x,  # 风险上报标题 apprOpnncontent

        )
    ]
    # 风险信息上报查询
    TestRiskInformationReportQuery = [
        (
            "SERVMAT" ,  # 风险上报标题 reporttitle
            # "SERVMAT" + x,  # 风险上报标题 apprOpnncontent

        )
    ]
    # 风险信息发布
    TestRiskInformationRelease = [
        (
            "SERVMAT",  # 风险上报标题查询 reporttitle
            "SERVMAT" + x,  # 风险发布标题 risktitle
            "SERVMAT" + x,  # 风险发布内容 reportcontent

        )
    ]
    # 风险信息发布审批
    TestRiskInformationReleaseApproval = [
        (
            "SERVMAT" ,  # 风险上报标题 reporttitle
            "SERVMAT" + x,  # 风险上报标题 apprOpnncontent

        )
    ]
    # 风险信息发布查询
    TestRiskInformationReleaseQuery = [
        (
            "SERVMAT" ,  # 风险发布标题 risktitle
            # "SERVMAT" + x,  # 风险上报标题 apprOpnncontent

        )
    ]
    # 内控指标上报
    TestControlIndexReport = [
        (
            "SERVMAT" + x,  # 指标描述上报标题 kpiRpupTtlsj
            "SERVMAT" + x,  # 指标描述上报内容 kpiRpupContsj
            "2020-08",  # 业务年月 timekssj
            "2020-09",  # 业务年月 timejssj
            "2020-08",  # 业务年月 timekstext
            "2020-09",  # 业务年月 timejstext
        )
    ]
    # 内控指标查询
    TestIndexReportQuery = [
        (
            "2020-08",  # 业务年月 timekstext
            "2020-09",  # 业务年月 timejstext
        )
    ]
    # 内控风险规则上报
    TestRiskReportRules = [
        (
            "SERVMAT",  # 内控风险规则 rulename
            "SERVMAT",  # 服务事项名称 mattname
        )
    ]
    # 内控风险规则上报审批
    TestRiskReportRulesApproval = [
        (
            "SERVMAT",  # 内控风险规则 mattname
            "SERVMAT",  # 服务事项名称 apprOpnnxx
        )
    ]
    # 内控风险规则上报审批
    TestControlRiskReportRulesQuery = [
        (
            "SERVMAT",  # 内控风险规则 mattname
            # "SERVMAT",  # 服务事项名称 apprOpnnxx
        )
    ]
    # 内控指标上报
    TestControlTaskResultReport = [
        (
            "SERVMAT" + x,  # 指标描述上报标题 taskRsltRpupTtlsj
            "SERVMAT" + x,  # 指标描述上报内容 taskRsltRpupContsj
            "2020-08",  # 业务年月 timekssj
            "2020-09",  # 业务年月 timejssj
            "2020-08",  # 业务年月 timekstext
            "2020-09",  # 业务年月 timejstext
        )
    ]
    # 内控指标查询
    TestControlTaskResultReportQuery = [
        (
            "2020-08",  # 业务年月 timekstext
            "2020-09",  # 业务年月 timejstext
        )
    ]

    testcs_1 = [
        1,
        2,
    ]

if __name__ == '__main__':
    t = NkData
    z = t.TestEventMaintenance
    print(z)
    time.sleep(3)
    print(z)
