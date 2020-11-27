from selenium.webdriver.common.by import By

doc0 = "结果检查"
doc1 = "选择菜单"
doc2 = "点击展开菜单按钮"
doc3 = "录入备注信息"
doc4 = "保存通讯录备注"
doc5 = "点击通讯录组维护的新增按钮"
doc6 = "录入通讯录组名称"
doc7 = "点击通讯录组维护的新增用户"

level1menu = (By.XPATH, '//div[contains(text(),"内部统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="通讯录管理"]')
level3menu = (By.XPATH, '//span[text()="通讯录查询"]')
#level4menu = (By.XPATH, '//span[text()="通讯录组维护"]')
level4menu = (By.XPATH, '//*[contains(text(),"通讯录组维护")]')
openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')

#iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATT000001"]/div/iframe')
iframe1 = (By.XPATH, '//*[@id="pane-ips-txlgl-cx"]/div/iframe')#通讯录查询
iframe2 = (By.XPATH, '//*[@id="pane-ips-txlgl-wh"]/div/iframe')#通讯录组维护
element1 = (By.XPATH, '//*[@class="hsa-row__footbar"]//span[text()="查询"]')
element2 = (By.XPATH, '//*[contains(@class,"el-table__fixed-right")]//div[text()="1"]/ancestor::tr//button'
                              '[@title="编辑"]/i')
element3 = (By.XPATH, '//*[@class="el-textarea el-input--medium"]/textarea[@placeholder="请输入备注信息"]')
element4 = (By.XPATH, '//span[text()="保存"]')
element55 = (By.XPATH, '//div[@class="el-table__fixed"]//thead//span[@class="el-checkbox__inner"]')#新增通讯录选择一个人员
#element55 = (By.XPATH, '//div[@class="el-table__header-wrapper"]//thead//span[@class="el-checkbox__inner"]')#新增通讯录选择一个人员



addrbookGrpName = (By.XPATH,'//div[@aria-label="个人通讯录组"]//label[@for="addrbookGrpName"]/..//input') # 新增通讯录选择一个人员

element6 = (By.XPATH, '//div[@class="hsa-adaptive-container"]/div[5]/div[@aria-label="人员分配列表"]/div[@class="el-dialog__footer"]//button[2]')#通讯录组维护的暂存
element7 = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/span/button[2]/span')#通讯录组维护的保存

close = (By.XPATH, '//span[@class="el-icon-close"]')

add_button1 = (By.XPATH, '//*[contains(@class,"el-button el-button--success el-button--medium")]')#通讯录组维护新增1
add_button22 = (By.XPATH, '//div[@aria-label="个人通讯录组"]//*[contains(text(),"新增")]')#通讯录组维护新增2


element5 = (By.XPATH,'//*[contains(@class,"is-required")]//input[@placeholder="请输入"]')#通讯录组新增输入
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

