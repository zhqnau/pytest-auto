from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控风险询问"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控风险询问"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05SUSPTINQ000011"]/div/iframe')
name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
askinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="询问"]')
askinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="询问"]')[0]
glass_query = (By.XPATH, '//label[@for="rspderName"]/..//i/..')
user_account = (By.XPATH, '//div[@aria-label="业务经办人员信息"]//label[text()="用户帐号"]/..//input')
userquery = (By.XPATH, '//div[@aria-label="业务经办人员信息"]//button/span[contains(text(),"查询")]')
userinf = (By.XPATH, '//div[@aria-label="业务经办人员信息"]//div[@class="el-table__fixed"]'
                     '//span/ancestor::tr//span[@class="el-radio__inner"]')
userinf1 = (By.XPATH, '//div[@aria-label="业务经办人员信息"]//div[@class="el-table__fixed"]'
                      '//span/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button = (By.XPATH, '//div[@aria-label="业务经办人员信息"]//button/span[contains(text(),"确认")]')
inq_cont = (By.XPATH, '//label[@for="inqCont"]/..//textarea')
confirmbutton = (By.XPATH, '//div[@aria-label="询问信息"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05SUSPTINQ000011"]/span')
