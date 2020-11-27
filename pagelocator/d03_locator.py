from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控采集抽样设置"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控采集抽样设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTSMPLSET006"]/div/iframe')
colinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                    '/ancestor::tr//button[@title="抽样设置"]/i')
colinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="抽样设置"]/i')[0]
matt_node_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项环节名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
samp_type = (By.XPATH, '//label[@for="smplType"]/..//input')
samp_type_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"and'
                                    '@x-placement="bottom-start"]//span[text()="普通抽样"]')
samp_rat = (By.XPATH, '//label[@for="smplRat"]/..//input')
high_cnt = (By.XPATH, '//label[@for="highCnt"]/..//input')
save_button = (By.XPATH, '//div[@aria-label="采集抽样设置信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTSMPLSET006"]/span')
