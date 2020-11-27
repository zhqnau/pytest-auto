from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "采集执行结果查询"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="采集执行结果查询"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTEVT0000010"]/div/iframe')
name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="统计任务名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTEVT0000010"]/span')




