from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控风险询问答复"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控风险询问答复"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05SUSPTINQEVT002"]/div/iframe')
name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
riskinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"925")]'
                     '/ancestor::tr//button[@title="答复"]')
riskinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"925")]'
                      '/ancestor::tr//button[@title="答复"]')[0]
rsp_cont = (By.XPATH, '//label[@for="rspdCont"]/..//textarea')
confirm_button = (By.XPATH, '//div[@aria-label="询问答复"]//button/span[contains(text(),"确定")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05SUSPTINQEVT002"]/span')


