from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "统计任务登记作废"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控统计任务作废"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTSTTCNCL002"]/div/iframe')
task_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="统计任务名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
taskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="作废"]/i')
taskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="作废"]/i')[0]
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"否")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTSTTCNCL002"]/span')











