from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "展现主题设置"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="展现主题设置"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04SUBJECTSET0008"]/div/iframe')
add_button = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
sbj_name = (By.XPATH, '//label[@for="sbjName"]/..//input')
sbj_describe = (By.XPATH, '//label[@for="sbjDscr"]/..//input')
data_source = (By.XPATH, '//label[@for="intctrlDataSouc"]/..//input')
source_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                         '//span[text()="风控中心"]')
configuration = (By.XPATH, '//label[@for="dispCfg"]/..//textarea')
parse_button = (By.XPATH, '//div[@aria-label="主题维护"]//button/span[contains(text(),"解 析")]')
save_button = (By.XPATH, '//div[@aria-label="主题维护"]//button/span[contains(text(),"保 存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04SUBJECTSET0008"]/span')







