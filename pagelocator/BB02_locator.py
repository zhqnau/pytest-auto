
from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置需求"
# menuRight = (By.CSS_SELECTOR, 'div.swiper-button-next swiper-arrow>i')
menuRight = (By.XPATH, '//div[@aria-label="Next slide"]')
level1menu = (By.XPATH, '//div[contains(text(),"医保业务基础子系统")]')
level2menu = (By.XPATH, '//span[text()="参保管理"]')
level3menu = (By.XPATH, '//span[text()="参保单位管理"]')
level4menu = (By.XPATH, '//span[text()="单位信息维护"]')

iframe = (By.XPATH, '//*[@id="pane-mbs-emp-mnt-01"]/div/iframe')
# zJia = (By.XPATH, '//div[starts-with(@id,"el-collapse-head-")]/div/button')

# empNo = (By.XPATH, '//*[@style="display: block;"]//input[@id="empNo" and @class="ant-input"]')
EMP_NO = (By.XPATH, '//*[@style="display: block;"]//input[@placeholder="单位编号+enter或点击搜索查询"]')

CONER_NAME = (By.XPATH, '//input[@id="conerName"]')

# SAVE_BUTTON = (By.XPATH, '//div[@class="footer"]//span[contains(text(),"保 存")]')
SAVE_BUTTON = (By.XPATH, '//div[@class="footer"]//button[@class="ant-btn ant-btn-primary"]')

asetType = (By.XPATH, '//label[@for="asetType"]/..//input')
# bGYP = (By.XPATH, '//ul[contains(@class,"el-scrollbar__view el-select-dropdown__list")]/li/span')[11]
asetTypelist = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="办公用品"]')
asetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
asetMtrUnt = (By.XPATH, '//label[@for="asetMtrUnt"]/..//input')
appyRea = (By.XPATH, '//label[@for="appyRea"]/..//textarea')
save = (By.XPATH, '//div[@aria-label="购置需求信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//span[text()="提交成功"]')
close = (By.XPATH, '//div[@id="tab-mbs-emp-mnt-01"]/span')

