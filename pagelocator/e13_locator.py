from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控任务授权作废"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控任务授权作废"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05TASKAUTHCNCL13"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_matt = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
riskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控处理人员")]'
                         '/ancestor::tr//button[@title="修改"]')
riskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"内控处理人员")]'
                         '/ancestor::tr//button[@title="修改"]')[0]
psn_account = (By.XPATH, '//label[@for="psnUact"]/..//i/..')
user_account = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//label[text()="用户帐号"]/..//input')
query_user = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"查询")]')
userinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"develop")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
userinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"develop")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_user = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"确认")]')
authDscr = (By.XPATH, '//div[@aria-label="授权变更信息"]//label[@for="authDscr"]/..//textarea')
save_change = (By.XPATH, '//div[@aria-label="授权变更信息"]//button/span[contains(text(),"保存")]')
increase = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
account = (By.XPATH, '//label[@for="psnUact"]/..//i/..')
account_id = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//label[text()="用户帐号"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"develop")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"develop")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"确认")]')
save_button = (By.XPATH, '//div[@aria-label="授权变更信息"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05TASKAUTHCNCL13"]/span')




