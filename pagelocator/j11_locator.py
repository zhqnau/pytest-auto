from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控风险规则上报审批"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="内控风险规则上报审批"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RULEREPORT0015"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
matt_query = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
report = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"审批")]')
apprRslt = (By.XPATH, '//div[@aria-label="审批信息"]//label[@for="apprRslt"]/..//input')
apprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="通过"]')
apprOpnn = (By.XPATH, '//div[@aria-label="审批信息"]//label[@for="apprOpnn"]/..//textarea')

save_button = (By.XPATH, '//div[@aria-label="审批信息"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RULEREPORT0015"]/span')

