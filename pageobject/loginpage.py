import time
import allure
from pageobject.basepage import BasePage
from utils.readconfig import ini
from pageobject.login_locators import LoginLocators as loc
'''
登录功能程序



'''


class LoginPage(BasePage):

    @allure.step("登录")  # allure报告固定用法 allure装饰器
    def login(self, username, password,
              verificationCode
              ):  # 括号内三个参数为用户名密码验证码，没有验证码就注掉
        """"""
        doc = "登录界面-登录功能"  # 记录日志固定用发

        self.driver.get(ini.url)  # 调用浏览器打开测试地址
        self.wait_element_visible(loc.input_username, doc=doc)  # 等待加载完成
        self.click(loc.tab_pas, doc=doc)  # 点击账号登录tab
        self.send_keys(loc.input_username, username, doc=doc)  # 输入用户名
        self.send_keys(loc.input_password, password, doc=doc)  # 输入密码
        # time.sleep(10)
        self.send_keys(loc.input_verificationCode, verificationCode, doc=doc)  # 输入验证码，不用就注掉
        self.click(loc.click_submit, doc=doc)  # 点击登录

    @allure.step("登录结果判断")
    def is_login_success(self):
        """判断是否登录成功 True  False"""
        doc = "登录界面-登录功能"

        result = self.is_element_exist(loc.type_loginPass, doc=doc)  # 获取登录成功后首页title判断是否登录成功
        return result


