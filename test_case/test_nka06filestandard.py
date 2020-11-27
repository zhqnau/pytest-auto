# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------业务规范设置管理---------------
----------档案规范维护------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a06_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"档案规范维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("档案规范维护模块")   # 对应模块名称
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
class TestArchivesStandardMaintenance():

    @allure.story("档案规范维护模块新增")  # 对应用例标题
    @pytest.mark.parametrize(
        "mattname, filename, filecnt, filedescribe", NkData.TestArchivesStandardMaintenance)
    @allure.title("打开档案规范维护模块")
    def test_ArchivesStandardMaintenance(self, login, mattname, filename, filecnt, filedescribe):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.move(level3menu, "档案规范维护模块")
            self.driver.click(level3menu, "档案规范维护模块")
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "档案规范维护首页")
        with allure.step('查询服务事项信息'):
            # 查询服务事项信息
            self.driver.send_keys(matt_name, mattname, "档案规范维护首页")
            self.driver.click(query_button, "档案规范维护首页")
        with allure.step('点击编辑'):
            # 点击编辑
            try:
                self.driver.click(information, "档案规范维护首页")
            except:
                self.driver.click(information1, "档案规范维护首页")
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "服务事项环节档案规范信息表")
            # 输入档案材料名称
            self.driver.send_keys(file_name, filename, "服务事项环节档案规范信息表")
            # 输入档案材料数量
            self.driver.send_keys(file_cnt, filecnt, "服务事项环节档案规范信息表")
            # 输入档案材料说明
            self.driver.send_keys(file_describe, filedescribe, "服务事项环节档案规范信息表")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "服务事项环节档案规范信息表")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "服务事项环节档案规范信息表")
            assert "成功" in result
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "档案规范维护首页")
