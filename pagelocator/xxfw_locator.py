from selenium.webdriver.common.by import By

doc0 = "结果检查"
doc1 = "选择菜单"
doc2 = "点击展开菜单按钮"
doc3 = "录入备注信息"
doc4 = "保存通讯录备注"
doc5 = "点击通讯录组维护的新增按钮"
doc6 = "录入通讯录组名称"
doc7 = "点击通讯录组维护的新增用户"

#站内消息服务
level1menu = (By.XPATH, '//div[contains(text(),"内部统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="消息服务"]')
level3menu = (By.XPATH, '//span[text()="站内消息服务"]')
level4menu = (By.XPATH, '//*[contains(text(),"短信消息服务")]')
level5menu = (By.XPATH, '//*[contains(text(),"短信消息审批")]')
openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')
close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

iframe1 = (By.XPATH, '//*[@id="pane-ips-xxfw-znxxfw"]/div/iframe')#站内消息服务
iframe2 = (By.XPATH, '//*[@id="pane-ips-xxfw-dxxxfw"]/div/iframe')#短信消息服务
iframe3 = (By.XPATH, '//*[@id="pane-ips-xxfw-dxxxsp"]/div/iframe')#短信消息审批

writemsg_button = (By.XPATH, '//div[@class="hsa-title-pane-item__toolbar"]//span[text()="写信"]')
input_title = (By.XPATH, '//label[@for="ttl"]/following-sibling::div[1]//input[@placeholder="请输入"]')
recpsn = (By.XPATH, '//div/form/div/div[2]/div/div/div/div/span/span/i')
input_msginfo = (By.XPATH,'//label[@for="cont"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
select_firstone = (By.XPATH,'//*[contains(text(),"通讯录列表")]/ancestor::p/following-sibling::div/div[@role="group"]/label[1]/span[@class="el-checkbox__input"]')
right_button = (By.XPATH,'//*[@id="pane-first"]/div/div/div[2]/button[2]/span/i')
confirm_button = (By.XPATH, '//div[@aria-label="收件人信息表"]/div[3]//span[1]/button[1]/span[text()="确定"]')
send_button = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/span/button[2]/span')

# 短信消息服务
writemsg_buttons = (By.XPATH, '//div[@class="hsa-title-pane-item__toolbar"]//span[text()="写信"]')
input_titles = (By.XPATH, '//label[@for="smsTtl"]/following-sibling::div[1]//input[@placeholder="请输入"]')
add_recpsns = (By.XPATH, '//div/button/span[text()="新增"]')
input_msginfos = (By.XPATH,'//label[@for="smsCont"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
select_firstones = (By.XPATH,'//*[@id="pane-first"]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
add_button = (By.XPATH,'//*[contains(text(),"查询结果")]/../div[1]/button[1]/span[1]')
confirm_buttons = (By.XPATH, '//*[@id="app"]/div/div[4]/div/div[3]/span/button[2]/span')
save_buttons = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/span/button[2]/span')
sub = (By.XPATH,'//*[contains(@class,"el-table__fixed-right")]//div[text()="1"]/ancestor::tr//button[@title="提交"]/i')
conf = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]/span')

# 短信消息审批
input_searchecase = (By.XPATH, '//label[text()="短信标题"]/../div[1]/div[1]/input[@placeholder="请输入"]')
search_button = (By.XPATH, '//span[text()="查询"]')
sp_button = (By.XPATH,'//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr[1]/td[9]//button[@title="审批"]')
sp_list = (By.XPATH,'//label[@for="apprRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
sptg_item = (By.XPATH,'//span[text()="通过"]')
finalsp_button = (By.XPATH,'//*[contains(@class,"el-dialog__footer")]//button[2]')

