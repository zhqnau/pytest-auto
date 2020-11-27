# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控规则管理流程---------------
----------内控风险规则作废----------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.b03_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"内控风险规则审批,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("内控风险规则作废模块")   # 对应模块名称
@pytest.mark.nkgzgl(reruns=2, reruns_delay=2)
class TestRiskRulesInvalid():

    @allure.story("内控风险规则作废")  # 对应用例标题
    @pytest.mark.parametrize(
        "rulename, Invalidreason", NkData.TestRiskRulesInvalid)
    @allure.title("打开内控风险规则作废模块")
    def test_RiskRulesInvalid(self, login, rulename, Invalidreason):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "内控规则管理流程菜单")
            self.driver.move(level3menu, "内控风险规则作废模块")
            self.driver.click(level3menu, "内控风险规则作废模块")
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "内控风险规则作废首页")
        with allure.step('查询信息'):
            # 查询子系统信息
            self.driver.send_keys(rule_name, rulename, "内控风险规则作废首页")
            self.driver.click(query_button, "内控风险规则作废首页")
        with allure.step('点击作废'):
            # 点击作废按钮--自用
            try:
                self.driver.click(Invalid_button, "内控风险规则作废首页")
            except:
                self.driver.click(Invalid_button1, "内控风险规则作废首页")
            # 点击审批按钮--软集
            # Invalid_button = self.driver.find_elements(By.XPATH, '//button[@type="button"and@title="作废"]')[0]
            # self.driver.execute_script("arguments[0].click();", Invalid_button)
        with allure.step('输入作废原因'):
            # 输入作废原因
            self.driver.send_keys(Invalid_reason, Invalidreason, '作废界面')
        with allure.step('保存结果'):
            # 点击关闭
            self.driver.click(close_button, '作废界面')
        # with allure.step('获取提示结果继续操作'):
        #     # 获取提示结果继续操作
        #     result1 = self.driver.text(txt1, "内控风险规则作废首页")
        #     assert "成功" in result1
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "内控风险规则作废首页")