from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控任务生成"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控任务生成"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05INTCTRLTASK006"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
month = (By.XPATH, '//div[@aria-label="任务补充"]//label[@class="el-form-item__label"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="任务补充"]//button/span[contains(text(),"查询")]')
generate_Button = (By.XPATH, '//div[@aria-label="任务补充"]//button/span[contains(text(),"生成")]')
close_Button = (By.XPATH, '//div[@aria-label="任务补充"]//button/span[contains(text(),"关闭")]')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
mattquery = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="疑点确认"]')[0]
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="疑点确认"]')
doubt_state = (By.XPATH, '//div[@aria-label="疑点确认信息"]//label[contains(text(),"疑点状态")]/..//input')
state_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                        '//span[text()="问题"]')
cause = (By.XPATH, '//div[@aria-label="疑点确认信息"]//label[contains(text(),"问题原因")]/..//input')
cause_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                        '//span[text()="其他"]')
prb_describe = (By.XPATH, '//div[@aria-label="疑点确认信息"]//label[contains(text(),"疑点确认说明")]/..//textarea')
biz_name = (By.XPATH, '//div[@aria-label="疑点确认信息"]//label[contains(text(),"检查任务名称")]/..//input')
task_objective = (By.XPATH, '//div[@aria-label="疑点确认信息"]//label[contains(text(),"内控任务目标")]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="疑点确认信息"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05INTCTRLTASK006"]/span')

