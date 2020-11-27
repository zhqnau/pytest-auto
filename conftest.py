import os
import allure
import pytest
from selenium import webdriver
from pageobject.loginpage import LoginPage
from utils.readconfig import ini


_driver = None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# request 内置的fixture


@pytest.fixture(scope="session", autouse=True)
def driver():
    global _driver
    if _driver is None:
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # _driver = webdriver.Chrome(options=chrome_options)
        _driver = webdriver.Chrome()
    _driver.maximize_window()  # 最大化
    yield _driver
    # print("1111111111")
    _driver.quit()








@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login(ini.username, ini.password, ini.verificationCode)
    return driver


