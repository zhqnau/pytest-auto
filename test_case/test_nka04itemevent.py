# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------业务规范设置管理---------------
----------事项事件维护------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a04_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@pytest.mark.skip
@allure.description(f"事项事件维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("事项事件维护模块")   # 对应模块名称
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
class TestItemEventMaintenance():

    @allure.story("事项事件维护模块新增")  # 对应用例标题
    @pytest.mark.parametrize("mattname, evtno, evtname, evtdescribe", NkData.TestItemEventMaintenance)
    @allure.title("打开事项事件维护模块")
    def test_ItemEventMaintenance(self, login, mattname, evtno, evtname, evtdescribe):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            self.driver.click(level1menu, "子系统菜单")
            if open1menu:
                self.driver.click(open1menu, "展开菜单")
            else:
                pass
            self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.move(level3menu, "事项事件维护模块")
            self.driver.click(level3menu, "事项事件维护模块")
        # with allure.step('内控弹框点掉'):
            # 内控弹框点掉
            # try:
            #     js = 'document.querySelector' \
            #          '("body > div.el-dialog__wrapper > div > div.el-dialog__body > div.confirm-button").click();'
            #     self.driver.execute_script(js)
            #     self.logger.info('点击内控弹框')
            # except:
            #     self.logger.info('没有内控弹框')
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "事项事件维护首页")
        with allure.step('查询并选择服务事项'):
            # 查询服务事项信息
            self.driver.send_keys(matt_name, mattname, '事项事件维护首页')
            self.driver.click(query_button, '事项事件维护首页')
            # 选择查询服务事项信息
            try:
                self.driver.click(information, '事项事件维护首页')
            except:
                self.driver.click(information1, '事项事件维护首页')
            # 选择查询服务事项信息--软集
            # radio = self.driver.find_elements(By.XPATH, '//input[@type="radio"and@class="el-radio__original"]')[0]
            # self.driver.execute_script("arguments[0].click();", radio)
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, '事项事件维护首页')
        with allure.step('输入信息'):
            # 输入事件编号
            self.driver.send_keys(evt_no, evtno, "服务事项事件信息表")
            # 输入事件名称
            self.driver.send_keys(evt_name, evtname, "服务事项事件信息表")
            # 输入事件描述
            self.driver.send_keys(evt_describe, evtdescribe, "服务事项事件信息表")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "服务事项事件信息表")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "事项事件维护首页")
            assert "成功" in result
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "事项事件维护首页")
