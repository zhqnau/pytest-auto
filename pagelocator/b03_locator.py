from selenium.webdriver.common.by import By


open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控规则管理流程"]')
level3menu = (By.XPATH, '//span[text()="内控风险规则作废"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB03RISKRULECNCL03"]/div/iframe')
rule_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="内控规则名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
Invalid_button = (By.XPATH, '//div[@class="el-table__fixed-right"]//span'
                            '[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="作废"]')
Invalid_button1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span'
                             '[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="作废"]')[0]
Invalid_reason = (By.XPATH, '//label[@for="cnclOpnn"]/..//textarea')
close_button = (By.XPATH, '//div[@aria-label="维护信息"]//button/span[contains(text(),"关闭")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB03RISKRULECNCL03"]/span')
