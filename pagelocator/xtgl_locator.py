from selenium.webdriver.common.by import By
import win32con
import win32gui

doc0 = "结果检查"
doc1 = "选择菜单"
doc2 = "点击展开菜单按钮"


level1menu = (By.XPATH, '//div[contains(text(),"统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="系统管理"]')
level3menu = (By.XPATH, '//span[text()="组织机构管理"]')
level4menu = (By.XPATH, '//span[text()="用户管理"]')
level5menu = (By.XPATH, '//span[text()="资源管理"]')
level6menu = (By.XPATH, '//span[text()="菜单收藏夹"]')
level7menu = (By.XPATH, '//span[text()="子系统管理"]')
level8menu = (By.XPATH, '//span[text()="安全角色管理"]')
level9menu = (By.XPATH, '//span[text()="业务角色管理"]')
level10menu = (By.XPATH, '//span[text()="密码修改"]')
level11menu = (By.XPATH, '//span[text()="密码重置"]')
level12menu = (By.XPATH, '//span[text()="用户授权日志"]')
level13menu = (By.XPATH, '//span[text()="系统安全日志"]')
level14menu = (By.XPATH, '//span[text()="用户解锁管理"]')
level15menu = (By.XPATH, '//span[text()="资源权限查询"]')
level16menu = (By.XPATH, '//span[text()="用户权限查询"]')
level17menu = (By.XPATH, '//span[text()="个人信息修改"]')
level18menu = (By.XPATH, '//span[text()="用户角色授权管理"]')




openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')


iframe1 = (By.XPATH, '//*[@id="pane-ips-xtgl-zzjggl"]/div/iframe')
iframe2 = (By.XPATH, '//*[@id="pane-ips-xtgl-yhgl"]/div/iframe')
iframe3 = (By.XPATH, '//*[@id="pane-ips-xtgl-zygl"]/div/iframe')
iframe4 = (By.XPATH, '//*[@id="pane-ips-xtgl-cdscj"]/div/iframe')
iframe5 = (By.XPATH, '//*[@id="pane-ips-xtgl-zxtgl"]/div/iframe')
iframe6 = (By.XPATH, '//*[@id="pane-ips-xtgl-aqjsgl"]/div/iframe')
iframe7 = (By.XPATH, '//*[@id="pane-ips-xtgl-ywjsgl"]/div/iframe')
iframe8 = (By.XPATH, '//iframe[@class="iframe header-info-collapse"]')
iframe9 = (By.XPATH, '//*[@id="pane-ips-xtgl-yhsqrz"]/div/iframe')
iframe10 = (By.XPATH, '//*[@id="pane-ips-xtgl-xtaqrz"]/div/iframe')
iframe11 = (By.XPATH, '//*[@id="pane-ips-xtgl-zyqxcx"]/div/iframe')
iframe12 = (By.XPATH, '//*[@id="pane-ips-xtgl-yhqxcx"]/div/iframe')
iframe13 = (By.XPATH, '//*[@id="pane-ips-xtgl-grxxxg"]/div/iframe')
iframe14 = (By.XPATH, '//*[@id="pane-ips-xtgl-yhjssqgl"]/div/iframe')



close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

#组织机构管理
jd = (By.XPATH,'//span[contains(text(),"组织机构树")]/../../following-sibling::div[1]//div[@role="group"]/div[1]')
add = (By.XPATH,'//ul[@id="rightClickMenu"]//span[text()="新增"]')
orgTypeCode_list = (By.XPATH,'//label[@for="orgTypeCode"]/following-sibling::div[1]//input')
orgTypeCode_item = (By.XPATH,'//li[text()="经办机构"]/following-sibling::li//span[text()="部门"]')
input_uscc = (By.XPATH,'//label[@for="uscc"]/following-sibling::div[1]//input')#信用代码
input_orgCodg = (By.XPATH,'//label[@for="orgCodg"]/following-sibling::div[1]//input')#医保单位编码
admdvs_list = (By.XPATH,'//label[@for="admdvs"]/following-sibling::div[1]//input')#医保单位编码
admdvs_item = (By.XPATH,'//*[contains(@style,"position") and (@x-placement)][1]//span[text()="国家医疗保障局"]')
save_button= (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]//span[text()="保存"]')
#user_info=(By.XPATH,'//div[@class="hsa-title-pane-item__tab tabSelected"]')
user_info=(By.XPATH,'//div[@class="hsa-title-pane-item__tab"]')
add_button = (By.XPATH, '//div[@id="pane-menuTab"]//button[@type="button"]/span[text()="新增"]')
select_user = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]')
select_button = (By.XPATH,'//div[@aria-label="选择用户帐号"]//span[text()="选择"]')
conf_button = (By.XPATH,'//div[@aria-label="提示"]//button[2]')

