from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产监控管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产库存管理"]')
level4menu = (By.XPATH, '//span[text()="资产监控管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-jkgl"]/div/iframe')
aset_name = (By.XPATH, '//div[@id="app"]/div/div[@class="hsa-adaptive-pane hsa-adaptive-pane-fix"]'
                       '//label[text()="资产名称"]/..//input')
aset_query = (By.XPATH, '//label[text()="资产名称"]/ancestor::form//button/span[contains(text(),"查询")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//*[@id="tab-ips-zcgl-jkgl"]/span')






