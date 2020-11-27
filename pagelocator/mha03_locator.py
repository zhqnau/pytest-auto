from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产购置计划审批"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产采购管理"]')
level4menu = (By.XPATH, '//span[text()="资产购置计划审批"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-gzjhsp"]/div/iframe')
# approval = (By.XPATH,
#             '//*[contains(@class,"el-table--scrollable-y")]/div[5]/div[2]/table/tbody/tr[1]/td[13]/div/span'
#             '/span[1]/button')
approvalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="审批"]/i')
approvalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//button[@title="审批"]/i[1]')
apprRslt = (By.XPATH, '//label[@for="apprRslt"]/..//input')
apprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="通过"]')
apprOpnn = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
approval_button = (By.XPATH, '//div[@aria-label="计划审批"]//button/span[contains(text(),"审批")]')
# approval1 = (By.XPATH, '//div[@class="el-dialog hsa-dialog"and @aria-label="计划审批"]/div[3]/span/button[2]')
# approval_button = (By.XPATH, '//*[contains(@class,"el-button el-button--default el-button--small el-button--primary ")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-gzjhsp"]/span')
plan_name = (By.XPATH, '//label[text()="计划名称"]/..//input')
plan_query = (By.XPATH, '//label[text()="计划名称"]/ancestor::form//button/span[contains(text(),"查询")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')





