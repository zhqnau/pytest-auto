from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控指标上报"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="内控指标上报"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09INTCTRLKPI0007"]/div/iframe')
generate = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"生成")]')
timeListks = (By.XPATH, '//div[@aria-label="内控指标描述"]//label[@for="timeList"]/..//input[@placeholder="开始月份"]')
timeListjs = (By.XPATH, '//div[@aria-label="内控指标描述"]//label[@for="timeList"]/..//input[@placeholder="结束月份"]')
kpiRpupTtl = (By.XPATH, '//div[@aria-label="内控指标描述"]//label[@for="kpiRpupTtl"]/..//input')
kpiRpupCont = (By.XPATH, '//div[@aria-label="内控指标描述"]//label[@for="kpiRpupCont"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="内控指标描述"]//button/span[contains(text(),"保存")]')
timeks = (By.XPATH, '//label[@for="timeList"]/..//input[@placeholder="开始月份"]')
timejs = (By.XPATH, '//label[@for="timeList"]/..//input[@placeholder="结束月份"]')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
kpiinf = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="上报"]')
kpiinf1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="上报"]')[0]
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09INTCTRLKPI0007"]/span')






