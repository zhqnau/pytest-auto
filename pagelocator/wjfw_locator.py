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
level2menu = (By.XPATH, '//span[text()="文件服务"]')
level3menu = (By.XPATH, '//span[text()="文件管理"]')
level4menu = (By.XPATH, '//span[text()="被分享文件"]')

openmenu = (By.XPATH, '//i[@title="展开菜单"]')
openedmenu = (By.XPATH, '//span[text()="收起"]')

iframe1 = (By.XPATH, '//*[@id="pane-ips-wjfw-wjgl"]/div/iframe')
iframe2 = (By.XPATH, '//*[@id="pane-ips-wjfw-bfxwj"]/div/iframe')

#iframe7 = (By.XPATH, '//iframe[@class="iframe"]')
close = (By.XPATH, '//span[@class="el-icon-close"]')
txt = (By.XPATH, '//div[@id="app"]/following-sibling::div[@role="alert"]/p')

#文件服务
upload_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button[1]/span')
download_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button[2]/span')
share_button = (By.XPATH,'//div[@class="hsa-title-pane-item__toolbar"]/button[3]/span')
select_firstdata = (By.XPATH,'//div[@class="el-table__fixed"]/div[@class="el-table__fixed-body-wrapper"]/table[@class="el-table__body"]/tbody/tr[1]/td[1]/div[@class="cell"]')
djupload = (By.XPATH,'//em[text()="点击上传"]')
start_upload = (By.XPATH,'//span[text()="开始上传"]')
select_firstperson = (By.XPATH,'//div[@aria-label="分享列表"]//div[@class="el-table__fixed-body-wrapper"]//tr[1]//span[@class="el-checkbox__inner"]')
#(By.XPATH,'//*[contains(@class,"el-table--scrollable-y")]//div[@class="el-table__fixed"]//div[text()="1"]')[1]
conf = (By.XPATH,'//div[@aria-label="分享列表"]//div[@class="el-dialog__footer"]/span/button[2]')


