from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产登记"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[contains(text(),"资产登记")]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-dj"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')

asetname = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="asetName"]/..//input')
userName = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="userName"]/..//span/i')

asetMtrUnt = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="asetMtrUnt"]/..//input')
bradMol = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="bradMol"]/..//input')
asetVal = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="asetVal"]/..//input')
asetType = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="asetType"]/..//input')
asetType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="办公用品"]')
usedObjType = (By.XPATH, '//div[@aria-label="资产登记"]//label[@for="usedObjType"]/..//input')
usedObjType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="单位"]')
Save = (By.XPATH, '//div[@aria-label="资产登记"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')


user_name = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]/..//input')
user_query = (By.XPATH, '//div[@aria-label="用户姓名"]//label[text()="用户名"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
userinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
userinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
user_save = (By.XPATH, '//div[@aria-label="用户姓名"]//button/span[contains(text(),"确 定")]')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-dj"]/span')










