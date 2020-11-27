from selenium.webdriver.common.by import By

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
open1menu = (By.XPATH, '//i[@title="展开菜单"]')

level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
level3menu = (By.XPATH, '//span[text()="业务环节维护"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATTNODE02"]/div/iframe')
# 首页输入框及查询按钮，可以通用
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (
    By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
              '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (
    By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
              '/ancestor::tr//span[@class="el-radio__inner"]')[0]
add_button = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
matt_node_no = (By.XPATH, '//label[@for="servMattNodeNo"]/..//input')
matt_node_name = (By.XPATH, '//label[@for="servMattNodeName"]/..//input')
opt_time_lmt = (By.XPATH, '//label[@for="optTimelmt"]/..//input')
sus_cnt = (By.XPATH, '//label[@for="demdDspoSusptCnt"]/..//input')
task_cnt = (By.XPATH, '//label[@for="demdDspoTaskCnt"]/..//input')
node_dsc = (By.XPATH, '//label[@for="servMattNodeDscr"]/..//textarea')
# 弹出框界面，可以通用
save_button = (By.XPATH, '//div[@aria-label="服务事项环节信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01SERVMATTNODE02"]/span')