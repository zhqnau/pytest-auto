from selenium.webdriver.common.by import By

doc1 = "选择菜单"
doc2 = "内控检查时限设置"
open1menu = (By.XPATH, '//i[@title="展开菜单"]')
level1menu = (By.XPATH, '//div[contains(text(),"内部控制子系统")]')
level2menu = (By.XPATH, '//span[text()="内控风险分析管理"]')
level3menu = (By.XPATH, '//span[text()="内控检查时限修改"]')
iframe = (By.XPATH, '//*[@id="pane-ICSB04TIMELIMITCHG12"]/div/iframe')
name = (By.XPATH, '//div[@class="hsa-row el-row"]//label[text()="业务环节名称"]/..//input')
query_button = (By.XPATH, '//div[@class="hsa-row el-row"]//button/span[contains(text(),"查询")]')
information = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="设置"]/i')
information1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//span[contains(text(),"SERVMAT")]'
                         '/ancestor::tr//button[@title="设置"]/i')[0]
warn_time = (By.XPATH, '//label[@for="warnTimelmt"]/..//input')
end_time = (By.XPATH, '//label[@for="endTimelmt"]/..//input')
save_button = (By.XPATH, '//div[@aria-label="时限修改"]//button/span[contains(text(),"保存")]')
confirm_button = (By.XPATH, '//div[@aria-label="请确认输入信息："]//button/span[contains(text(),"确定")]')
txt1 = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')
close = (By.XPATH, '//div[@id="tab-ICSB04TIMELIMITCHG12"]/span')





