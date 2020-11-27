
from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置需求"
# menuRight = (By.CSS_SELECTOR, 'div.swiper-button-next swiper-arrow>i')
menuRight = (By.XPATH, '//div[@aria-label="Next slide"]')
level1menu = (By.XPATH, '//div[contains(text(),"医保业务基础子系统")]')
level2menu = (By.XPATH, '//span[text()="参保管理"]')
level3menu = (By.XPATH, '//span[text()="参保登记管理"]')
level4menu = (By.XPATH, '//span[text()="单位复核管理（复审）"]')

iframe = (By.XPATH, '//*[@id="pane-mbs-emp-rew-02"]/div/iframe')
# zJia = (By.XPATH, '//div[starts-with(@id,"el-collapse-head-")]/div/button')

# empNo = (By.XPATH, '//*[@style="display: block;"]//input[@id="empNo" and @class="ant-input"]')
EMP_NO = (By.XPATH, '//input[@id="empNo"]')

# QUERY_BUTTON = (By.XPATH, '//button[@class="ant-btn ant-btn-primary"]//span[text()="查 询"]')
QUERY_BUTTON = (By.XPATH, '//form[@class="ant-form ant-form-horizontal ant-row ant-form-auto-layout"]//button[@class="ant-btn ant-btn-primary"]')
# SAVE_BUTTON = (By.XPATH, '//div[@class="footer"]//span[contains(text(),"保 存")]')
SAVE_BUTTON = (By.XPATH, '//div[@class="footer"]//button[@class="ant-btn ant-btn-primary"]')

CONFIRM_BUTTON = (By.XPATH, '//div[@class="ant-modal-body"]//button[@class="ant-btn ant-btn-primary"]')

# BIZ_TYPE = (By.XPATH, '//div[@class="ant-select-selection ant-select-selection--single" and @aria-expanded="true"]')
BIZ_TYPE = (By.XPATH, '//div[text()="请选择"]')
BIZ_TYPE_LIST = (By.XPATH, '//li[text()="单位注销"]')
# bGYP = (By.XPATH, '//ul[contains(@class,"el-scrollbar__view el-select-dropdown__list")]/li/span')[11]

#//tr[@data-row-key="0"]//td[@class="ant-table-fixed-columns-in-body"]//a[@class="ta-color-detail"]
SELECT = (By.XPATH, '//tr[@data-row-key="0"]//td[@class="ant-table-selection-column"]//input[@class="ant-checkbox-input"]')

CHECK =  (By.XPATH, '//div[@class="ant-card-extra"]//button[@class="ant-btn ant-btn-primary"]')


txt = (By.XPATH, '//span[text()="批量审核完成"]')

close = (By.XPATH, '//div[@id="tab-mbs-emp-rew-02"]/span')

