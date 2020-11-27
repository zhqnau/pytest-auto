from selenium.webdriver.common.by import By


open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控规则管理流程"]')
level3menu = (By.XPATH, '//span[text()="内控风险规则登记"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB03RISKRULEREG001"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
matt_no = (By.XPATH, '//label[@for="servMattNo"]/..//i/..')
matt_name = (By.XPATH, '//div[@aria-label="服务事项信息"]//label[text()="服务事项名称"]/..//input')
risk_querybutton = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"查询")]')
risk_information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                              '/ancestor::tr//span[@class="el-radio__inner"]')
risk_information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                               '/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"选择")]')
matt_node_no = (By.XPATH, '//label[@for="servMattNodeNo"]/..//i/..')
matt_node_name = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//label[text()="服务事项环节名称"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//button/span[contains(text(),"查询")]')
information = (
    By.XPATH,
    '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed"]'
    '//span[contains(text(),"SERVMAT")]/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (
    By.XPATH,
    '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
    '/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button1 = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//button/span[contains(text(),"选择")]')
rule_code = (By.XPATH, '//label[@for="intctrlRuleCode"]/..//input')
rule_name = (By.XPATH, '//label[@for="intctrlRuleName"]/..//input')
ctrl_degree = (By.XPATH, '//label[@for="intctrlDeg"]/..//input')
ctrl_degree_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="提醒类"]')
ctrl_rule_type = (By.XPATH, '//label[@for="intctrlRuleType"]/..//input')
ctrl_rule_type_list = (By.XPATH,
            '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]//span[text()="对服务事项"]')
ctrl_rule_describe = (By.XPATH, '//label[@for="intctrlRuleDscr"]/..//textarea')
msgCont = (By.XPATH, '//label[@for="msgCont"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="维护信息"]//button/span[contains(text(),"暂存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
ser_matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button1 = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
submit = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                    '/ancestor::tr//button[@title="提交"]')
submit1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]')[0]
confirm_button2 = (By.XPATH, '//div[@class="el-message-box__btns"]//button/span[contains(text(),"确认")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB03RISKRULEREG001"]/span')