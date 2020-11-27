from selenium.webdriver.common.by import By
from pagedata.nk_data import NkData  # 引用此脚本对应的测试数据信息

from tools.timenum import ts

x = str(ts)
y = NkData.TestItemEventMaintenance[0][0]

level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="业务规范设置管理"]')
level3menu = (By.XPATH, '//span[text()="事项事件维护"]')
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB01INCOMPATIBLE07"]/div/iframe')
matt_name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="服务事项名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, f'//div[@class="el-table__fixed"]//span[contains(text(),"{y}")]'
                         '/ancestor::tr//span[@class="el-radio__inner"]')
information1 = (By.XPATH, '//div[@class="el-table__fixed"]//span[contains(text(),"SERVMAT")]'
                          '/ancestor::tr//span[@class="el-radio__inner"]')[0]
add_button = (By.XPATH, "//div[contains(@id,'el-collapse-head-')]/div/button")
evt_no = (By.XPATH, '//label[@for="servMattEvtNo"]/..//input')
evt_name = (By.XPATH, '//label[@for="servMattEvtName"]/..//input')
evt_describe = (By.XPATH, '//label[@for="servMattEvtDscr"]/..//textarea')
save_button = (By.XPATH, '//div[@aria-label="服务事项事件信息表"]//button/span[contains(text(),"保存")]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB01INCOMPATIBLE07"]/span')

print(type(y))
print(y)
print(information)