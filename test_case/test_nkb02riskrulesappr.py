# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控规则管理流程---------------
----------内控风险规则审批----------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.b02_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"内控风险规则审批,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("内控风险规则审批模块")   # 对应模块名称
@pytest.mark.nkgzgl(reruns=2, reruns_delay=2)
class TestRiskRulesApproval():


    @allure.story("内控风险规则审批")  # 对应用例标题
    @pytest.mark.parametrize(
        "rulename, appopinion", NkData.TestRiskRulesApproval)
    @allure.title("打开内控风险规则审批模块")
    def test_RiskRulesApproval(self, login, rulename, appopinion):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "内控规则管理流程菜单")
            self.driver.move(level3menu, "内控风险规则审批模块")
            self.driver.click(level3menu, "内控风险规则审批模块")
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "内控风险规则审批首页")
        with allure.step('查询内控规则信息'):
            # 查询内控规则信息
            self.driver.send_keys(rule_name, rulename, '内控风险规则审批首页')
            self.driver.click(query_button, '内控风险规则审批首页')
        with allure.step('点击审批'):
            # 点击审批按钮
            try:
                self.driver.click(button, '内控风险规则审批首页')
            except:
                self.driver.click(button1, '内控风险规则审批首页')
            # 点击审批按钮--软集
            # button = self.driver.find_elements(By.XPATH, '//button[@type="button"and@title="审批"]')[0]
            # self.driver.execute_script("arguments[0].click();", button)
        with allure.step('填写审批结果'):
            # 点击审批结果
            self.driver.click(app_result, "审批界面")
            # 选择审批结果
            self.driver.click(app_result_list, "审批界面")
            # 输入审批意见
            self.driver.send_keys(app_opinion, appopinion, "审批界面")
        with allure.step('保存审批结果'):
            # 点击审批
            self.driver.click(approval_button, "审批界面")
        with allure.step('获取提示结果信息'):
            # 获取提示结果继续操作
            result1 = self.driver.text(txt1, '内控风险规则审批首页')
            assert "成功" in result1
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, '内控风险规则审批首页')
