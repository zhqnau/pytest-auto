from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产采购付款管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产财务管理"]')
level4menu = (By.XPATH, '//span[text()="资产采购付款管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-cgfk"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
spler_name = (By.XPATH, '//div[@aria-label="资产订单信息"]//label[text()="供应商名称"]/..//input')
spler_query = (By.XPATH, '//div[@aria-label="资产订单信息"]//label[text()="供应商名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
splerinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
splerinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
spler_save = (By.XPATH, '//div[@aria-label="资产订单信息"]//button/span[contains(text(),"确定")]')

paymtd = (By.XPATH, '//label[@for="paymtd"]/..//input')
paymtd_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                         '//span[text()="现金"]')
save = (By.XPATH, '//div[@aria-label="资产采购付款信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-cgfk"]/span')







