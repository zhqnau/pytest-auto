# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------业务规范设置管理---------------
----------业务环节经办规则维护------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a03_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"业务环节经办规则维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
@allure.feature("业务环节经办规则维护模块")
class TestEventRuleMaintenance():

    @allure.story("业务环节经办规则维护")  # 对应用例标题
    @pytest.mark.parametrize("mattname, chkrulename, chkrulenode", NkData.TestEventRuleMaintenance)
    @allure.title("业务环节经办规则维护模块新增")
    def test_EventRuleMaintenance(self, login, mattname, chkrulename, chkrulenode):
        driver = login
        self.driver = BasePage(driver)
        with allure.step("打开菜单"):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.move(level3menu, "业务环节经办规则维护模块")
            self.driver.click(level3menu, "业务环节经办规则维护模块")
        # 内控弹框点掉
        # try:
        #     js = 'document.querySelector' \
        #          '("body > div.el-dialog__wrapper > div > div.el-dialog__body > div.confirm-button").click();'
        #     self.driver.execute_script(js)
        #     self.logger.info('点击内控弹框')
        # except:
        #     self.logger.info('没有内控弹框')
        with allure.step("界面使用iframe，转换成iframe进行定位"):
            self.driver.switch_frame(iframe, "业务环节经办规则维护首页")
        with allure.step('查询并选择服务事项'):
            # 查询服务事项名称
            self.driver.send_keys(matt_name, mattname, "业务环节经办规则维护首页")
            self.driver.click(query_button, "业务环节经办规则维护首页")
            # 选择服务事项信息--自用
            try:
                self.driver.click(information, "业务环节经办规则维护首页")
            except:
                self.driver.click(information1, "业务环节经办规则维护首页")
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "业务环节经办规则维护首页")
        with allure.step('输入信息'):
            # 输入经办规则编号
            # self.driver.send_keys(chk_rule_id, chkruleid, "服务事项环节校验信息表")
            # 输入经办规则名称
            self.driver.send_keys(chk_rule_name, chkrulename, "服务事项环节校验信息表")
            # 输入经办规则说明
            self.driver.send_keys(chk_rule_node, chkrulenode, "服务事项环节校验信息表")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "服务事项环节校验信息表")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "业务环节经办规则维护首页")
            assert "成功" in result
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "业务环节经办规则维护首页")


if __name__ == '__main__':
    @pytest.fixture(scope="session")
    def test_a(login):
        driver = login
        driver = BasePage(driver)
        driver.click(level1menu, "子系统菜单")
        if open1menu:
            driver.click(open1menu, "展开菜单")
        else:
            pass
        driver.click(level2menu, "业务规范设置管理菜单")