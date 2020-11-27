from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控任务分派审批"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控任务分派审批"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05TASKAUTHAPPR08"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="审批"]/i')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="审批"]/i')[0]
app_result = (By.XPATH, '//label[@for="apprRslt"]/..//input')
result_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                         '//span[text()="通过"]')
app_opinion = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="审批信息"]//button/span[contains(text(),"审批")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05TASKAUTHAPPR08"]/span')


