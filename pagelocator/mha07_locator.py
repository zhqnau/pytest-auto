from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产预算申报审批"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产预算管理"]')
level4menu = (By.XPATH, '//span[text()="资产预算申报审批"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-yssbsp"]/div/iframe')
approvalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i')
approvalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]/i[1]')
asetApprRslt = (By.XPATH, '//label[@for="asetApprRslt"]/..//input')
asetApprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="通过"]')
apprOpnn = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
approval = (By.XPATH, '//div[@aria-label="申报信息审批"]//button/span[contains(text(),"审批")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-yssbsp"]/span')

Name = (By.XPATH, '//div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]//label[text()="计划名称"]/..//input')
query = (By.XPATH, '//div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]//label[text()="计划名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')



