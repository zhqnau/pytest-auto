from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产采购管理"]')
level4menu = (By.XPATH, '//span[text()="资产购置管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-gzgl"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
splerName = (By.XPATH, '//label[@for="asetOrdDFormEdit.splerName"]/..//input')
spler_name = (By.XPATH, '//div[@aria-label="供应商信息"]//label[text()="供应商名称"]/..//input')
spler_query = (By.XPATH, '//div[@aria-label="供应商信息"]//label[text()="供应商名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
splerinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
splerinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
spler_save = (By.XPATH, '//div[@aria-label="供应商信息"]//button/span[contains(text(),"确定")]')

generationDetails = (By.XPATH, '//div[@aria-label="订单信息维护"]//button/span[contains(text(),"生成明细")]')
save = (By.XPATH, '//div[@aria-label="订单信息维护"]//button/span[contains(text(),"保存")]')
plan_save = (By.XPATH, '//div[@aria-label="资产预算申报明细信息"]//button/span[contains(text(),"确定")]')

plan_name = (By.XPATH, '//div[@aria-label="资产预算申报明细信息"]//label[text()="计划名称"]/..//input')
plan_query = (By.XPATH, '//div[@aria-label="资产预算申报明细信息"]//label[text()="计划名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
planinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
planinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-gzgl"]/span')





