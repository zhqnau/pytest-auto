from selenium.webdriver.common.by import By
import win32con
import win32gui

doc0 = "结果检查"
doc1 = "选择菜单"
doc2 = "点击展开菜单按钮"


level1menu = (By.XPATH, '//div[contains(text(),"内部统一门户子系统")]')
level2menu = (By.XPATH, '//span[text()="专项工作"]')
level3menu = (By.XPATH, '//span[text()="项目委托"]')
level4menu = (By.XPATH, '//span[text()="项目发布"]')
level5menu = (By.XPATH, '//span[text()="项目申报"]')
level6menu = (By.XPATH, '//span[text()="项目结题申请"]')
level7menu = (By.XPATH, '//span[text()="项目结题评审"]')
level8menu = (By.XPATH, '//span[text()="项目结题审批"]')
level9menu = (By.XPATH, '//span[text()="项目成果"]')
level10menu = (By.XPATH, '//span[text()="项目通用查询"]')

openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')


iframe1 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmfb"]/div/iframe')
iframe2 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmsb"]/div/iframe')
iframe3 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmjtsq"]/div/iframe')
iframe4 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmjtps"]/div/iframe')
iframe5 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmjtsp"]/div/iframe')
iframe6 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmcg"]/div/iframe')
iframe7 = (By.XPATH, '//*[@id="pane-ips-xmwt-xmtycx"]/div/iframe')
iframe8 = (By.XPATH, '//iframe[@class="iframe header-info-collapse"]')


close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

