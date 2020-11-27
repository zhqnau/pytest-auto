from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产预算申报管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产预算管理"]')
level4menu = (By.XPATH, '//span[text()="资产预算申报管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-yssb"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')

planName = (By.XPATH, '//div[@aria-label="购置计划信息"]//label[text()="购置计划名称"]/..//input')
plan_query = (By.XPATH, '//div[@aria-label="购置计划信息"]//label[text()="购置计划名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
planinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
planinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
plan_save = (By.XPATH, '//div[@aria-label="购置计划信息"]//button/span[contains(text(),"确定")]')
datailed_button = (By.XPATH, '//div[@aria-label="资产预算申报信息维护"]//button/span[contains(text(),"新增申报明细")]')

inquiryName = (By.XPATH, '//div[@aria-label="资产预算询价信息"]//label[text()="资产名称"]/..//input')
inquiry_query = (By.XPATH, '//div[@aria-label="资产预算询价信息"]//label[text()="资产名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
inquiryinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
inquiryinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
inquiry_save = (By.XPATH, '//div[@aria-label="资产预算询价信息"]//button/span[contains(text(),"确定")]')

save = (By.XPATH, '//div[@aria-label="资产预算申报信息维护"]//button/span[contains(text(),"暂存")]')

confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')

Name = (By.XPATH, '//div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]//label[text()="计划名称"]/..//input')
query = (By.XPATH, '//div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]//label[text()="计划名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
submitinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]/i')
submitinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                     '/ancestor::tr//button[@title="提交"]/i[1]')

txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-yssb"]/span')