#用户管理
add_button1 = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button/span')
person_id = (By.XPATH,'//*[contains(text(),"基础信息")]/../../following-sibling::div[1]//input[@placeholder="请输入证件号码查询"]')
user_name = (By.XPATH,'//*[contains(text(),"基础信息")]/../../following-sibling::div[1]//label[@for="userName"]/following-sibling::div//input[@placeholder="请输入"]')
phone_no = (By.XPATH,'//*[contains(text(),"基础信息")]/../../following-sibling::div[1]//label[@for="mob"]/following-sibling::div//input[@placeholder="请输入"]')
uact = (By.XPATH,'//*[contains(text(),"帐号信息")]/../../following-sibling::div[1]//label[@for="uact"]/following-sibling::div//input[@placeholder="只能包含字母、数字、_或者-"]')
pwd = (By.XPATH,'//*[contains(text(),"帐号信息")]/../../following-sibling::div[1]//label[@for="pwd"]/following-sibling::div//input[@placeholder="系统生成初始密码，可不录入"]')
orgunit_list = (By.XPATH,'//*[contains(text(),"帐号信息")]/../../following-sibling::div[1]//label[@for="orguntId"]/following-sibling::div//input[@placeholder="请选择"]')
orgunit_item = (By.XPATH,'//div[contains(@style,"transform-origin:") and (@role)]//span[text()="新国家医疗保障局"]')

#资源管理
zy_item = (By.XPATH,'//span[@class="custom-tree-node"]/span[2]/span[text()="菜单列表"]/ancestor::div[1]/following-sibling::div/div[1]/div[1]')
upload_button = (By.XPATH,'//span[text()="点击上传"]')
menucode = (By.XPATH,'//label[@for="resuCodg"]/following-sibling::div//input[@placeholder="请输入"]')
path_input = (By.XPATH,'//label[@for="resuPath" and text()="菜单路径"]/following-sibling::div//input[@placeholder="请输入"]')
save_button1 = (By.XPATH,'//span[contains(text(),"菜单维护")]/..//span[contains(text(),"保存")]')

#菜单收藏夹
add_button2 = (By.XPATH,'//span[contains(text(),"查询结果")]/..//span[contains(text(),"新增")]')
save_button2 = (By.XPATH,'//div[@aria-label="菜单"]//span[contains(text(),"保存")]')


#子系统管理
add_button3 = (By.XPATH,'//span[contains(text(),"新增")]')
subsysname = (By.XPATH,'//label[@for="subsysName"]/following-sibling::div//input[@placeholder="请输入"]')
subsysCodg = (By.XPATH,'//label[@for="subsysCodg"]/following-sibling::div//input[@placeholder="请输入"]')
sysPath = (By.XPATH,'//label[@for="sysPath"]/following-sibling::div//input[@placeholder="请输入"]')
save_button3 = (By.XPATH,'//div[@aria-label="子系统信息"]//span[contains(text(),"保存")]')


#安全角色管理
jd1 = (By.XPATH,'//span[contains(text(),"安全角色树")]/../../following-sibling::div[1]//div[@role="group"]/div[1]/../../div[1]//span[@class="custom-tree-node"]/span/span[1]')
save_button4 = (By.XPATH,'//span[contains(text(),"角色维护")]/following-sibling::div//span[text()="保存"]')
add1 =(By.XPATH,'//ul[@role="menubar"]//span[text()="新增"]')
add_admin = (By.XPATH,'//span[contains(text(),"管理员列表")]/following-sibling::div//span[text()="新增"]')
conf_button1 = (By.XPATH,'//div[@aria-label="提示"]//span[contains(text(),"确定")]')

