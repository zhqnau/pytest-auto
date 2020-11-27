from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控整改结果录入"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控整改结果录入"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05TASKRECTIFY010"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
zginf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//button[@title="整改"]')
zginf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//button[@title="整改"]')[0]
rectification_time = (By.XPATH, '//label[@for="rfomTime"]/..//input')
resultinput = (By.XPATH, '//label[@for="rfomRslt"]/..//input')
result_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                         '//span[text()="已整改"]')
rectification_detail = (By.XPATH, '//div[@aria-label="内控检查任务整改"]//label[@for="rfomDetl"]'
                                  '/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="内控检查任务整改"]//button/span[contains(text(),"暂存")]')
tjinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"")]'
                         '/ancestor::tr//button[@title="提交"]')
tjinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"")]'
                         '/ancestor::tr//button[@title="提交"]')[0]
ascertain = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"是")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05TASKRECTIFY010"]/span')



