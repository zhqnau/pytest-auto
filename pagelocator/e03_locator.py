from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "点击内控手工风险追加"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控手工风险追加"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05SUSPTMANLADD03"]/div/iframe')
add_button = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
mattnoi = (By.XPATH, '//label[@for="servMattNo"]/..//i/..')
matt_no = (By.XPATH, '//div[@aria-label="服务事项信息"]//label[text()="服务事项名称"]/..//input')
mattquery = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@aria-label="服务事项信息"]//div[@class="el-table__fixed-right"]'
                     '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')
mattinf1 = (By.XPATH, '//div[@aria-label="服务事项信息"]//div[@class="el-table__fixed-right"]'
                      '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')[0]
mattnodenoi = (By.XPATH, '//label[@for="servMattNodeNo"]/..//i/..')
mattnodeno = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//label[text()="环节名称"]/..//input')
nodequery = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//button/span[contains(text(),"查询")]')
nodeinf = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed-right"]'
                     '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')
nodeinf1 = (By.XPATH, '//div[@aria-label="服务事项环节信息"]//div[@class="el-table__fixed-right"]'
                      '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')[0]
rulecodei = (By.XPATH, '//label[@for="intctrlRuleId"]/..//i/..')
rule_code = (By.XPATH, '//div[@aria-label="内控规则信息"]//label[text()="内控规则名称"]/..//input')
rulequery = (By.XPATH, '//div[@aria-label="内控规则信息"]//button/span[contains(text(),"查询")]')
ruleinf = (By.XPATH, '//div[@aria-label="内控规则信息"]//div[@class="el-table__fixed-right"]'
                     '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')
ruleinf1 = (By.XPATH, '//div[@aria-label="内控规则信息"]//div[@class="el-table__fixed-right"]'
                      '//span[contains(text(),"SERVMAT")]/ancestor::tr//button[@title="选中"]')[0]
psn_no = (By.XPATH, '//label[@for="insuPsnNo"]/..//input')
ins_name = (By.XPATH, '//label[@for="insuName"]/..//input')
cert_no = (By.XPATH, '//label[@for="certno"]/..//input')
ins_emp = (By.XPATH, '//label[@for="insuEmpNo"]/..//input')
emp_name = (By.XPATH, '//label[@for="empName"]/..//input')
biznamei = (By.XPATH, '//label[@for="bizOpterName"]/..//i/..')
name = (By.XPATH, '//div[@aria-label="业务经办人信息"]//label[text()="经办人姓名"]/..//input')
userquery = (By.XPATH, '//div[@aria-label="业务经办人信息"]//button/span[contains(text(),"查询")]')
userinf = (By.XPATH, '//div[@aria-label="业务经办人信息"]//div[@class="el-table__fixed-right"]'
                     '//span[contains(text(),"测试二")]/ancestor::tr//button[@title="选中"]')
userinf1 = (By.XPATH, '//div[@aria-label="业务经办人信息"]//div[@class="el-table__fixed-right"]'
                      '//span[contains(text(),"测试二")]/ancestor::tr//button[@title="选中"]')[0]
biz_time = (By.XPATH, '//label[@for="bizOptTime"]/..//input')
describe = (By.XPATH, '//label[@for="prbDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="手工风险追加"]//button/span[contains(text(),"暂存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
ser_matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
riskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交"]')
riskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交"]')[0]
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
close = (By.XPATH, '//div[@id="tab-ICSB05SUSPTMANLADD03"]/span')