#业务角色管理
add_button4 = (By.XPATH,'//span[contains(text(),"业务角色列表")]/following-sibling::div//span[text()="新增"]')#首页面的新增保存按钮
rolename_input = (By.XPATH,'//div[@aria-label="新增业务角色"]//label[@for="roleName" and text()="角色名称"]/following-sibling::div//input[@placeholder="请输入"]')#打开的窗口中的输入框定位
save_button5 = (By.XPATH,'//div[@aria-label="新增业务角色"]//span[contains(text(),"保存")]')#打开的窗口中的保存按钮定位
select_role = (By.XPATH,'//span[contains(text(),"选择业务角色")]/../../following-sibling::div//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')#主要页面上的单选列表勾选
add_button5 = (By.XPATH,'//span[contains(text(),"角色下帐号列表")]/following-sibling::div//span[text()="新增"]')
select_user1 = (By.XPATH,'//div[@aria-label="选择帐号"]//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]')#窗口中的多选框选择用户，修改窗口标题
select_button1 = (By.XPATH,'//div[@aria-label="选择帐号"]//span[text()="选择"]')

#用户授权日志
search_button = (By.XPATH,'//div[@id="pane-first"]//span[text()="查询"]')


#系统安全日志
search_button1 = (By.XPATH,'//div[@id="pane-lginTab"]//span[text()="查询"]')

#资源权限管理
search_button2 = (By.XPATH,'//span[text()="查询"]')

#修改个人信息
tel_edit = (By.XPATH,'//label[@for="tel"]/following-sibling::div[1]/div/input')
save_button6 = (By.XPATH,'//span[contains(text(),"保存")]')

#用户角色授权管理
search_button3 = (By.XPATH,'//span[text()="查询"]')
#search_button3 = (By.XPATH,'//div[@class="hsa-row__footbar"]/button[contains(@class,"primary")]/span[text()="查询"]')
select_user2 = (By.XPATH,'//div[contains(@class,"scrollable-y")]//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')
add_button6 = (By.XPATH,'//span[contains(text(),"角色信息")]/following-sibling::div//span[text()="新增"]')
select_user3 = (By.XPATH,'//div[@aria-label="查询业务角色"]//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]')
select_button2 = (By.XPATH,'//div[@aria-label="查询业务角色"]//span[text()="选择"]')



