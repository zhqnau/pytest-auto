import datetime
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from utils.dir_config import *
import time
import win32con
import win32gui


class BasePage(object):
    """
    二次封装
    1、封装基本函数--执行日志、异常处理、失败截图
    2、所有页面的公共部分
    """
    def __init__(self, browser):
        self.driver = browser
        self.logger = Logger.get_logger()
        self.timeout = 20
        self.wait = WD(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        # self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.logger.info("打开网页：%s" % url)
            return self.driver
        except TE:
            raise TE("打开%s超时请检查网络或网址服务器" % url)

    def screenshot(self):
        """
        截图并保存在Screenshot文件夹下
        :param img_doc: 截图说明
        :return:
        """
        ts = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        screenshot_dir1 = os.path.normpath(screenshot_dir)
        screen_name1 = ts + '.png'
        screen_name = os.path.join(screenshot_dir1, screen_name1)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.logger.info('已截图保存，截图保存在:{}'.format(screenshot_dir1))
        except Exception as e:
            self.logger.error('截图发生异常: %s' % e)

    def wait_element_visible(self, locator, times=30, poll_frequency=0.5, doc=""):
        """
        等待元素
        :param locator: 元素定位（元祖形式：元素定位类型、元素定位方式）
        :param times: 等待时间30s
        :param poll_frequency: 等待周期
        :param doc: 模块名——页面名——操作名
        :return: none
        """
        self.logger.info(f"等待元素{locator}可见")
        try:
            # 开始等待的时间
            time_start = datetime.datetime.now()
            WD(self.driver, times, poll_frequency).until(EC.visibility_of_all_elements_located(locator))
            # 结束等待时间
            time_end = datetime.datetime.now()
            time_wait = (time_end - time_start).seconds
            # 打印日志
            self.logger.info(f"等待元素{locator}可见结束，开始时间{time_start},结束时间{time_end},等待时长{time_wait}")
        except:
            # 捕捉异常
            self.logger.exception("等待元素可见失败！")
            # 截图
            self.screenshot()
            raise

    def find_element_presence(self, *locator, doc=""):
        """元素存在dom中，即被找到"""
        self.logger.info(f"{doc}查找存在dom中元素：{locator}")
        try:
            WD(self.driver, 10).until(EC.presence_of_element_located(locator))  # 显示等待
            return self.driver.find_element(*locator)
        except:
            # print(locator, '页面未找到元素')
            self.logger.warning(locator, '页面未找到元素')

    def get_elements(self, *locator, doc="", is_displayed=True):

        ele_v = WD(self.driver, 30, 0.5).until(EC.visibility_of_element_located(locator))  # 元素可见
        ele_p = WD(self.driver, 30, 0.5).until(EC.presence_of_element_located(locator))  # 元素存在
        ele_va = WD(self.driver, 30, 0.5).until(EC.visibility_of_all_elements_located(locator))  #
        ele_pa = WD(self.driver, 30, 0.5).until(EC.presence_of_all_elements_located(locator))

        method, value = locator.split(',', maxsplit=1)
        if 'css' in method:
            method = By.CSS_SELECTOR
        elif 'class' in method:
            method = By.CLASS_NAME
        elif 'text' in method:
            method = By.PARTIAL_LINK_TEXT
        elif 'tag' in method:
            method = By.TAG_NAME
        elif 'id' in method:
            method = By.ID
        elif 'xpath' in method:
            method = By.XPATH
        elements = self.driver.find_elements(by=method, value=value)
        new_elements = []
        for element in elements:
            try:
                if ele_pa != '':
                    if is_displayed:
                        if element.is_displayed():
                            new_elements.append(element)
                    else:
                        new_elements.append(element)
                else:
                    if is_displayed:
                        if element.is_displayed():
                            new_elements.append(element)
                    else:
                        new_elements.append(element)
                return new_elements
            except:
                self.logger.exception("查找元素失败！请检查元素是否存在")
                self.screenshot()
                raise


    def get_element(self, locator, index=0, doc=""):

        self.logger.info(f"{doc}查找元素：{locator}{[index]}")
        elements = self.find_elements(*locator)
        try:
            if len(elements) > 0 and index < len(elements):
                return elements[index]
            elif index > len(elements):
                self.logger.warning("输入index超出定位元素列表%s长度！", locator)
            elif len(elements) == 0:
                self.logger.warning("定位元素列表为空：%s", locator)
            else:
                return elements[0]
        except:
            self.logger.exception("查找元素失败！")
            self.screenshot()
            raise



    # def find_element(self, locator, doc=""):
    #     """寻找元素"""
    #     self.logger.info(f"{doc}查找元素：{locator}")
    #     try:
    #         # 2020-10-22 出现问题修改：元素存在dom中但是未可见查找失败
    #         try:
    #             # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
    #             WD(self.driver, 30, 0.5).until(EC.visibility_of_element_located(locator))
    #             return self.driver.find_element(*locator)
    #         except:
    #             WD(self.driver, 30).until(EC.presence_of_element_located(locator))  # 显示等待
    #             return self.driver.find_element(*locator)
    #     except:
    #         # print('找不到定位元素: %s' % loc[1])
    #         self.logger.exception("查找元素失败！")
    #         self.screenshot()
    #         raise

    # def find_elements(self, locator, doc=""):
    #     """寻找多个元素"""
    #     self.logger.info(f"{doc}查找元素：{locator}")
    #     try:
    #         WD(self.driver, 30, 0.5).until(EC.visibility_of_all_elements_located(locator))  # 显示等待
    #         # self.driver.execute_Script("arguments[0].scrollIntoViewIfNeeded(true);", *loc)
    #         # self.driver.wait_element_visible(*locator)
    #         return self.driver.find_elements(*locator)
    #     except:
    #         # print('找不到定位元素: %s' % loc[1])
    #         self.logger.exception("查找元素失败！")
    #         self.screenshot()
    #         raise

    def find_element_by_index(self, locator, index, doc=""):
        """"""
        self.logger.info(f"{doc}查找元素：{locator}{[index]}")
        elements = self.driver.find_elements(*locator)
        if len(elements) > index:
            return elements[int(index)]
        else:
            # print('找不到定位元素: %s' % loc[1])
            self.logger.exception("查找元素失败！")
            self.screenshot()
            raise

    # @wait
    # def click(self, locator, doc=""):
    #     """
    #     点击操作
    #     :param self:
    #     :param locator:
    #     :param doc:
    #     :return:
    #     """
    #     ele = self.find_element(locator, doc)
    #     time.sleep(0.5)
    #     try:
    #         ele.click()
    #         self.logger.info(f"{doc}点击元素{locator}")
    #     except:
    #         self.logger.info("元素点击失败！")
    #         # print("无法点击元素: ", e)
    #         self.screenshot()
    #         # raise

    # @wait
    def send_keys(self, locator, text, doc=""):
        """

        :param self:
        :param locator:
        :param text: 输入内容
        :param doc:
        :return:
        """
        self.logger.info(f"{doc}元素{locator}输入{text}")
        try:
            try:
                ele = self.find_element(locator, doc)
                ele.click()  # 点击
                ele.clear()  # 清空文本框
                ele.send_keys(text)  # 输入文本
            except:
                ele = self.find_elements(locator, doc)
                ele.click()  # 点击
                ele.clear()  # 清空文本框
                ele.send_keys(text)  # 输入文本
        except:
            # print("页面中未能找到元素", loc)
            self.logger.exception("元素输入失败！")
            self.screenshot()
            raise

    def switch_frame(self, locator, doc=""):
        """
        切换frame
        :param locator:
        :param doc:
        :return:
        """
        ele = self.find_element(locator, doc)
        try:
            self.driver.switch_to.frame(ele)
            self.logger.info(f"{doc}进入iframe界面{locator}")
        except:
            self.logger.info("进入iframe界面失败！")
            # print("无法点击元素: ", e)
            self.screenshot()
            raise

    # def switch_back(self, locator, doc=""):
    #     """
    #     切换frame
    #     :param locator:
    #     :param doc:
    #     :return:
    #     """
    #     ele = self.find_element(locator, doc)
    #     try:
    #         self.driver.switch_to.default_content(ele)
    #         self.logger.info(f"{doc}退出iframe界面{locator}")
    #     except:
    #         self.logger.info("退出iframe界面失败！")
    #         # print("无法点击元素: ", e)
    #         self.screenshot()
    #         raise

    def switch_back(self, doc=""):
        """
        切换frame
        :param locator:
        :param doc:
        :return:
        # """
        # ele = self.find_element(locator, doc)
        try:
            self.driver.switch_to.default_content()
            self.logger.info(f"{doc}退出iframe界面")
        except:
            self.logger.info("退出iframe界面失败！")
            # print("无法点击元素: ", e)
            self.screenshot()
            raise

    def execute_script(self, locator, doc=""):
        """
        执行js
        :param locator:
        :param doc:
        :return:
        """
        ele = self.find_element(locator, doc)
        try:
            self.driver.execute_script("arguments[0].click();", ele)
            self.logger.info(f"{doc}js点击{locator}")
        except:
            self.logger.info("js点击操作失败！")
            # print("无法点击元素: ", e)
            self.screenshot()
            raise

    def text(self, locator, doc=""):
        """
        获取text文本
        :param locator:
        :param doc:
        :return:
        """
        ele = self.find_element(locator, doc)
        try:
            # _text = WD(self.driver, 10).until(lambda x: x.find_element(locator).text
            _text = ele.text
            self.logger.info(f"{doc}元素{locator}获取文本成功:{_text}")
            return _text
        except:
            self.logger.info("获取文本失败！")
            # print("无法点击元素: ", e)
            self.screenshot()
            raise

    def move(self, locator, doc=""):
        """
        移动到目的元素
        :param locator:
        :param doc:
        :return:
        """
        ele = self.find_element(locator, doc)
        # 移动到目的元素
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            self.logger.info(f"{doc}鼠标移动到元素{locator}成功")
        except:
            self.logger.info("鼠标移动到元素失败")
            self.screenshot()
            raise

    # def move_to_elem(self, locator, doc=""):
    #     """
    #     :param self:
    #     :param locator:
    #     :param text: 输入内容
    #     :param doc:
    #     :return:
    #     """
    #     ele = self.find_element(locator, doc)
    #     self.logger.info(f"{doc}元素{locator}输入enter")
    #     actionChains = ActionChains(self.driver)
    #     try:
    #         # ele.click()  # 点击
    #         # ele.clear()  # 清空文本框
    #         actionChains.move_to_element(ele)
    #         # actionChains.context_click(ele)
    #     except:
    #         # print("页面中未能找到元素", loc)
    #         self.logger.exception("鼠标悬停目标元素失败！")
    #         self.screenshot()
    #         raise

    # 需要pypiwin32库
    def uploadfile(self):
        filepath = r'F:\1.jpg'
        uploadwindowname = u'打开'  # CHROME窗口名称是打开
        uploadwindow = win32gui.FindWindow('#32770', uploadwindowname)  # 定位“文件上传 窗口
        # print(uploadwindow)

        parent = win32gui.FindWindowEx(uploadwindow, None, 'ComboBoxEx32', None)
        Combobox_real = win32gui.FindWindowEx(parent, None, 'ComboBox', None)
        Edit_box = win32gui.FindWindowEx(Combobox_real, None, 'Edit', None)

        win32gui.SetForegroundWindow(Edit_box)
        time.sleep(1)
        win32gui.SendMessage(Edit_box, win32con.WM_SETTEXT, None, filepath)
        openbuttonname = u'打开(&O)'
        time.sleep(1)
        openbutton = win32gui.FindWindowEx(uploadwindow, None, "Button", openbuttonname)  # 定位“保存”按钮
        # print(openbutton)
        win32gui.PostMessage(openbutton, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        win32gui.PostMessage(openbutton, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    # from selenium.webdriver.common.keys import Keys

    # def send_keys_enter(self, locator, doc=""):
    #     """
    #     :param self:
    #     :param locator:
    #     :param text: 输入内容
    #     :param doc:
    #     :return:
    #     """
    #     ele = self.find_element(locator, doc)
    #     try:
    #         # ele.click()  # 点击
    #         # ele.clear()  # 清空文本框
    #         ele.send_keys(Keys.ENTER)  # 输入文本
    #         self.logger.info(f"{doc}元素{locator}键盘输入enter")
    #
    #     except:
    #         # print("页面中未能找到元素", loc)
    #         self.logger.exception("键盘输入enter失败！")
    #         self.screenshot()
    #         raise

    def keys_enter(self, locator, doc=""):
        """
        :param self:
        :param locator:
        :param text: 输入内容
        :param doc:
        :return:
        """
        ele = self.find_element(locator, doc)
        try:
            # ele.click()  # 点击
            # ele.clear()  # 清空文本框
            ele.send_keys(Keys.ENTER)  # 输入文本
            self.logger.info(f"{doc}元素{locator}键盘输入enter")

        except:
            # print("页面中未能找到元素", loc)
            self.logger.exception("键盘输入enter失败！")
            self.screenshot()
            raise

    def right_click(self, locator, doc=""):
        """
        :param self:
        :param locator:
        :param text: 输入内容
        :param doc:
        :return:
        """

        ele = self.find_element(locator, doc)
        try:
            # ele.click()  # 点击
            # ele.clear()  # 清空文本框
            # actionChains.move_to_element(ele)
            # actionChains = ActionChains(self.driver)
            # actionChains.context_click(ele).perform()
            ActionChains(self.driver).context_click(ele).perform()
            self.logger.info(f"{doc}元素{locator}鼠标右键点击")

        except:
            # print("页面中未能找到元素", loc)
            self.logger.exception("鼠标右键点击失败！")
            self.screenshot()
            raise

    def double_click(self, locator, doc=""):
        """
        :param self:
        :param locator:
        :param text: 输入内容
        :param doc:
        :return:
        """

        ele = self.find_element(locator, doc)
        # actionChains = ActionChains(self.driver)
        try:
            # ele.click()  # 点击
            # ele.clear()  # 清空文本框
            # actionChains.move_to_element(ele)
            # actionChains.double_click(ele).perform()
            ActionChains(self.driver).double_click(ele).perform()
            self.logger.info(f"{doc}元素{locator}鼠标左键双击")

        except:
            # print("页面中未能找到元素", loc)
            self.logger.exception("鼠标左键双击操作失败！")
            self.screenshot()
            raise
