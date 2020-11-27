from selenium.webdriver.common.by import By


level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
level3menu = (By.XPATH, '//span[text()="服务事项维护"]')
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATT000001"]/div/iframe')
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
ser_matt_no = (By.XPATH, '//label[@for="servMattNo"]/..//input')
ser_matt_name = (By.XPATH, '//label[@for="servMattName"]/..//input')
sub_sys_id = (By.XPATH, '//label[@for="subsysId"]/..//i/..')
sub_system_name = (By.XPATH, '//div[@aria-label="子系统信息"]//label[text()="子系统名称"]/..//input')
query_button = (By.XPATH, '//div[@aria-label="子系统信息"]//button/span[text()="查询"]')





information = (
    By.XPATH,
    '//div[@class="el-table__fixed"]//span[contains(text(),"内部控制")]/ancestor::tr//span[@class="el-radio__inner"]'
)
information1 = (
    By.XPATH,
    '//div[@class="el-table__fixed"]//span[contains(text(),"内部控制")]/ancestor::tr//span[@class="el-radio__inner"]')[0]

confirm_button = (By.XPATH, '//div[@aria-label="子系统信息"]//button/span[contains(text(),"确认")]')
opt_time_lmt = (By.XPATH, '//label[@for="optTimelmt"]/..//input')
ser_matt_desc = (By.XPATH, '//label[@for="servMattDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="服务事项信息"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01SERVMATT000001"]/span')
