from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产分配管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产分配管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-fpgl"]/div/iframe')
aset_name = (By.XPATH, '//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//label[text()="资产名称"]/ancestor::form//button/span[contains(text(),"查询")]')
allocationinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"0924测试")]'
                     '/ancestor::tr//button[@title="分配"]/i')
allocationinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"0924测试")]'
                     '/ancestor::tr//button[@title="分配"]/i[1]')
allocation_button = (By.XPATH, '//div[@aria-label="资产分配信息表"]//button/span[text()="添加分配"]')

asetName = (By.XPATH, '//label[@for="asetName"]/..//span/i')

asetlinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"0924测试")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
asetlinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"0924测试")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="分配资产"]//button/span[contains(text(),"确 定")]')
ownr = (By.XPATH, '//label[@for="ownr"]/..//span/i')
ownr_name = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]/..//input')
ownr_query = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
ownrinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
ownrinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
ownr_save = (By.XPATH, '//div[@aria-label="用户姓名"]//button/span[contains(text(),"确 定")]')

save = (By.XPATH, '//label[text()="归属人"]/ancestor::div[@aria-label="资产分配信息表"]//button/span[text()="保存"]')
Save = (By.XPATH, '//label[text()="申请人"]/ancestor::div[@aria-label="资产分配信息表"]//button/span[text()="保存"]')

txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-fpgl"]/span')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')


