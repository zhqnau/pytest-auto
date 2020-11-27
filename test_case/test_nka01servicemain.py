# -*-coding:utf-8-*-
"""
----------内部控制子系统--------------------
----------业务规范设置管理-----------------
----------服务事项维护--------------------
"""
import pytest  # @pytest.mark修饰器需引用pytest
from pageobject.basepage import BasePage  # 脚本需要用到BasePage类中的自定义方法，可左ctrl+鼠标左键点击查看
from pagelocator.a01_locator import *  # 引用此脚本对应的xpath定位信息
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息
import allure  # @allure修饰器 ，allure报告引用需要
from utils.timenum import nt


@allure.description(f"服务事项维护,本次执行时间为：{nt}")  # 对应allure报告描述信息
@allure.feature("服务事项维护模块")   # 对应allure报告模块名称
@pytest.mark.nkywgf(reruns=2, reruns_delay=2)
class TestServiceMaintenance:

    @allure.story("服务事项维护")  # 对应allure报告用例标题
    # pytest参数化数据信息，前5个是模块需要的数据，NkData.TestServiceMaintenance是取NkData.py文件中的TestServiceMaintenance
    @pytest.mark.parametrize(
        'sermattno, sermattname, subsystemname, opttimelmt, sermattdesc', NkData.TestServiceMaintenance)
    @allure.title("服务事项维护新增")  # 对应allure报告title
    # login是传递登录信息，后边的是@pytest.mark.parametrize的参数数据信息
    def test_servicemaintenance(self, login, sermattno, sermattname, subsystemname, opttimelmt, sermattdesc):
        driver = login  # 将登陆后获取的driver传递出来
        self.driver = BasePage(driver)  # 脚本需要用到 basepage.py中BasePage类的方法，
        # 故把带有登录信息的driver传递给BasePage在赋值给self.driver
        with allure.step('打开菜单'):  # 对应allure报告中测试步骤，固定写法
            self.driver.click(level1menu, "子系统菜单")
            # 点击菜单self.driver为上述引用固定写法，click为BasePage中方法，括号内为click方法中固定写法
            if open1menu:  # 如果医保局项目菜单未展开则点击展开
                self.driver.click(open1menu, "展开菜单")
            else:
                pass
            self.driver.click(level2menu, "业务规范设置管理菜单")
            self.driver.click(level3menu, "服务事项维护模块")
        with allure.step('界面使用iframe，转换成iframe进行定位'):
            self.driver.switch_frame(iframe, "服务事项维护首页")
        with allure.step('点击新增'):
            self.driver.click(add_button, "服务事项维护首页")
        with allure.step('输入信息'):
            # 输入服务事项编号
            self.driver.send_keys(ser_matt_no, sermattno , "服务事项信息界面页")
            # 输入服务事项名称
            self.driver.send_keys(ser_matt_name, sermattname , "服务事项信息界面页")
            # 点击子系统编号
            self.driver.click(sub_sys_id, "服务事项信息界面页")
            # 子系统信息界面，输入子系统名称
            self.driver.send_keys(sub_system_name, subsystemname, "子系统信息界面页")
            # 点击查询
            self.driver.click(query_button, "子系统信息界面页")
            # 选择信息
            try:
                self.driver.click(information,  "子系统信息界面页")
            except:
                self.driver.click(information1,  "子系统信息界面页")
            # 点击确认
            self.driver.click(confirm_button, "子系统信息界面页")
            # 输入经办时限
            self.driver.send_keys(opt_time_lmt, opttimelmt, "服务事项信息界面页")
            # 输入服务事项说明
            self.driver.send_keys(ser_matt_desc, sermattdesc, "服务事项信息界面页")
        with allure.step('点击保存'):
            # 点击保存
            self.driver.click(save_button, "服务事项信息界面页")
        with allure.step('获取提示结果继续操作'):
            # 获取提示结果继续操作
            result = self.driver.text(txt, "服务事项维护首页")
            assert "成功" in result

        with allure.step('关闭模块'):
            # 关闭模块
            self.driver.switch_back()
            self.driver.click(close, "服务事项维护首页")
