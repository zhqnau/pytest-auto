from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产盘点"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[text()="资产盘点"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-pd"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')

intrTime = (By.XPATH, '//label[@for="intrTime"]/..//input')
asetNo = (By.XPATH, '//div[@aria-label="资产盘点信息"]//label[@for="asetNo"]/..//span/i')

asetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
intrCnt = (By.XPATH, '//label[@for="intrCnt"]/..//input')
intrRslt = (By.XPATH, '//div[@aria-label="资产盘点信息"]//label[@for="intrRslt"]/..//input')
intrRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="盘盈"]')
Save = (By.XPATH, '//div[@aria-label="资产盘点信息"]//button/span[contains(text(),"暂存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')


aset_name = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="资产基本信息"]//button/span[contains(text(),"确定")]')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-pd"]/span')










