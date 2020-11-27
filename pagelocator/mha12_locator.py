from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "违规处置"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[contains(text(),"资产使用申请")]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-sysq"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
asetName = (By.XPATH, '//label[@for="asetName"]/..//span/i')
aset_name = (By.XPATH, '//div[@aria-label="资产选择"]//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//div[@aria-label="资产选择"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="资产选择"]//button/span[contains(text(),"确 定")]')

assetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
usedObjType = (By.XPATH, '//label[@for="usedObjType"]/..//input')
used = (By.XPATH, '//label[@for="used"]/..//textarea')
usedObjType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="个人"]')
save = (By.XPATH, '//div[@aria-label="资产使用申请"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-sysq"]/span')




