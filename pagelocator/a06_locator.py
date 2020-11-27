from selenium.webdriver.common.by import By


open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
level3menu = (By.XPATH, '//span[text()="档案规范维护"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATTFILE05"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="编辑"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//button[@title="编辑"]')[0]
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
file_name = (By.XPATH, '//label[@for="fileMatlName"]/..//input')
file_cnt = (By.XPATH, '//label[@for="fileMatlCnt"]/..//input')
file_describe = (By.XPATH, '//label[@for="fileMatlDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="服务事项环节档案规范信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01SERVMATTFILE05"]/span')