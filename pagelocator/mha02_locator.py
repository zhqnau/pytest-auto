from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置计划"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产采购管理"]')
level4menu = (By.XPATH, '//span[text()="资产购置计划"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-gzjh"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
purcPlanName = (By.XPATH, '//label[@for="editForm.purcPlanName"]/..//input')
timeks = (By.XPATH, '//label[@for="editForm.planTime"]/..//input[@placeholder="开始日期"]')
timejs = (By.XPATH, '//label[@for="editForm.planTime"]/..//input[@placeholder="结束日期"]')
plan_button = (By.XPATH, '//div[@aria-label="资产购置计划信息维护"]//button/span[contains(text(),"录入明细")]')
# jHTime = (By.XPATH, '//i[@class="el-input__icon el-range__icon el-icon-date"]')
# button = (By.XPATH, '//div[@class = "el-picker-panel__sidebar"]/button[3]')
# lRMX = (By.XPATH, '//*[contains(@class,"el-button el-button--primary el-button--medium")]')[1]
asetName = (By.XPATH, '//label[@for="asetName"]/..//input')
asetType = (By.XPATH, '//label[@for="asetType"]/..//input')
# bGYP = (By.XPATH, '//ul[contains(@class,"el-scrollbar__view el-select-dropdown__list")]/li/span')[19]
asetTypelist = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="办公用品"]')
asetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
asetMtrUnt = (By.XPATH, '//label[@for="asetMtrUnt"]/..//input')
budgPric = (By.XPATH, '//label[@for="budgPric"]/..//input')
plan_save = (By.XPATH, '//div[@aria-label="计划明细信息维护"]//button/span[contains(text(),"保存")]')
Save = (By.XPATH, '//div[@aria-label="资产购置计划信息维护"]//button/span[contains(text(),"暂存")]')
plan_name = (By.XPATH, '//label[text()="计划名称"]/..//input')
plan_query = (By.XPATH, '//label[text()="计划名称"]/ancestor::form//button/span[contains(text(),"查询")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
submit = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]/i')
submit1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]/i')[0]
close = (By.XPATH, '//div[@id="tab-ips-zcgl-gzjh"]/span')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')