#项目发布
add_button = (By.XPATH, '//*[text()="新增"]')
input_projNo = (By.XPATH,'//label[@for="projNo"]/following-sibling::div[1]//input[@placeholder="请输入"]')
input_projName = (By.XPATH,'//label[@for="projName"]/following-sibling::div[1]//input[@placeholder="请输入"]')
projType_list = (By.XPATH,'//label[@for="projType"]/following-sibling::div[1]//input[@placeholder="请选择"]')
projType_item = (By.XPATH,'//div[@x-placement="bottom-start"]//li/span[text()="基础医学"]')
fundBudgAmt = (By.XPATH,'//label[@for="fundBudgAmt"]/following-sibling::div[1]//input[@placeholder="请输入"]')
projCont = (By.XPATH,'//label[@for="projCont"]/following-sibling::div[1]/div/textarea[@placeholder="请输入"]')
save_button = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/span/button[2]/span')
#lcb_button = (By.XPATH, '//*[contains(@class,"el-table__fixed-right")]//tr//button[@title="里程碑"]')[0]
lcb_button = (By.XPATH,'//div[@class="el-table__fixed-right"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[11]//button[@title="里程碑"]')
mlteCont_input = (By.XPATH,'//label[@for="mlteCont"]/following-sibling::div[1]/div/textarea[@placeholder="请输入"]')
upload_file = (By.XPATH,'//label[contains(text(),"里程碑文件")]/..//input[@placeholder]')
data_input = (By.XPATH, '//label[@for="mlteTime"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
nextm = (By.XPATH, '//button[@aria-label="下个月"]')
firstday = (By.XPATH,'//div[@x-placement="bottom-start"]//tr[@class="el-date-table__row"]/td[@class="next-month"][last()]')[1]
save_button1 = (By.XPATH, '//div[@aria-label="里程碑"]//span[text()="保存"]')
# select_firstdata = (By.XPATH, '//*[contains(@class,"el-table--scrollable-y")]/div[4]//span[@class="el-radio__inner"]')[0]
# select_firstdata = (By.XPATH,'//*[contains(text(),"11223344")]')[0]
select_firstdata = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]/div[@class="cell"]')
sub_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button/span[text()="提交"]')
conf = (By.XPATH,'//div[@aria-label="操作提示"]//button[2]')
fb_button = (By.XPATH,'//div[contains(@class,"el-table--scrollable-y")]//div[@class="el-table__fixed-right"]/div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[last()]//button[@title="发布"]')
open_zj = (By.XPATH,'//label[@for="stdyPsnName"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
input_zj = (By.XPATH,'//label[@for="profName"]/following-sibling::div[1]/div/input[@placeholder="请输入专家姓名"]')
serach_zj = (By.XPATH,'//label[@for="profName"]/../../following-sibling::div[1]//span[text()="查询"]')
chose_zj = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed"]//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')
save_button2 = (By.XPATH,'//span[text()="确 定"]')
serach_button = (By.XPATH,'//span[text()="查询"]')
save_button3 = (By.XPATH,'//span[text()="保存"]')
save_button4 = (By.XPATH,'//div[@aria-label="操作提示"]//div[@class="el-message-box__btns"]/button[2]/span')


#项目申报
edit_button = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[12]//button[@title="编辑"]')
chosefile_button= (By.XPATH,'//input[@placeholder="选择文件"]')
data_input1 = (By.XPATH, '//label[@for="upldTime"]/following-sibling::div[1]/div/input[@placeholder="请输入"]')
save_button5 = (By.XPATH, '//div[@aria-label="项目里程碑"]/div[3]//span[text()="保存"]')

#项目结题申请
XMno_input = (By.XPATH,'//label[text()="项目编号"]/../div[@class="el-form-item__content"]//input[@placeholder="请输入"]')
XMna_input = (By.XPATH,'//label[text()="项目名称"]/../div[@class="el-form-item__content"]//input[@placeholder="请输入"]')

sub_button1 = (By.XPATH,'//span[text()="提交"]')
edit_button1 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[18]//button[@title="编辑"]')

#项目结题评审
expert_button = (By.XPATH,'//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[19]//button[@title="确认专家"]')
expert_add_button = (By.XPATH,'//span[text()="添加专家"]')
expert_name = (By.XPATH,'//label[@for="profName"]/following-sibling::div[1]/div/input[@placeholder="请输入专家姓名"]')
serach_expert = (By.XPATH,'//div[@aria-label="专家选择"]//span[text()="查询"]')
#chose_expert = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed-body-wrapper"]//span[@class="el-radio__inner"]')[0]
conf_button = (By.XPATH,'//span[text()="确 定"]')
chose_expert = (By.XPATH,'//div[@aria-label="专家选择"]//div[@class="el-table__fixed"]//div[@class="el-table__fixed-body-wrapper"]//tr[1]/td[1]')
close_button = (By.XPATH,'//div[@aria-label="专家抽取"]/div/button/i')
edit_button2 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[19]//button[@title="编辑"]')
ps_list = (By.XPATH,'//label[@for="rewRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
ps_result = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="通过"]')
ps_info = (By.XPATH,'//label[@for="rewOpnn"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
save_button6 = (By.XPATH, '//div[@aria-label="项目评审"]/div[@class="el-dialog__footer"]//span[text()="保存"]')
conf_button1 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')

#项目结题审批
sp_button = (By.XPATH,'//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr[1]/td[17]//button[@title="审批"]')
sp_list = (By.XPATH,'//label[@for="apprRslt"]/following-sibling::div[1]//input[@placeholder="请选择"]')
sp_result = (By.XPATH, '//div[@x-placement="bottom-start"]//span[text()="通过"]')
sp_info = (By.XPATH,'//label[@for="apprOpnn"]/following-sibling::div[1]//textarea[@placeholder="请输入"]')
save_button7 = (By.XPATH, '//div[@aria-label="项目审批"]/div[@class="el-dialog__footer"]//span[text()="保存"]')
conf_button2 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')

#项目成果
edit_button3 = (By.XPATH, '//div[@class="el-table__fixed-right"]//div[text()="1"]/ancestor::tr/td[8]//button[@title="编辑"]')
save_button8 = (By.XPATH, '//div[@aria-label="项目成果信息表"]/div[3]//span[text()="保存"]')
conf_button3 = (By.XPATH,'//div[@class="el-message-box__btns"]/*[contains(@class,"el-button--primary")]')