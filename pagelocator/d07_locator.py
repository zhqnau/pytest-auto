from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控规则模版设置"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控规则模版设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTRULETMPL07"]/div/iframe')
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
rule_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="内控规则名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
setting = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="设置"]/i')
setting1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="设置"]/i')[0]
clc_type = (By.XPATH, '//label[@for="clctType"]/..//input')
clc_type_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                           '//span[text()="事后"]')
data_type = (By.XPATH, '//label[@for="intctrlDataSouc"]/..//input')
data_type_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="mysql"]')
data_name = (By.XPATH, '//label[@for="intctrlDataSoucName"]/..//input')
data_name_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="内部控制"]')
data_cond = (By.XPATH, '//label[@for="dataCond"]/..//textarea')
note = (By.XPATH, '//label[contains(text(),"备注")]/..//textarea')
verify_button = (By.XPATH, '//div[@aria-label="指标条件"]//button/span[contains(text(),"验证")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
save_button = (By.XPATH, '//div[@aria-label="指标条件"]//button/span[contains(text(),"保存")]')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTRULETMPL07"]/span')





