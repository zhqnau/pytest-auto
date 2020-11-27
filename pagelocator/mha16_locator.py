from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产报废"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[text()="资产报废"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-bf"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
invdRea = (By.XPATH, '//label[@for="invdRea"]/..//textarea')

volauser_name = (By.XPATH, '//label[text()="用户姓名"]/..//input')

aset_button = (By.XPATH, '//div[@aria-label="报废信息维护"]//button/span[contains(text(),"选择资产")]')

aset_name = (By.XPATH, '//div[@aria-label="固定资产信息"]//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//div[@aria-label="固定资产信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')

asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"0924测试")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"0924测试")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
aset_save = (By.XPATH, '//div[@aria-label="固定资产信息"]//button/span[contains(text(),"确定")]')
save = (By.XPATH, '//div[@aria-label="报废信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-bf"]/span')






