# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控功能模块管理---------------
----------受控模块作废申请---------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.c03_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"受控模块作废申请,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("受控模块作废申请模块")   # 对应allure报告模块名称
@pytest.mark.nkgnmk(reruns=2, reruns_delay=2)
class TestControlledModuleInvalid():

    @allure.story("受控模块作废申请维护")  # 对应allure报告用例标题
    # pytest参数化数据信息
    @pytest.mark.parametrize(
        'menuname, applydesc', NkData.TestControlledModuleInvalid)
    @allure.title("受控模块作废申请")  # 对应allure报告
    def test_ControlledModuleInvalid(self, login, menuname, applydesc):
        driver = login
        self.driver = BasePage(driver)
        with allure.step('打开菜单'):
            # self.driver.click(level1menu, "子系统菜单")
            # if open1menu:
            #     self.driver.click(open1menu, "展开菜单")
            # else:
            #     pass
            # self.driver.move(level2menu, "内控功能模块管理")
            # self.driver.click(level2menu, "内控功能模块管理")
            self.driver.move(level3menu, "受控模块作废申请模块")
            self.driver.click(level3menu, "受控模块作废申请模块")
        with allure.step('转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "受控模块作废申请首页")
        with allure.step('查询信息'):
            # 查询子系统信息
            self.driver.send_keys(menu_name, menuname, "受控模块作废申请首页")
            self.driver.click(query_button, "受控模块作废申请首页")
        with allure.step('点击提交申请'):
            # 点击提交申请
            try:
                self.driver.click(information, "受控模块作废申请首页")
            except:
                self.driver.click(information1, "受控模块作废申请首页")
            # 点击提交申请--软集
            # submit = self.driver.find_elements(By.XPATH, '//button[@title="提交申请"]/i')[0]
            # self.driver.execute_script("arguments[0].click();", title)
        with allure.step('输入申请原因'):
            # 输入申请原因
            self.driver.send_keys(apply_describe, applydesc, "作废申请信息页")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "作废申请信息页")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result1 = self.driver.text(txt1, "受控模块作废申请首页")
            assert "成功" in result1
        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "受控模块作废申请首页")
