from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产出库管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[text()="资产出库管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-ckgl"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')

order_name = (By.XPATH, '//div[@aria-label="资产库存信息"]//label[text()="资产名称"]/..//input')
order_query = (By.XPATH, '//div[@aria-label="资产库存信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
orderinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
orderinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
order_save = (By.XPATH, '//div[@aria-label="资产库存信息"]//button/span[contains(text(),"确定")]')

asetCnt = (By.XPATH, '//label[@for="asetCnt"]/..//input')
asetStooutRea = (By.XPATH, '//div[@aria-label="资产出库信息维护"]//label[@for="asetStooutRea"]/..//input')
asetStooutRea_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="借用"]')
recer = (By.XPATH, '//label[@for="recer"]/..//span/i')
recer_name = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]/..//input')
recer_query = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
recerinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
recerinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
recer_save = (By.XPATH, '//div[@aria-label="用户姓名"]//button/span[contains(text(),"确 定")]')
save = (By.XPATH, '//div[@aria-label="资产出库信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-ckgl"]/span')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')

reger = (By.XPATH, '//label[@for="reger"]/..//input')



