from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控展现设置"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控展现设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04INTCTRLDISP009"]/div/iframe')
matt_node_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项环节名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMATTNODE0713")]'
                         '/ancestor::tr//button[@title="新增"]/i')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMATTNODE0713")]'
                         '/ancestor::tr//button[@title="新增"]/i')[0]
checkbox = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"ICSB01INCOMPATIBLE06")]'
                      '/ancestor::tr//span[@class="el-checkbox__inner"]')
checkbox = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"ICSB01INCOMPATIBLE06")]'
                      '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
saveButton = (By.XPATH, '//div[@aria-label="新增主题信息"]//button/span[contains(text(),"保存")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04INTCTRLDISP009"]/span')







