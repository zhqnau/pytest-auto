from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产票据"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[text()="资产票据"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-pjgl"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
billName = (By.XPATH, '//label[@for="billName"]/..//input')
asetBillType = (By.XPATH, '//label[@for="asetBillType"]/..//input')
asetBillType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="发票"]')
asetBillSoucType = (By.XPATH, '//div[@aria-label="资产票据信息表"]//label[@for="asetBillSoucType"]/..//input')
asetBillSoucType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="处置收益"]')
billTime = (By.XPATH, '//label[@for="billTime"]/..//input')
billtimelist = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-picker-panel el-date-picker el-popper"]'
                          '//span[contains(text(),"24")]')
biller = (By.XPATH, '//label[@for="biller"]/..//input')
save = (By.XPATH, '//div[@aria-label="资产票据信息表"]//button/span[contains(text(),"保存")]')

bill_name = (By.XPATH, '//div[@id="app"]/div/div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]'
                       '//label[text()="票据名称"]/..//input')
bill_query = (By.XPATH, '//div[@id="app"]/div/div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]'
                       '//label[text()="票据名称"]/ancestor::form//button/span[contains(text(),"查询")]')
billinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
billinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

archiving = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"归档")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-pjgl"]/span')



