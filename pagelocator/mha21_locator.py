from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产损坏赔付管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产财务管理"]')
level4menu = (By.XPATH, '//span[text()="资产损坏赔付管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-shpfgl"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
asettNo = (By.XPATH, '//label[@for="asetNo"]/..//span/i')
aset_name = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="资产基本信息"]//button/span[contains(text(),"确定")]')
payerName = (By.XPATH, '//label[@for="payerName"]/..//input')
save = (By.XPATH, '//div[@aria-label="资产损坏赔付信息表"]//button/span[contains(text(),"保存")]')
payAmt = (By.XPATH, '//label[@for="payAmt"]/..//input')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-pjgl"]/span')






