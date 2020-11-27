from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "受控模块作废申请"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控功能模块管理"]')
level3menu = (By.XPATH, '//span[text()="受控模块作废申请"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB02MODUCNCL000003"]/div/iframe')
menu_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="受控模块名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交申请"]/i')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//button[@title="提交申请"]/i')[0]
apply_describe = (By.XPATH, '//label[@for="appyDesc"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="生效申请信息"]//button/span[contains(text(),"保存")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB02MODUCNCL000003"]/span')