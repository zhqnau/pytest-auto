from selenium.webdriver.common.by import By

open1menu = (By.XPATH, '//i[@title="展开菜单"]')
doc1 = "选择菜单"
doc2 = "资产预算询价管理"
level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="资产管理"]')
level3menu = (By.XPATH, '//span[text()="资产预算管理"]')
level4menu = (By.XPATH, '//span[text()="资产预算询价管理"]')
iframe = (By.XPATH, '//*[@id="pane-ips-zcgl-ysxj"]/div/iframe')
add_button = (By.XPATH, '//div[@role="tab"]//button/span[contains(text(),"新增")]')
purcPlanName = (By.XPATH, '//label[@for="purcPlanName"]/..//input')
planName = (By.XPATH, '//div[@aria-label="购置计划明细信息"]//label[text()="计划名称"]/..//input')
plan_query = (By.XPATH, '//div[@aria-label="购置计划明细信息"]//label[text()="计划名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
planinf = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
planinf1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
plan_save = (By.XPATH, '//div[@aria-label="购置计划明细信息"]//button/span[contains(text(),"确定")]')

spler_name = (By.XPATH, '//div[@aria-label="供应商信息"]//label[text()="供应商名称"]/..//input')
spler_query = (By.XPATH, '//div[@aria-label="供应商信息"]//label[text()="供应商名称"]'
                        '/ancestor::form//button/span[contains(text(),"查询")]')
# xx = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/section[1]'
#                 '/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span[1]/span')

splerinf = (By.XPATH, '//div[@aria-label="供应商信息"]//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
splerinf1 = (By.XPATH, '//div[@aria-label="供应商信息"]//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')[0]
splerName = (By.XPATH, '//label[@for="splerName"]/..//input')
spler_save = (By.XPATH, '//div[@aria-label="供应商信息"]//button/span[contains(text(),"确定")]')

# gys = (By.XPATH, '/html/body/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/section[1]'
#                  '/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span[1]/span')
# dQDGys = (By.XPATH, '//div[@aria-label="供应商信息"]/div[2]/div/div[3]/div/div/div/div/div/div/button')
bradMol = (By.XPATH, '//label[@for="bradMol"]/..//input')
rpupPric = (By.XPATH, '//label[@for="rpupPric"]/..//input')
save = (By.XPATH, '//div[@aria-label="资产询价信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ips-zcgl-ysxj"]/span')



