from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "风险信息发布查询"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控综合管理"]')
level3menu = (By.XPATH, '//span[text()="风险信息发布查询"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB09RISKRLSQUERY04"]/div/iframe')
risk_title = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="风险发布标题"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB09RISKRLSQUERY04"]/span')








