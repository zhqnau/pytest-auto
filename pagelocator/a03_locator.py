from selenium.webdriver.common.by import By


level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level3menu = (By.XPATH, '//span[text()="业务环节经办规则维护"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATTCHK003"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//span[@class="el-radio__inner"]')[0]
add_button = (By.XPATH, '//div[contains(@id,"el-collapse-head-")]/div/button')
chk_rule_id = (By.XPATH, '//label[@for="chkRuleId"]/..//input')
chk_rule_name = (By.XPATH, '//label[@for="chkRuleName"]/..//input')
chk_rule_node = (By.XPATH, '//label[@for="chkRuleDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="服务事项环节校验信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01SERVMATTCHK003"]/span')