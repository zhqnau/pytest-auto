from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产处置备案"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产处置备案"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-czba"]/div/iframe')
aset_name = (By.XPATH, '//div[@id="app"]/div/div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]'
                       '//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//label[text()="资产名称"]/ancestor::form//button/span[contains(text(),"查询")]')
disposalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"0924")]'
                     '/ancestor::tr//button[@title="处置"]/i')
disposalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"0924")]'
                     '/ancestor::tr//button[@title="处置"]/i[1]')

txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-czba"]/span')
dspoWay = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//label[@for="dspoWay"]/..//input')
rentName = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//label[@for="rentName"]/..//input')

lsrName = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//label[@for="lsrName"]/..//input')
usedTime = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//label[@for="usedTime"]/..//input')
usedTimelist = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-picker-panel el-date-picker el-popper"]'
                          '//span[contains(text(),"24")]')
exprTime = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//label[@for="exprTime"]/..//input')
exprTimelist = (By.XPATH,'//div[@id="app"]/following-sibling::div[@class="el-picker-panel el-date-picker el-popper"][2]'
                         '//span[contains(text(),"25")]')
dspoWay_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="出租"]')
Save = (By.XPATH, '//div[@aria-label="资产处置备案信息表"]//button/span[contains(text(),"保存")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')







