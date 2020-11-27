# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------业务规范设置管理---------------
----------不相容角色维护----------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a07_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"不相容角色维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("不相容角色维护模块")   # 对应模块名称
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
class TestIncompatibleRoleMaintenance():

    @allure.story("不相容角色维护模块新增")  # 对应用例标题
    @pytest.mark.parametrize(
        "rolename, businname, busin2name, roledesc", NkData.TestIncompatibleRoleMaintenance)
    @allure.title("打开不相容角色维护模块")
    def test_IncompatibleRoleMaintenance(self, login, rolename, businname, busin2name, roledesc):
        driver = login
        self.driver = BasePage(driver)
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.move(level3menu, "不相容角色维护模块")
            self.driver.click(level3menu, "不相容角色维护模块")
        with allure.step('转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, '不相容角色维护首页')
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, '不相容角色维护首页')
        with allure.step('输入信息'):
            # 输入互斥角色规范名称
            self.driver.send_keys(role_name, rolename, "互斥规范页面")
            # 点击角色1编号
            self.driver.click(role1_no)
            # 查询业务角色名称
            self.driver.send_keys(business_role_name, businname, '业务角色信息界面')
            self.driver.click(quer_button, "业务角色信息界面")
            # 选择业务角色信息
            try:
                self.driver.click(informatio, "业务角色信息界面")
            except:
                self.driver.click(informatio1, "业务角色信息界面")
            # 选择信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//input[@type="radio"and@class="el-radio__original"]')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击确定
            self.driver.click(confirm_button_1, "业务角色信息界面")
            # 点击角色2编号
            self.driver.click(role2_no, "互斥规范页面")
            # 查询业务角色2名称
            self.driver.send_keys(business_role2_name, busin2name, "业务角色信息界面")
            self.driver.click(query_button, "业务角色信息界面")
            # 选择业务角色信息
            try:
                self.driver.click(information, "业务角色信息界面")
            except:
                self.driver.click(information1, "业务角色信息界面")
            # 选择信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//input[@type="radio"and@class="el-radio__original"]')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
            # 点击确定
            self.driver.click(confirm_button, "业务角色信息界面")
            # 输入互斥原因
            self.driver.send_keys(role_describe, roledesc, "互斥规范页面")
            # 点击保存
            self.driver.click(save_button, "互斥规范页面")
            # 获取提示结果继续操作
            result = self.driver.text(txt, '不相容角色维护首页')
            assert "成功" in result
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, '不相容角色维护首页')
