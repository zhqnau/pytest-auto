from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产审批"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产审核管理"]')
level4menu = (By.XPATH, '//span[text()="资产审批"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-sp"]/div/iframe')
aset_name = (By.XPATH, '//div[@id="app"]/div/div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]'
                       '//label[text()="名称"]/..//input')
asetBizType = (By.XPATH, '//label[@for="asetBizType"]/..//input')
asetBizType_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="处置收益"]')
asetApplstas = (By.XPATH, '//label[@for="asetApplstas"]/..//input')
asetApplstas_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="待审批"]')
aset_query = (By.XPATH, '//label[text()="名称"]/ancestor::form//button/span[contains(text(),"查询")]')
approvalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i')
approvalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i[1]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-sp"]/span')
asetApprRslt = (By.XPATH, '//label[@for="asetApprRslt"]/..//input')

apprOpnn = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
asetApprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="通过"]')
Save = (By.XPATH, '//div[@aria-label="资产审核信息"]//button/span[contains(text(),"审批")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')

