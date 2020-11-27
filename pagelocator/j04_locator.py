from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "风险信息发布"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="风险信息发布"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RISKRLS0000002"]/div/iframe')
report_title = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="风险发布标题"]/..//input')
query_button = (By.XPATH, '//label[text()="风险上报标题"]/ancestor::form//button/span[contains(text(),"查询")]')
reported = (By.XPATH, '//div[@role="tab"]//div[contains(text(),"已上报")]')
riskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="发布风险信息"]')
riskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="发布风险信息"]')[0]
risk_title = (By.XPATH, '//label[@for="rlsTtl"]/..//input')
risk_title_type = (By.XPATH, '//label[@for="rlsType"]/..//input')
risk_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                       '//span[text()="风险数据发布"]')
report_content = (By.XPATH, '//label[@for="rlsCont"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="风险发布"]//button/span[contains(text(),"保存")]')
reportinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
reportinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
release = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"发布")]')
receiver_array = (By.XPATH, '//label[@for="receiverArray"]/..//input')
receiver_array_list = (By.XPATH, '//div[@id="app"]/following-sibling::div//ul//span[contains(text(),"新疆省")]')
confirm_button = (By.XPATH, '//div[@aria-label="内控风险信息发布"]//button/span[contains(text(),"确定")]')
ascertain = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"是")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RISKRLS0000002"]/span')


