from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控指标审批"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="内控指标审批"]')
reported_status = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="上报状态"]/..//input')
iframe = (By.XPATH, '//*[@id="pane-ICSB09INTCTRLKPISL09"]/div/iframe')
reportedstatus_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                 '//span[text()="未上报"]')
query_button = (By.XPATH, '//label[text()="上报状态"]/ancestor::form//button/span[contains(text(),"查询")]')
reportinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="审批"]')
reportinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="审批"]')[0]
approval = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"审批")]')
apprRslt = (By.XPATH, '//div[@aria-label="内控任务结果概述审批"]//label[@for="apprRslt"]/..//input')
apprRslt_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="通过"]')
save_button = (By.XPATH, '//div[@aria-label="内控任务结果概述审批"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09INTCTRLKPISL09"]/span')




