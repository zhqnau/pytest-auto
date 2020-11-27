from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控任务结果查询"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="内控任务结果查询"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RESULTQUERY010"]/div/iframe')
timeks = (By.XPATH, '//label[@for="timeList"]/..//input[@placeholder="开始月份"]')
timejs = (By.XPATH, '//label[@for="timeList"]/..//input[@placeholder="结束月份"]')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RESULTQUERY010"]/span')








