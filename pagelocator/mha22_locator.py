from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产处置收益管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产处置收益管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-czsygl"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
asetNo = (By.XPATH, '//label[@for="asetNo"]/..//input')
aset_name = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//div[@aria-label="资产基本信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="资产基本信息"]//button/span[contains(text(),"确定")]')

asetCnt = (By.XPATH, '//div[@aria-label="资产处置收益信息"]//label[@for="asetCnt"]/..//input')
dspoWay = (By.XPATH, '//div[@aria-label="资产处置收益信息"]//label[@for="dspoWay"]/..//input')
dspoWay_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="处置"]')
dstnEmp = (By.XPATH, '//div[@aria-label="资产处置收益信息"]//label[@for="dstnEmp"]/..//input')
amt = (By.XPATH, '//div[@aria-label="资产处置收益信息"]//label[@for="amt"]/..//input')
Save = (By.XPATH, '//div[@aria-label="资产处置收益信息"]//button/span[contains(text(),"暂存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-czsygl"]/span')






