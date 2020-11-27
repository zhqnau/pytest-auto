from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产折旧摊销"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产使用管理"]')
level4menu = (By.XPATH, '//span[text()="资产折旧摊销"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-zjtx"]/div/iframe')
aset_name = (By.XPATH, '//label[text()="资产名称"]/..//input')
deprStas = (By.XPATH, '//label[@for="deprStas"]/..//input')
deprStas_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="未折旧"]')
deprStas_list1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="已折旧"]')
aset_query = (By.XPATH, '//label[text()="资产名称"]/ancestor::form//button/span[contains(text(),"查询")]')
asetinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"水杯0925")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')
asetinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"水杯0925")]'
                         '/ancestor::tr//span[@class="el-checkbox__inner"]')[0]
depreciation = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"批量折旧")]')
dspoAlgo = (By.XPATH, '//label[@for="asetDeprFormEdit.dspoAlgo"]/..//input')
dspoAlgo_list = (By.XPATH, '//div[@id="app"]/following-sibling::div[@class="el-select-dropdown el-popper"]'
                                '//span[text()="年限平均法"]')
resr = (By.XPATH, '//label[@for="asetDeprFormEdit.resr"]/..//input')
deprBegntime = (By.XPATH, '//label[@for="asetDeprFormEdit.deprBegntime"]/..//input')
planUsedYears = (By.XPATH, '//label[@for="asetDeprFormEdit.planUsedYears"]/..//input')
memo = (By.XPATH, '//label[@for="memo"]/..//textarea')
plan_save = (By.XPATH, '//div[@aria-label="资产折旧信息维护"]//button/span[contains(text(),"暂存")]')
submit = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"批量提交")]')
confirm_button = (By.XPATH, '//div[@class="el-message-box__wrapper"]//button/span[contains(text(),"确定")]')


txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-zjtx"]/span')





