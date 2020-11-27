# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控功能模块管理---------------
----------受控模块登记------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.c01_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"受控模块登记,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("受控模块登记模块")   # 对应allure报告模块名称
@pytest.mark.nkgnmk(reruns=2, reruns_delay=2)
class TestControlledModuleRegistration():

    @allure.story("受控模块登记模块维护")  # 对应allure报告用例标题
    # pytest参数化数据信息
    @pytest.mark.parametrize(
        'mattnodename, menuname, warncont', NkData.TestControlledModuleRegistration)
    @allure.title("受控模块登记")  # 对应allure报告
    def test_ControlledModuleRegistration(self, login, mattnodename, menuname, warncont):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            self.driver.click(level1menu, "子系统菜单")
            if open1menu:
                self.driver.click(open1menu, "展开菜单")
            else:
                pass
            self.driver.move(level2menu, "内控功能模块管理")
            self.driver.click(level2menu, "内控功能模块管理")
            self.driver.move(level3menu, "内控功能模块管理")
            self.driver.click(level3menu, "受控模块登记模块")
        with allure.step('转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "受控模块登记模块首页")
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "受控模块登记模块首页")
        with allure.step('输入新增信息'):
            # 点击业务环节名称
            self.driver.click(servMattNodeName, "受控模块登记界面")
            # 查询业务环节名称
            self.driver.send_keys(matt_node_name, mattnodename, "服务事项环节选择界面")
            # 点击查询
            self.driver.click(query_button, "服务事项环节选择界面")
            # 点击选择
            try:
                self.driver.click(information1, "服务事项环节选择界面")
            except:
                self.driver.click(information, "服务事项环节选择界面")
            # 选择业务环节信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//button[@title="选择"]/i')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击菜单编码
            self.driver.click(menu_no, "受控模块登记界面")
            # 查询菜单信息
            self.driver.send_keys(menu_name, menuname, "菜单选择界面")
            self.driver.click(menu_query_button, "菜单选择界面")
            # 选择菜单信息
            try:
                self.driver.click(skmkinf, "菜单选择界面")
            except:
                self.driver.click(skmkinf1, "菜单选择界面")
            # 选择菜单信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//button[@title="选择"]/i')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击事前提醒
            self.driver.click(warn, "受控模块登记界面")
            # 选择是否提醒
            self.driver.click(warn_list, "受控模块登记界面")
            # 输入提醒内容
            self.driver.send_keys(warn_cont, warncont, "受控模块登记界面")
            # 点击事中记录
            self.driver.click(rcd, "受控模块登记界面")
            # 选择是否记录
            self.driver.click(rcd_list, "受控模块登记界面")
            # 选择规则信息
            try:
                self.driver.click(SERVMATinf, "受控模块登记界面")
            except:
                self.driver.click(SERVMATinf1, "受控模块登记界面")
            # 选择规则信息--软集
            # checkbox = self.driver.find_elements(By.XPATH, '//input[@type="checkbox"and@class="el-checkbox__inner"]')[0]
            # self.driver.execute_script("arguments[0].click();", checkbox)
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "受控模块登记界面")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result1 = self.driver.text(txt1, "受控模块登记模块首页")
            assert "成功" in result1
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "受控模块登记模块首页")
