from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控参数设置"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控功能模块管理"]')
level3menu = (By.XPATH, '//span[text()="内控参数设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB02RISKRULEPARAS5"]/div/iframe')
rule_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="内控规则名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="维护"]/i')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//button[@title="维护"]/i')[0]
add_button = (By.XPATH, '//div[@aria-label="规则参数信息"]//button/span[contains(text(),"新增")]')
para_code = (By.XPATH, '//label[@for="intctrlParaCode"]/..//input')
para_name = (By.XPATH, '//label[@for="intctrlParaName"]/..//input')
para_type = (By.XPATH, '//label[@for="intctrlParaType"]/..//input')
para_type_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                            '//span[text()="数值型"]')
para_val = (By.XPATH, '//label[@for="intctrlParaval"]/..//input')
para_desc = (By.XPATH, '//label[@for="intctrlParaDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="参数信息"]//button/span[contains(text(),"保存")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB02RISKRULEPARAS5"]/span')


