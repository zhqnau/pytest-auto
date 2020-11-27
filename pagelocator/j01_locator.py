from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "风险信息上报"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="风险信息上报"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RISKRPUP000001"]/div/iframe')
increase = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
report_title = (By.XPATH, '//label[@for="rpupTtl"]/..//input')
report_title_type = (By.XPATH, '//label[@for="rpupType"]/..//input')
title_type_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                             '//span[text()="业务风险"]')
report_content = (By.XPATH, '//label[@for="rpupCont"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="风险上报"]//button/span[contains(text(),"保存")]')
risk_report_title = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="风险上报标题"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
report = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"上报")]')
ascertain = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"是")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RISKRPUP000001"]/span')






