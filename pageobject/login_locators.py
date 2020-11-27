from selenium.webdriver.common.by import By
'''
登录首页定位元素
'''

class LoginLocators(object):
    """登录首页定位元素"""
    tab_pas = (By.ID, 'tab-password')    # 账号登录tab（医保局首页有用户登录，扫码登录，ca登录三个tab）
    input_username = (By.NAME, 'username')  # 用户名输入框 定位元素
    input_password = (By.NAME, 'password')  # 密码输入框 定位元素
    input_verificationCode = (By.NAME, 'verificationCode')  # 验证码输入框 定位元素
    click_submit = (By.XPATH, '//button[contains(@class,el-button)]/span[contains(text(),"登 录")]')  # 登录按钮 定位元素
    type_loginPass = (By.XPATH, '//span[contains(text(),"首页")]')  # 登陆成功后首页页面首页字样title 定位元素

