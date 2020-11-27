from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控规则管理流程"]')
level3menu = (By.XPATH, '//span[text()="内控风险规则审批"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB03RISKRULEEXAM02"]/div/iframe')
rule_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="内控规则名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
button = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                    '/ancestor::tr//button[@title="审批"]')
button1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]')[0]
app_result = (By.XPATH, '//label[@for="apprRslt"]/..//input')
app_result_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                             '//span[text()="通过"]')
app_opinion = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
approval_button = (By.XPATH, '//div[@aria-label="审批信息"]//button/span[contains(text(),"审批")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB03RISKRULEEXAM02"]/span')

