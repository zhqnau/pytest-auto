from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "受控模块审批"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控功能模块管理"]')
level3menu = (By.XPATH, '//span[text()="受控模块审批"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB02MODUAPPR000004"]/div/iframe')
name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="受控模块名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控")]'
                         '/ancestor::tr//button[@title="审批"]/i')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控")]'
                          '/ancestor::tr//button[@title="审批"]/i')[0]
apply_result = (By.XPATH, '//label[@for="apprRslt"]/..//input')
apply_result_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                               '//span[text()="通过"]')
approval_opinion = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB02MODUAPPR000004"]/span')
save_button = (By.XPATH, '//div[@aria-label="审批信息"]//button/span[contains(text(),"保存")]')