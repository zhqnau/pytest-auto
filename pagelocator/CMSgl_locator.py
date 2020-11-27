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
level2menu = (By.XPATH, '//span[text()="CMS管理"]')
level3menu = (By.XPATH, '//span[text()="CMS模板编辑"]')
level4menu = (By.XPATH, '//span[text()="CMS模板审批"]')
level5menu = (By.XPATH, '//span[text()="CMS栏目编辑"]')
level6menu = (By.XPATH, '//span[text()="CMS栏目审批"]')
level7menu = (By.XPATH, '//span[text()="CMS栏目内容编辑"]')
level8menu = (By.XPATH, '//span[text()="CMS栏目内容审批"]')
#level4menu = (By.XPATH, '//span[text()="通讯录组维护"]')
#level4menu = (By.XPATH, '//*[contains(text(),"通讯录组维护")]')
openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')

#iframe = (By.XPATH, '//*[@id="pane-ICSB01SERVMATT000001"]/div/iframe')
iframe1 = (By.XPATH, '//*[@id="pane-ips-cms-mbbj"]/div/iframe')
iframe2 = (By.XPATH, '//*[@id="pane-ips-cms-mbsp"]/div/iframe')
iframe3 = (By.XPATH, '//*[@id="pane-ips-cms-lmbj"]/div/iframe')
iframe4 = (By.XPATH, '//*[@id="pane-ips-cms-lmsp"]/div/iframe')
iframe5 = (By.XPATH, '//*[@id="pane-ips-cms-lmnrbj"]/div/iframe')
iframe6 = (By.XPATH, '//*[@id="pane-ips-cms-lmnrsp"]/div/iframe')
iframe7 = (By.XPATH, '//iframe[@class="iframe"]')
close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

#CMS模板编辑
add_button = (By.XPATH, '//div[@class="hsa-title-pane-item__toolbar"]/button/span[text()="新增"]')
search_button = (By.XPATH, '//span[text()="查询"]')
input_title = (By.XPATH,'//label[@for="tmplTtl"]/following-sibling::div[1]//input[@placeholder="请输入"]')
save_button = (By.XPATH,'//*[text()="暂存"]')
# select_firstdata = (By.XPATH, '//*[contains(@class,"el-table--scrollable-y")]/div[4]//span[@class="el-radio__inner"]')[0]
# select_firstdata = (By.XPATH,'//*[contains(text(),"11223344")]')[0]
select_firstdata = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]/div[@class="cell"]')
sub_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button/span[text()="提交"]')
conf = (By.XPATH,'//div[@aria-label="操作提示"]//button[2]')


#CMS模板审批
sp_button = (By.XPATH,'//*[contains(@class,"el-table__fixed-right")]//div[text()="1"]/ancestor::tr//button[@title="审批"]')
sp_list = (By.XPATH,'//label[@for="apprRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
sp_tg = (By.XPATH,'//li[1]/span[text()="通过"]')
save_button1 = (By.XPATH,'//*[@id="app"]/div/div[4]/div/div[3]/span/div/button[2]/span')

#CMS栏目编辑
add_button2 = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button[3]/span[text()="新增父级标题"]')
input_text2 = (By.XPATH,'//label[@for="colTtl"]/following-sibling::div[1]/div/input')
save_button2 = (By.XPATH, '//span[text()="暂 存"]')
select_newdata2 = (By.XPATH,'//div[@class="custom-tree-container"]/div/div[2]/div/div[last()-1]')
sub_button2 = (By.XPATH, '//*[text()="提交"]')

#CMS栏目审批
sp_button3 = (By.XPATH,'//*[contains(@class,"el-table__fixed-right")]//div[text()="1"]/ancestor::tr/td[8]/div[@class="cell"]')

#CMS栏目审批
#select_title = (By.XPATH,'//div/input[@placeholder="输入标题名称"]/../../div[2]/div/div/div[2]/div[last()]')[1]
select_title = (By.XPATH,'//div[@class="custom-tree-container"]/div/div[2]/div[last()]/div[1]/div[2]/div[1]')
add_button3 = (By.XPATH, '//*[text()="新增"]')
#mould_list = (By.XPATH,'//label[@for="tmplIfo"]/following-sibling::div[1]//input[@placeholder="请选择"]')
mould_list = (By.XPATH,'//label[@for="tmplIfo"]/following-sibling::div[1]//i')
mould_item = (By.XPATH,'//span[text()="新闻模板"]')
input_text3 = (By.XPATH,'//label[@for="contTtl"]/following-sibling::div[1]//input[@placeholder="请输入"]')
save_button3 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div[3]/span/div/button[2]/span')
select_newdata3 = (By.XPATH, '//*[contains(@class,"el-table__fixed")]//div[text()="1"]/ancestor::tr/td[1]/div[@class="cell"]')[0]
sub_button4 = (By.XPATH, '//*[text()="提交"]')
conf_button5 = (By.XPATH,'//div[@class="el-message-box__content"]/following-sibling::div/button[2]/span')
