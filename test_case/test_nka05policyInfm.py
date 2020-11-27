# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------业务规范设置管理---------------
----------政策信息维护------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from selenium.webdriver.common.keys import Keys
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a05_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"政策信息维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("政策信息维护模块")   # 对应模块名称
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
class TestPolicyInformationMaintenance():

    @allure.story("政策信息维护模块新增")  # 对应用例标题
    @pytest.mark.parametrize(
        "polno, yeardata, indxdata, ttldata, reguldata, pfzdata, sbjwdata, regulcontdata",
        NkData.TestPolicyInformationMaintenance)
    @allure.title("打开政策信息维护模块")
    def test_PolicyInformationMaintenance(
            self, login, polno, yeardata, indxdata, ttldata, reguldata, pfzdata, sbjwdata, regulcontdata):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.move(level3menu, "政策信息维护模块")
            self.driver.click(level3menu, "政策信息维护模块")
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
            self.driver.switch_frame(iframe, "政策信息维护首页")
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "政策信息维护首页")
        with allure.step('输入信息'):
            # 输入政策法规编号
            self.driver.send_keys(pol_no, polno, "政策法规信息表")
            # 输入年份
            self.driver.send_keys(year, yeardata, "政策法规信息表")
            self.driver.send_keys(year, Keys.ENTER, "政策法规信息表")
            # 输入索引号
            self.driver.send_keys(indx, indxdata, "政策法规信息表")
            # # 输入发布日期
            # rls_date = (By.XPATH, '//label[@for="rlsDate"]/..//input')
            # self.driver.send_keys(rls_date, "2020-05-01", "政策法规信息表")
            # 输入标题
            self.driver.send_keys(ttl, ttldata, "政策法规信息表")
            # 输入政策法规来源
            self.driver.send_keys(regulations_sources, reguldata, "政策法规信息表")
            # 输入发文字号
            self.driver.send_keys(post_fonts_z, pfzdata, "政策法规信息表")
            # 输入主题词
            self.driver.send_keys(sbjwd, sbjwdata, "政策法规信息表")
            # 输入法规摘要
            self.driver.send_keys(regulations_cont, regulcontdata, "政策法规信息表")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "政策法规信息表")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "政策信息维护首页")
            assert "成功" in result
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "政策信息维护首页")
