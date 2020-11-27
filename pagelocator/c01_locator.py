from selenium.webdriver.common.by import By


open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控功能模块管理"]')
level3menu = (By.XPATH, '//span[text()="受控模块登记"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB02MODUREG0000001"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
servMattNodeName = (By.XPATH, '//label[@for="servMattNodeName"]/..//i/..')
matt_node_name = (By.XPATH, '//div[@aria-label="服务事项环节选择"]'
                            '//label[contains(text(),"业务环节名称")]/..//input')
query_button = (By.XPATH, '//div[@aria-label="服务事项环节选择"]//button/span[contains(text(),"查询")]')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                                      '/ancestor::tr//button[@title="选择"]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="选择"]')[0]
menu_no = (By.XPATH, '//label[@for="menuNo"]/..//i/..')
menu_name = (By.XPATH, '//div[@aria-label="菜单选择"]//label[text()="菜单名称"]/..//input')
menu_query_button = (By.XPATH, '//div[@aria-label="菜单选择"]//button/span[contains(text(),"查询")]')
skmkinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控")]'
                         '/ancestor::tr//button[@title="选择"]/i')
skmkinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控")]'
                          '/ancestor::tr//button[@title="选择"]/i')[0]
warn = (By.XPATH, '//label[@for="bffactWarn"]/..//input')
warn_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"and'
                       '@x-placement="bottom-start"]//span[text()="是"]')
warn_cont = (By.XPATH, '//label[@for="warnCont"]/..//textarea')
rcd_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"and'
                      '@x-placement="bottom-start"]//span[text()="是"]')
SERVMATinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
SERVMATinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
save_button = (By.XPATH, '//div[@aria-label="受控模块"]//button/span[contains(text(),"保存")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB02MODUREG0000001"]/span')
rcd = (By.XPATH, '//label[@for="infactRcd"]/..//input')