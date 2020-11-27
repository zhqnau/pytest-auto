from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控风险规则上报"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="内控风险规则上报"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RULEREPORT0005"]/div/iframe')
increase = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
rule_name = (By.XPATH, '//label[@for="intctrlRuleName"]/..//i/..')
name = (By.XPATH, '//div[@role="button"]/span[contains(text(),"内控规则")]/ancestor::div[@aria-label="内控规则上报"]'
                  '//label[text()="内控规则名称"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="内控规则上报"]//button/span[contains(text(),"查询")]')
ruleinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="选择"]')
ruleinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="选择"]')[0]
save_button = (By.XPATH, '//div[@aria-label="内控规则上报"]//button/span[contains(text(),"保存")]')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
matt_query = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
reported_status = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="上报状态"]/..//input')
reported_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="未上报"]')
report = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"上报")]')
ascertain = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"是")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RULEREPORT0005"]/span')


