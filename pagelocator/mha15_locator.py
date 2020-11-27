from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产分配管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产评估管理"]')
level4menu = (By.XPATH, '//span[text()="违规处置"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-wgcz"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
volausername = (By.XPATH, '//label[@for="volaUserName"]/..//span/i')
volauser_name = (By.XPATH, '//label[text()="用户姓名"]/..//input')
volauser_query = (By.XPATH, '//label[text()="用户姓名"]/ancestor::form//button/span[contains(text(),"查询")]')
volauserinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
volauserinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"测试二")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
volauser_save = (By.XPATH, '//div[@aria-label="资产与人员关系信息"]//button/span[contains(text(),"确定")]')

volaRea = (By.XPATH, '//label[@for="volaRea"]/..//textarea')
dspoRslt = (By.XPATH, '//label[@for="dspoRslt"]/..//textarea')
memo = (By.XPATH, '//label[@for="memo"]/..//textarea')
Save = (By.XPATH, '//div[@aria-label="资产违规处置信息维护"]//button/span[contains(text(),"保存")]')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-wgcz"]/span')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')


