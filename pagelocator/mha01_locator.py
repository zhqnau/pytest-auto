from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置需求"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产采购管理"]')
level4menu = (By.XPATH, '//span[text()="资产购置需求"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-gzxq"]/div/iframe')
# zJia = (By.XPATH, '//div[starts-with(@id,"el-collapse-head-")]/div/button')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
asetName = (By.XPATH, '//label[@for="asetName"]/..//input')
asetType = (By.XPATH, '//label[@for="asetType"]/..//input')
# bGYP = (By.XPATH, '//ul[contains(@class,"el-scrollbar__view el-select-dropdown__list")]/li/span')[11]
asetTypelist = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="办公用品"]')
asetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
asetMtrUnt = (By.XPATH, '//label[@for="asetMtrUnt"]/..//input')
appyRea = (By.XPATH, '//label[@for="appyRea"]/..//textarea')
save = (By.XPATH, '//div[@aria-label="购置需求信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-gzxq"]/span')







