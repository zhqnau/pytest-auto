import datetime
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from utils.dir_config import *
import time
# import win32con
# import win32gui


class BasePage(object):
    """
    二次封装
    1、封装基本函数--执行日志、异常处理、失败截图
    2、所有页面的公共部分
    
    更新日志（2020-10-30）：
    1、优化find_element和find_elements写法
    2、增加dom中存在但不可见元素的定位
    3、增加返回find_elements 的数组的定位，如果有多个符合条件的元素，还可以指定要点击第几个,默认index=0
    
    例如：EMP_NO = (By.XPATH, '//input[@id="empNo"]')
    self.driver.send_keys(EMP_NO, empNo, "单位编号", 1)
    即第2个id 为 empNo 的输入框输入empNo
    """
    def __init__(self, browser):
        self.driver = browser
        self.logger = Logger.get_logger()
        self.timeout = 30
        self.driver.implicitly_wait(30)
        self.wait = WD(self.driver, self.timeout)

    def get_url(self, url):
        """
        打开网址并验证
        :param url: 网址
        :return:
        """
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
        等待元素可见
        :param locator: 元素定位（元祖形式：元素定位类型、元素定位方式。例如(BY.XPATH, //div)）
        :param times: 等待时间 times=30
        :param poll_frequency: 等待周期 poll_frequency=0.5
        :param doc: 记录日志描述：模块名——页面名——操作名
        :return:
        """
        self.logger.info(f"{doc}界面，等待元素{locator}可见")
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
            self.logger.exception(f"{doc}界面，等待元素{locator}可见失败！")
            # 截图
            self.screenshot()
            raise

    def find_element_presence(self, *locator, doc=""):
        """
        元素存在dom中，即被找到
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :return:
        """
        self.logger.info(f"{doc}界面，查找存在dom中元素：{locator}")
        try:
            WD(self.driver, 10).until(EC.presence_of_element_located(locator))  # 显示等待
            return self.driver.find_element(*locator)
        except:
            self.logger.warning(f"{doc}界面，未找到{locator}元素！")
            raise

    def is_element_exist(self, locator, doc=""):
        """
        元素是否存在
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :return:
        """
        self.logger.info(f"{doc}界面，判断元素存在：{locator}")
        try:
            element = self.find_element(*locator)
            if element == '':
                self.logger.exception(f"{doc}界面，元素{locator}不存在！")
                return False
            else:
                self.logger.exception(f"{doc}界面，元素{locator}存在！")
                return True
        except:
            self.logger.info(f"{doc}界面，判断元素元素{locator}存在失败！请检查！")
            raise

    def find_elements(self, *locator, doc=""):
        """
        寻找多个元素
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :return:
        """
        self.logger.info(f"{doc}界面，查找元素：{locator}")
        elements = self.driver.find_elements(*locator)
        new_elements = []
        try:
            for element in elements:
                try:
                    # ele_va = WD(self.driver, 90, 0.5).until(EC.visibility_of_all_elements_located(locator))  # 元素可见
                    WD(self.driver, 30, 0.5).until(EC.visibility_of_element_located(locator))  # 元素可见
                    new_elements.append(element)
                except:
                    # ele_pa = WD(self.driver, 90, 0.5).until(EC.presence_of_all_elements_located(locator))  # 所有元素存在
                    WD(self.driver, 30, 0.5).until(EC.presence_of_element_located(locator))  # 元素存在
                    new_elements.append(element)
            return new_elements
        # try:
        #     # ele_pa = WD(self.driver, 90, 0.5).until(EC.presence_of_all_elements_located(locator))  # 所有元素存在
        #     ele_p = WD(self.driver, 90, 0.5).until(EC.presence_of_element_located(locator))  # 元素存在
        #     for element in elements:
        #         if ele_p != '':
        #             # ele_va = WD(self.driver, 90, 0.5).until(EC.visibility_of_all_elements_located(locator))  # 元素可见
        #             ele_v = WD(self.driver, 90, 0.5).until(EC.visibility_of_element_located(locator))  # 元素可见
        #             if ele_v != '':
        #                 new_elements.append(element)
        #         else:
        #             new_elements.append(element)
        #     # print(new_elements)
        #     return new_elements
        except:
            self.logger.exception(f"{doc}界面，查找元素：{locator}失败！请检查元素是否存在")
            self.screenshot()
            raise

    def find_element(self, locator, doc="", index=0):
        """
        查找元素返回locator_list，默认第1个可用index指定第N个locator
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        self.logger.info(f"{doc}界面，查找元素：{locator}{[index]}")
        elements = self.find_elements(*locator, doc="")
        try:
            if len(elements) > 0 and index < len(elements):
                return elements[int(index)]
            elif index > len(elements):
                self.logger.warning("输入index超出定位元素列表%s长度！", locator)
            elif len(elements) == 0:
                self.logger.warning("定位元素列表为空：%s", locator)
            else:
                return elements[0]
        except:
            self.logger.exception(f"{doc}界面，查找元素：{locator}{[index]}失败！")
            self.screenshot()
            raise

    def click(self, locator, doc="", index=0):
        """
        点击操作
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator, doc=doc)
        time.sleep(0.5)
        self.logger.info(f"{doc}点击元素{locator}{[index]}")
        try:
            elements[int(index)].click()
        except:
            self.logger.info(f"{doc}点击元素{locator}{[index]}失败！")
            self.screenshot()
            raise

    def send_keys(self, locator, text, doc="", index=0):
        """
        键盘输入操作
        :param locator: (BY.XPATH, //div)
        :param text: 输入内容
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        try:
            elements = self.find_elements(*locator, doc=doc)
            elements[index].click()  # 点击
            elements[index].clear()  # 清空文本框
            elements[index].send_keys(text)  # 输入文本
            self.logger.info(f"{doc},元素{locator}{[index]}输入{text}")
        except:
            self.logger.exception(f"{doc}界面,元素{locator}{[index]}输入{text}失败！")
            self.screenshot()
            raise

    def switch_frame(self, locator, doc="", index=0):
        """
        切换frame
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        self.logger.info(f"{doc}进入iframe界面{locator}{[index]}")
        try:
            self.driver.switch_to.frame(elements[int(index)])
        except:
            self.logger.info("进入iframe界面失败！")
            self.screenshot()
            raise

    def switch_back(self, doc=""):
        """
        退出frame
        :param doc: 记录日志描述：模块名——页面名——操作名
        :return:
        """
        self.logger.info(f"{doc}退出iframe界面")
        try:
            self.driver.switch_to.default_content()
        except:
            self.logger.info("退出iframe界面失败！")
            self.screenshot()
            raise

    def execute_script(self, locator, doc="", index=0):
        """
        执行js
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        self.logger.info(f"{doc}js点击{locator}")
        try:
            self.driver.execute_script("arguments[0].click();", elements[int(index)])
        except:
            self.logger.info("js点击操作失败！")
            self.screenshot()
            raise

    def text(self, locator, doc="", index=0):
        """
        获取text文本
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        try:
            _text = elements[index].text
            self.logger.info(f"{doc}界面，元素{locator}获取文本成功:{_text}")
            return _text
        except:
            self.logger.info(f"{doc}界面，元素{locator}获取文本失败！")
            self.screenshot()
            raise

    def move(self, locator, doc="", index=0):
        """
        移动到目的元素
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator, doc=doc)
        self.logger.info(f"{doc}界面，鼠标移动到元素{locator}")
        # 移动到目的元素
        try:
            ActionChains(self.driver).move_to_element(elements[int(index)]).perform()
        except:
            self.logger.info(f"{doc}界面，鼠标移动到元素{locator}失败")
            self.screenshot()
            raise

    # # 需要pypiwin32库
    # def uploadfile(self):
    #     filepath = r'F:\1.jpg'
    #     uploadwindowname = u'打开'  # CHROME窗口名称是打开
    #     uploadwindow = win32gui.FindWindow('#32770', uploadwindowname)  # 定位“文件上传 窗口
    #     # print(uploadwindow)
    #
    #     parent = win32gui.FindWindowEx(uploadwindow, None, 'ComboBoxEx32', None)
    #     Combobox_real = win32gui.FindWindowEx(parent, None, 'ComboBox', None)
    #     Edit_box = win32gui.FindWindowEx(Combobox_real, None, 'Edit', None)
    #
    #     win32gui.SetForegroundWindow(Edit_box)
    #     time.sleep(1)
    #     win32gui.SendMessage(Edit_box, win32con.WM_SETTEXT, None, filepath)
    #     openbuttonname = u'打开(&O)'
    #     time.sleep(1)
    #     openbutton = win32gui.FindWindowEx(uploadwindow, None, "Button", openbuttonname)  # 定位“保存”按钮
    #     # print(openbutton)
    #     win32gui.PostMessage(openbutton, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    #     win32gui.PostMessage(openbutton, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    def keys_enter(self, locator, doc="", index=0):
        """
        键盘按下enter键
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        self.logger.info(f"{doc}界面，元素{locator}键盘按下enter键")
        try:
            elements[index].send_keys(Keys.ENTER)
        except:
            self.logger.exception(f"{doc}界面，元素{locator}键盘按下enter键失败！")
            self.screenshot()
            raise

    def right_click(self, locator, doc="", index=0):
        """
        点击鼠标右键
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        self.logger.info(f"{doc}界面，元素{locator}点击鼠标右键")
        try:
            ActionChains(self.driver).context_click(elements[int(index)]).perform()
        except:
            self.logger.exception(f"{doc}界面，元素{locator}点击鼠标右键失败！")
            self.screenshot()
            raise

    def double_click(self, locator, doc="", index=0):
        """
        双击鼠标左键
        :param locator: (BY.XPATH, //div)
        :param doc: 记录日志描述：模块名——页面名——操作名
        :param index: 结果列表例如(BY.XPATH, //div)[0]
        :return:
        """
        elements = self.find_elements(*locator)
        self.logger.info(f"{doc}界面，元素{locator}双击鼠标左键")
        try:
            ActionChains(self.driver).double_click(elements[int(index)]).perform()
        except:
            self.logger.exception("f{doc}界面，元素{locator}双击鼠标左键失败！")
            self.screenshot()
            raise
