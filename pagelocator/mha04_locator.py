from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "供应商管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产采购管理"]')
level4menu = (By.XPATH, '//span[text()="供应商管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-gys"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
splerName = (By.XPATH, '//label[@for="splerName"]/..//input')
coner = (By.XPATH, '//label[@for="coner"]/..//input')
tel = (By.XPATH, '//label[@for="tel"]/..//input')
asetTypeList = (By.XPATH, '//label[@for="asetTypeList"]/..//input')
memu1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper is-multiple"]'
                           '//span[text()="办公用品"]')
memu2 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper is-multiple"]'
                           '//span[text()="办公家具"]')
memu3 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper is-multiple"]'
                           '//span[text()="电子设备"]')
memu4 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper is-multiple"]'
                           '//span[text()="其他"]')
splerAddr = (By.XPATH, '//label[@for="splerAddr"]/..//input')
bankName = (By.XPATH, '//label[@for="bankName"]/..//input')
bankName_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="中国工商银行"]')
bankCardno = (By.XPATH, '//label[@for="bankCardno"]/..//input')
save = (By.XPATH, '//div[@aria-label="供应商信息维护"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-gys"]/span')
textarea = (By.XPATH, '//label[text()="备注"]/..//textarea')





