from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控统计任务登记"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控统计任务登记"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04CLCTSTT0000001"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
stt_name = (By.XPATH, '//label[@for="clctSttName"]/..//input')
next_step = (By.XPATH, '//div[@aria-label="统计任务信息表"]//button/span[contains(text(),"下一步")]')
mattglass = (By.XPATH, '//label[text()="服务事项编号"]/..//i/..')
matt_name = (By.XPATH, '//div[@aria-label="服务事项信息"]//label[text()="服务事项名称"]/..//input')
mattquery = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@aria-label="服务事项信息"]//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//span[@class="el-radio__input"]')
mattinf1 = (By.XPATH, '//div[@aria-label="服务事项信息"]//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                      '/ancestor::tr//span[@class="el-radio__input"]')[0]
mattconfirm = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"确认")]')
eventglass = (By.XPATH, '//label[@for="servMattNodeNo"]/..//i/..')
event_name = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//label[text()="服务事项环节名称"]/..//input')
eventquery = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//button/span[contains(text(),"查询")]')
eventinf = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed"]'
                      '//span[contains(text(),"SERVMAT")]/ancestor::tr//span[@class="el-radio__inner"]')
eventinf1 = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed"]'
                       '//span[contains(text(),"SERVMAT")]/ancestor::tr//span[@class="el-radio__inner"]')[0]
eventconfirm = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//button/span[contains(text(),"确认")]')
ruleinf = (By.XPATH, '//span[contains(text(),"SERVMAT")]/ancestor::tr//span[@class="el-checkbox__inner"]')
ruleinf1 = (By.XPATH, '//span[contains(text(),"SERVMAT")]/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
verify_button = (By.XPATH, '//div[@aria-label="统计任务信息表"]//button/span[contains(text(),"验证")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
cron_name = (By.XPATH, '//div[@aria-label="统计任务信息表"]//label[text()="cron参数"]/..//i/..')
minute = (By.XPATH, '//div[@aria-label="调度时间参数设置"]//div[@class="el-tabs__header is-top"]'
                    '//span[contains(text(),"分")]')
radio = (By.XPATH, '//div[@aria-label="调度时间参数设置"]//span[contains(text(),"每一分钟")]/..'
                   '//span[@class="el-radio__inner"]')
save_button = (By.XPATH, '//div[@aria-label="调度时间参数设置"]//button/span[contains(text(),"保存")]')
tasksave = (By.XPATH, '//div[@aria-label="统计任务信息表"]//button/span[contains(text(),"保存")]')
matt_node_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项环节名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
taskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交"]')
taskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交"]')[0]
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"是")]')
close = (By.XPATH, '//div[@id="tab-ICSB04CLCTSTT0000001"]/span')