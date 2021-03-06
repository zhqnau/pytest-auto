from selenium.webdriver.common.by import By

doc1 = "选择菜单"

open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控采集范围设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTCOND000004"]/div/iframe')
matt_node_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项环节名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="设置"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//button[@title="设置"]')[0]
intctrlDataSouc = (By.XPATH, '//label[@for="intctrlDataSouc"]/..//input')
intctrlDataSouc_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="mysql"]')
intctrlDataSoucName = (By.XPATH, '//label[@for="intctrlDataSoucName"]/..//input')
intctrlDataSoucName_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="内部控制"]')
data_cond = (By.XPATH, '//label[@for="dataCond"]/..//textarea')
verify_button = (By.XPATH, '//div[@aria-label="指标条件"]//button/span[contains(text(),"验证")]')
save = (By.XPATH, '//div[@aria-label="指标条件"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close_windows = (By.XPATH, '//div[@aria-label="指标条件"]//button/span[contains(text(),"关闭")]')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTCOND000004"]/span')
