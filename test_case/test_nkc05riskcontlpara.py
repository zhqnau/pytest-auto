# -*-coding:utf-8-*-
"""
----------内部控制子系统------------------
----------内控功能模块管理---------------
----------内控参数设置------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.c05_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"内控参数设置,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("内控参数设置模块")   # 对应allure报告模块名称
@pytest.mark.nkgnmk(reruns=2, reruns_delay=2)
class TestRiskControlParameters():

    @allure.story("内控参数设置维护")  # 对应allure报告用例标题
    # pytest参数化数据信息
    @pytest.mark.parametrize(
        'rulename, paracode, paraname, paraval, paradesc', NkData.TestRiskControlParameters)
    @allure.title("内控参数设置")  # 对应allure报告
    def test_RiskControlParameters(self, login, rulename, paracode, paraname, paraval, paradesc ):
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
            self.driver.move(level3menu, "受控模块审批模块")
            self.driver.click(level3menu, "受控模块审批模块")
        with allure.step('内控弹框点掉'):
            # 内控弹框点掉
            try:
                js = (By.XPATH,
                      '//div[@id="app"]/following-sibling::div[@class="el-dialog__wrapper"]//*[text()="我已阅读并知晓"]')
                self.driver.execute_script(js, "内控参数设置首页")
            except:
                pass
        with allure.step('转换成iframe进行定位'):
            # 界面使用iframe，转换成iframe进行定位
            self.driver.switch_frame(iframe, "内控参数设置首页")

        with allure.step('内控弹框点掉'):
            # 查询受内控规则
            self.driver.send_keys(rule_name, rulename, "内控参数设置首页")
            self.driver.click(query_button, "内控参数设置首页")
        with allure.step('点击维护'):
            # 点击维护--自用
            try:
                self.driver.click(information, "内控参数设置首页")
            except:
                self.driver.click(information1, "内控参数设置首页")
            # 点击维护--软集
            # maintenance = self.driver.find_elements(By.XPATH, '//button[@title="维护"]/i')[0]
            # self.driver.execute_script("arguments[0].click();", maintenance)
        with allure.step('点击新增'):
            # 点击新增
            self.driver.click(add_button, "规则参数信息页")
        with allure.step('内控弹框点掉'):
            # 输入参数编码
            self.driver.send_keys(para_code, paracode, '参数信息')
            # 输入参数名称
            self.driver.send_keys(para_name, paraname, '参数信息')
            # 点击参数类型
            self.driver.click(para_type, '参数信息')
            # 选择参数类型
            self.driver.click(para_type_list, '参数信息')
            # 输入参数值
            self.driver.send_keys(para_val, paraval, '参数信息')
            # 输入参数描述
            self.driver.send_keys(para_desc, paradesc, '参数信息')
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, '参数信息')
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result1 = self.driver.text(txt1, "规则参数信息页")
            assert "成功" in result1
        with allure.step('内控弹框点掉'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "内控参数设置首页")
