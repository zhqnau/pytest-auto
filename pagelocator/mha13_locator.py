from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产使用审批"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产使用审批"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-sysp"]/div/iframe')
aset_name = (By.XPATH, '//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//label[text()="资产名称"]/ancestor::form//button/span[contains(text(),"查询")]')
approvalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i')
approvalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i[1]')

apprRslt = (By.XPATH, '//label[@for="apprRslt"]/..//input')
apprOpnn = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
apprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="通过"]')

Save = (By.XPATH, '//div[@aria-label="资产使用审批"]//button/span[contains(text(),"保存")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-sysp"]/span')




