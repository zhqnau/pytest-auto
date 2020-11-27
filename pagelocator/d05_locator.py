from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "统计任务登记审批"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控统计任务审批"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTSTTAPPR003"]/div/iframe')
task_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="统计任务名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
taskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="审批"]/i')
taskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                      '/ancestor::tr//button[@title="审批"]/i')[0]
approval_result = (By.XPATH, '//label[@for="apprRslt"]/..//input')
result_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                         '//span[text()="通过"]')
approval_opinion = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="统计任务审批表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTSTTAPPR003"]/span')
