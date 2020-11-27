from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产折旧摊销审核"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产折旧摊销审核"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-zjtxsp"]/div/iframe')
submituser_name = (By.XPATH, '//label[text()="提交人"]/..//input')
submituser_query = (By.XPATH, '//label[text()="提交人"]/ancestor::form//button/span[contains(text(),"查询")]')
approvalinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"测试二")]'
                     '/ancestor::tr//button[@title="审批"]/i')
approvalinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"测试二")]'
                     '/ancestor::tr//button[@title="审批"]/i[1]')

applstas = (By.XPATH, '//label[@for="applstas"]/..//input')
apprOpnn = (By.XPATH, '//label[@for="apprOpnn"]/..//textarea')
applstas_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                              '//span[text()="审批通过"]')

Save = (By.XPATH, '//div[@aria-label="资产折旧审批信息"]//button/span[contains(text(),"审批")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-zjtxsp"]/span')

