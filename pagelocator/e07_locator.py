from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控任务分派"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控任务分派"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05INTCTRLAUTH007"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
matt_query = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="任务分派"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                      '/ancestor::tr//button[@title="任务分派"]')[0]
usertypeinf = (By.XPATH, '//div[@aria-label="内控任务分派"]//div[@class="el-table__fixed"]'
                         '//span[contains(text(),"业务整改人员")]/ancestor::tr//span[@class="el-radio__inner"]')
usertypeinf1 = (By.XPATH, '//div[@aria-label="内控任务分派"]//div[@class="el-table__fixed"]'
                          '//span[contains(text(),"业务整改人员")]/ancestor::tr//span[@class="el-radio__inner"]')[0]
psn_account = (By.XPATH, '//label[@for="psnUact"]/..//i/..')
user_account = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//label[text()="用户帐号"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"查询")]')
userinf = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//div[@class="el-table__fixed"]'
                     '//span[contains(text(),"develop")]/ancestor::tr//span[@class="el-radio__inner"]')
userinf1 = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//div[@class="el-table__fixed"]//span'
                      '[contains(text(),"develop")]/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button = (By.XPATH, '//div[@aria-label="查询经办人员信息"]//button/span[contains(text(),"确认")]')
memo = (By.XPATH, '//div[@aria-label="内控任务分派"]//label[@for="memo"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="内控任务分派"]//button/span[contains(text(),"暂存")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交分派申请"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="提交分派申请"]')[0]
ascertain = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05INTCTRLAUTH007"]/span')
