# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控规则管理流程---------------
----------内控风险规则登记----------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.b01_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"内控风险规则登记,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("内控风险规则登记模块")   # 对应模块名称
@pytest.mark.nkgzgl(reruns=2, reruns_delay=2)
class TestRiskControlRules():

    @allure.story("内控风险规则登记模块新增")  # 对应用例标题
    @pytest.mark.parametrize(
        "mattname, mattnodename, rulecode, rulename, ctrlruledesc, msgContdesc, sermattname", NkData.TestRiskControlRules)
    @allure.title("打开内控风险规则登记模块")
    def test_RiskControlRules(
            self, login, mattname, mattnodename, rulecode, rulename, ctrlruledesc,msgContdesc, sermattname):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            self.driver.click(level1menu, "子系统菜单")
            if open1menu:
                self.driver.click(open1menu, "展开菜单")
            else:
                pass
            self.driver.click(level2menu, "内控规则管理流程菜单")
            self.driver.click(level3menu, "内控风险规则登记模块")
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "内控风险规则登记首页")
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "内控风险规则登记首页")
        with allure.step('输入信息'):
            # 点击服务事项编号
            self.driver.click(matt_no, "维护信息界面")
            # 查询服务事项信息
            self.driver.send_keys(matt_name, mattname, '服务事项信息界面')
            self.driver.click(risk_querybutton, '服务事项信息界面')
            # 选择服务事项信息
            try:
                self.driver.click(risk_information, '服务事项信息界面')
            except:
                self.driver.click(risk_information1, '服务事项信息界面')
            # 选择信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//input[@type="radio"and@class="el-radio__original"]')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击确定
            self.driver.click(confirm_button, '服务事项信息界面')
            # 点击业务环节编号
            self.driver.click(matt_node_no, "维护信息界面")
            # 查询子系统信息
            self.driver.send_keys(matt_node_name, mattnodename, '服务事项环节信息界面')
            self.driver.click(query_button, '服务事项环节信息界面')
            # 选择服务事项环节信息
            try:
                self.driver.click(information, '服务事项环节信息界面')
            except:
                self.driver.click(information1, '服务事项环节信息界面')
            # 选择服务事项环节信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//input[@type="radio"and@class="el-radio__original"]')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击确定
            self.driver.click(confirm_button1, '服务事项环节信息界面')
            # 输入内控规则编号
            self.driver.send_keys(rule_code, rulecode, "维护信息界面")
            # 输入内控规则名称
            self.driver.send_keys(rule_name, rulename, "维护信息界面")
            # 点击内控程度
            self.driver.click(ctrl_degree, "维护信息界面")
            # 选择内控程度
            self.driver.click(ctrl_degree_list, "维护信息界面")
            # 点击规则类别
            self.driver.click(ctrl_rule_type, "维护信息界面")
            # 选择规则类别
            self.driver.click(ctrl_rule_type_list, "维护信息界面")
            # 输入内控规则描述
            self.driver.send_keys(ctrl_rule_describe, ctrlruledesc, "维护信息界面")
            # 输入消息内容
            self.driver.send_keys(msgCont, msgContdesc, "维护信息界面")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "维护信息界面")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "内控风险规则登记首页")
            assert "成功" in result
            # time.sleep(3)
        with allure.step('首页界面查询框点击查询'):
            # 首页界面查询框点击查询
            self.driver.send_keys(ser_matt_name, sermattname, "内控风险规则登记首页")
            self.driver.click(query_button1, "内控风险规则登记首页")
        with allure.step('点击提交'):
            # 点击提交
            try:
                self.driver.click(submit, "内控风险规则登记首页")
            except:
                self.driver.click(submit1, "内控风险规则登记首页")
            # 点击提交
            # submit = self.driver.find_elements(By.XPATH, '//button[@type="button"and@title="提交"]')[0]
            # self.driver.execute_script("arguments[0].click();", submit)
            # 点击确定
            self.driver.click(confirm_button2, "内控风险规则登记首页")
            # 获取提示结果继续操作
            result1 = self.driver.text(txt1, "内控风险规则登记首页")
            assert "成功" in result1
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "内控风险规则登记首页")
