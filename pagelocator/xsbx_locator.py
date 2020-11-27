from selenium.webdriver.common.by import By

doc0 = "结果检查"
doc1 = "选择菜单"
doc2 = "点击展开菜单按钮"

level1menu = (By.XPATH, '//div[contains(text(),"内部统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="线上报销"]')
level3menu = (By.XPATH, '//span[text()="线上填写电子单据"]')
level4menu = (By.XPATH, '//*[contains(text(),"一级审批")]')
level5menu = (By.XPATH, '//*[contains(text(),"二级审批")]')
level6menu = (By.XPATH, '//*[contains(text(),"报销卡维护")]')
level7menu = (By.XPATH, '//*[contains(text(),"报销核查")]')
level8menu = (By.XPATH, '//*[contains(text(),"报销查询")]')
openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')
close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

iframe1 = (By.XPATH, '//*[@id="pane-ips-xsbx-txdzdj"]/div/iframe')
iframe2 = (By.XPATH, '//*[@id="pane-ips-xsbx-yjsp"]/div/iframe')
iframe3 = (By.XPATH, '//*[@id="pane-ips-xsbx-ejsp"]/div/iframe')
iframe4 = (By.XPATH, '//*[@id="pane-ips-xsbx-yhxxwh"]/div/iframe')
iframe5 = (By.XPATH, '//*[@id="pane-ips-xsbx-bxhc"]/div/iframe')
iframe6 = (By.XPATH, '//*[@id="pane-ips-xsbx-bxcx"]/div/iframe')
iframe7 = (By.XPATH, '//iframe[@class="iframe"]')

#在线填写电子单据
add_button = (By.XPATH, '//div[@class="hsa-title-pane-item__toolbar"]//span[text()="新增"]')
pay_method_list = (By.XPATH, '//label[@for="paymtd"]/following-sibling::div//i')
pay_method_item = (By.XPATH,"//span[text()='现金']")
expense_list = (By.XPATH, '//label[@for="reimItem"]/following-sibling::div//i')
expense_item = (By.XPATH, "//span[text()='差旅费']")
save_button1 = (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[3]/span/div/button[2]/span')
save_button2 = (By.XPATH, "//span[text()='保存']")
conf_button1 = (By.XPATH,"//div[@class='el-message-box__btns']/button[2]")
expense_money = (By.XPATH,'//label[@for="billAmt"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
date_open = (By.XPATH,'//i[@class = "el-input__icon el-range__icon el-icon-date"]')
# start_date = (By.XPATH,'//i[@class = "el-input__icon el-range__icon el-icon-date"]/following-sibling::input')[0]
# end_date = (By.XPATH,'//i[@class = "el-input__icon el-range__icon el-icon-date"]/following-sibling::input')[1]
# date_chose = (By.XPATH,'//body[@class="el-popup-parent--hidden"]//div[@x-placement="top-end"]//div[contains(@class,"is-left")]//tr[2]/td[1]')
date_chose = (By.XPATH,'//div[contains(@class,"is-left")]//tr[2]/td[1]')

cfd = (By.XPATH,'//label[contains(text(),"出发地")]/following-sibling::div/div')
cfd_1 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][1]//span[text()="北京市"]')
cfd_2 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][1]//span[text()="市辖区"]')
#cfd_3 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][1]//span[text()="东城区"]')

mdd = (By.XPATH,'//label[contains(text(),"目的地")]/following-sibling::div/div')
mdd_1 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][2]//span[text()="北京市"]')
mdd_2 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][2]//span[text()="市辖区"]')
#mdd_3 = (By.XPATH, '//*[contains(@style,"position") and (@x-placement)][2]//span[text()="东城区"]')

traffic = (By.XPATH,'//label[contains(text(),"交通工具")]/following-sibling::div/div')
traffic_1 = (By.XPATH,'//span[text()="火车"]')

close_button = (By.XPATH,'//*[@id="app"]/div/div[5]/div[1]/div[3]/span/div/button[1]')
data_chose = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]/div[@class="cell"]')
submit_button = (By.XPATH,'//*[text()="提交"]')
conf_button2 = (By.XPATH,'//div[@class="el-message-box__content"]/following-sibling::div/button[2]/span')

#一、二级审批
sp_button1 = (By.XPATH,'//div[contains(@class,"el-table--scrollable-x")]//div[@class="el-table__fixed-right"]//table[@class="el-table__body"]//tr[1]/td[last()]//button[@title="审批"]')
sp_list = (By.XPATH,'//*[contains(@class,"el-col-lg-8")]/div//input[@placeholder="请选择"]')
sp_item = (By.XPATH,'//div[@x-placement="bottom-start"]//span[text()="通过"]')
save_button3 =(By.XPATH,'//div[@aria-label="审批"]//span[text()="保存"]')

#报销核查
hc_button = (By.XPATH,'//div[contains(@class,"el-table--scrollable-x")]//div[@class="el-table__fixed-right"]//table[@class="el-table__body"]//tr[1]/td[last()]//button[@title="核查"]')
save_button4 =(By.XPATH,'//div[@aria-label="报销核查"]//span[text()="保存"]')

#报销卡维护
bank_list = (By.XPATH,'//label[@for="bankName"]/following-sibling::div[1]//input[@placeholder="请选择"]')
chosed_bank = (By.XPATH,'//li/span[text()="中国人民银行会计营业部门"]')
phone_no = (By.XPATH,"//label[@for='bankCode']/..//input[@placeholder='请输入']")
bank_no = (By.XPATH,"//label[@for='bankCardno']/..//input[@placeholder='请输入']")
save_button5 =(By.XPATH,'//div[@aria-label="银行信息表"]//span[text()="保存"]')

#报销查询
reset_button =(By.XPATH,'//span[text()="重置"]')
search_button =(By.XPATH,'//span[text()="查询"]')
close_button1 =(By.XPATH,'//span[text()="关 闭"]')
ck_button = (By.XPATH,'//div[contains(@class,"el-table--scrollable-x")]//div[@class="el-table__fixed-right"]//table[@class="el-table__body"]//tr[1]/td[last()]//button[@title="申请信息"]')
