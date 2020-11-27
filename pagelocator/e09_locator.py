from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "内控佐证材料录入"
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控任务管理"]')
level3menu = (By.XPATH, '//span[text()="内控佐证材料录入"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB05EVIDMATL000009"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
mattinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
mattinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
increase = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
doc_type = (By.XPATH, '//label[@for="eviddocType"]/..//input')
type_list = (
By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]//span[text()="自传材料"]')
doc_name = (By.XPATH, '//label[@for="eviddocName"]/..//input')
doc_describe = (By.XPATH, '//div[@aria-label="佐证材料信息"]//label[@for="eviddocDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="佐证材料信息"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB05EVIDMATL000009"]/span')