# #项目发布
# add_button = (By.XPATH, '//*[text()="新增"]')
# input_projNo = (By.XPATH,'//label[@for="projNo"]/following-sibling::div[1]//input[@placeholder="请输入"]')
# input_projName = (By.XPATH,'//label[@for="projName"]/following-sibling::div[1]//input[@placeholder="请输入"]')
# projType_list = (By.XPATH,'//label[@for="projType"]/following-sibling::div[1]//input[@placeholder="请选择"]')
# projType_item = (By.XPATH,'//div[@x-placement="bottom-start"]//li/span[text()="基础医学"]')
# fundBudgAmt = (By.XPATH,'//label[@for="fundBudgAmt"]/following-sibling::div[1]//input[@placeholder="请输入"]')
# projCont = (By.XPATH,'//label[@for="projCont"]/following-sibling::div[1]/div/textarea[@placeholder="请输入"]')
# save_button = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/span/button[2]/span')
# #lcb_button = (By.XPATH, '//*[contains(@class,"el-table__fixed-right")]//tr//button[@title="里程碑"]')[0]
# lcb_button = (By.XPATH,'//div[@class="el-table__fixed-right"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[11]//button[@title="里程碑"]')
# mlteCont_input = (By.XPATH,'//label[@for="mlteCont"]/following-sibling::div[1]/div/textarea[@placeholder="请输入"]')
# upload_file = (By.XPATH,'//label[contains(text(),"里程碑文件")]/..//input[@placeholder]')
# data_input = (By.XPATH, '//label[@for="mlteTime"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
# nextm = (By.XPATH, '//button[@aria-label="下个月"]')
# firstday = (By.XPATH,'//div[@x-placement="bottom-start"]//tr[@class="el-date-table__row"]/td[@class="next-month"][last()]')[1]
# save_button1 = (By.XPATH, '//div[@aria-label="里程碑"]//span[text()="保存"]')
# # select_firstdata = (By.XPATH, '//*[contains(@class,"el-table--scrollable-y")]/div[4]//span[@class="el-radio__inner"]')[0]
# # select_firstdata = (By.XPATH,'//*[contains(text(),"11223344")]')[0]
# select_firstdata = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]/div[@class="cell"]')
# sub_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button/span[text()="提交"]')
# conf = (By.XPATH,'//div[@aria-label="操作提示"]//button[2]')
# fb_button = (By.XPATH,'//div[contains(@class,"el-table--scrollable-y")]//div[@class="el-table__fixed-right"]/div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[last()]//button[@title="发布"]')
# open_zj = (By.XPATH,'//label[@for="stdyPsnName"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
# input_zj = (By.XPATH,'//label[@for="profName"]/following-sibling::div[1]/div/input[@placeholder="请输入专家姓名"]')
# serach_zj = (By.XPATH,'//label[@for="profName"]/../../following-sibling::div[1]//span[text()="查询"]')
# chose_zj = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed"]//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')
# save_button2 = (By.XPATH,'//span[text()="确 定"]')
# serach_button = (By.XPATH,'//span[text()="查询"]')
# save_button3 = (By.XPATH,'//span[text()="保存"]')
# save_button4 = (By.XPATH,'//div[@aria-label="操作提示"]//div[@class="el-message-box__btns"]/button[2]/span')
#
#
# #项目申报
# edit_button = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[12]//button[@title="编辑"]')
# chosefile_button= (By.XPATH,'//input[@placeholder="选择文件"]')
# data_input1 = (By.XPATH, '//label[@for="upldTime"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
# save_button5 = (By.XPATH, '//div[@aria-label="项目里程碑"]/div[3]//span[text()="保存"]')
#
# #项目结题申请
# XMno_input = (By.XPATH,'//label[text()="项目编号"]/../div[@class="el-form-item__content"]//input[@placeholder="请输入"]')
# XMna_input = (By.XPATH,'//label[text()="项目名称"]/../div[@class="el-form-item__content"]//input[@placeholder="请输入"]')
#
# sub_button1 = (By.XPATH,'//span[text()="提交"]')
# edit_button1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[18]//button[@title="编辑"]')
#
# #项目结题评审
# expert_button = (By.XPATH,'//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[19]//button[@title="确认专家"]')
# expert_add_button = (By.XPATH,'//span[text()="添加专家"]')
# expert_name = (By.XPATH,'//label[@for="profName"]/following-sibling::div[1]/div/input[@placeholder="请输入专家姓名"]')
# serach_expert = (By.XPATH,'//div[@aria-label="专家选择"]//span[text()="查询"]')
# #chose_expert = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed-body-wrapper"]//span[@class="el-radio__inner"]')[0]
# conf_button = (By.XPATH,'//span[text()="确 定"]')
# chose_expert = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed"]//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')
# close_button = (By.XPATH,'//div[@aria-label="专家抽取"]/div/button/i')
# edit_button2 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[19]//button[@title="编辑"]')
# ps_list = (By.XPATH,'//label[@for="rewRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
# ps_result = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="通过"]')
# ps_info = (By.XPATH,'//label[@for="rewOpnn"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
# save_button6 = (By.XPATH, '//div[@aria-label="项目评审"]/div[@class="el-dialog__footer"]//span[text()="保存"]')
# conf_button1 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')
#
# #项目结题审批
# sp_button = (By.XPATH,'//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr[1]/td[17]//button[@title="审批"]')
# sp_list = (By.XPATH,'//label[@for="apprRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
# sp_result = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="通过"]')
# sp_info = (By.XPATH,'//label[@for="apprOpnn"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
# save_button7 = (By.XPATH, '//div[@aria-label="项目审批"]/div[@class="el-dialog__footer"]//span[text()="保存"]')
# conf_button2 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')
#
# #项目成果
# edit_button3 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[8]//button[@title="编辑"]')
# save_button8 = (By.XPATH, '//div[@aria-label="项目成果信息表"]/div[3]//span[text()="保存"]')
# conf_button3 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')