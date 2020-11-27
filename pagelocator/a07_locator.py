from selenium.webdriver.common.by import By


open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
level3menu = (By.XPATH, '//span[text()="不相容角色维护"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01INCOMPATIBLE06"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
role_name = (By.XPATH, '//label[@for="incpRoleName"]/..//input')
role1_no = (By.XPATH, '//label[@for="role1No"]/..//i/..')
business_role_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="业务角色名称"]/..//input')
quer_button = (By.XPATH, '//div[@aria-label="业务角色信息"]//button/span[contains(text(),"查询")]')
informatio = (
    By.XPATH,
    '//div[@class="el-table__fixed"]//span[contains(text(),"内控")]/ancestor::tr//span[@class="el-radio__inner"]')
informatio1 = (
    By.XPATH,
    '//div[@class="el-table__fixed"]//span[contains(text(),"内控")]/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button_1 = (By.XPATH, '//div[@aria-label="业务角色信息"]//button/span[contains(text(),"确认")]')
business_role2_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="业务角色名称"]/..//input')
role2_no = (By.XPATH, '//label[@for="role2No"]/..//i/..')
query_button = (By.XPATH, '//div[@aria-label="业务角色信息"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"内控")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"内控")]'
                          '/ancestor::tr//span[@class="el-radio__inner"]')[0]
confirm_button = (By.XPATH, '//div[@aria-label="业务角色信息"]//button/span[contains(text(),"确认")]')
role_describe = (By.XPATH, '//label[@for="incpRoleDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="互斥规范"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01INCOMPATIBLE06"]/span')