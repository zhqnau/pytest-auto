# pytest框架介绍


### 简介

本框架基于Python+selenium+pytest+allure组成，用户以Page Object的模式编写用例。元素的定位和操作按照页面划分，达到Web端自动化回归测试的目的，并生成测试报告。

### 运行日志

outputs/logs

### 失败截图

outputs/screenshot


### 效果展示

outputs/report/allure_report/index.html


### 快速上手


- 安装依赖包

python3.7.9 # python3.8有兼容性问题,

selenium  #　pip install selenium

Chromedriver # 根据谷歌浏览器版本自行下载http://npm.taobao.org/mirrors/chromedriver/   下载后放在Python根目录下

allure # allure-2.13.5可自行下载https://github.com/allure-framework/allure2/releases/tag/2.13.5  下载后解压环境变量将allure-2.13.5\bin配置在path下，cmd输入alllure验证是否成功

python依赖库：

先升级pip至最新
 pip install pytest
 pip install pytest-rerunfailures 用于当用例失败时，指定次数。用法：--reruns 3
 pip install pytest-xdist 用于并发执行。用法：-n 并发数，如果并发数为auto表示会自动根据CPU的数量设定并发数量。--dist=loadscope
 pip install allure-pytest  


##### 以下内容若已安装, 可跳过。

- 安装Python


  下载对应操作系统的Python版本并安装。

- 下载IDE(非必须)

  推荐Pycharm


- 安装必须的库

  目录中有install.py, 安装好Python之后, 在终端窗口中输入如下命令:

  Linux/mac: ```python3 install.py```

  windows: ```python install.py```

  注意: 安装时需要带上install.py路径或者进入该文件所在目录。


- Pycharm配置(若有)

  - 配置项目Python环境

    File->Open


   选择cspytest目录, 点击窗口右下角的Open


  打开Preferences, 在Project Interpreter里选择刚才安装Python的地址, 点击OK


 - IDE 配置 
	
	先在plugins 安装python community edition
	在配置Python环境
	在terminal中安装Python库，或者直接在标红的引用库下点击install

 -  运行用例
 运行之前先右键pagedata、pagelocator、pageobject、test_case、tools选择Mark Directory as Sources Root
 右击run.py, 选择Run则为运行模式, Debug则为调试模式
 若出现未引用库导致失败，鼠标放在标红的引用下根据提示install成功就可以了
 若出现utf-8编码失败，则换用其他编码方式例如：ansi



### 目录结构


```
project

|
└───data # 存放数据
|   |   config.ini # 测试项目地址，登录名密码验证码。   若无验证码则可去掉
|   |   nk_data.yaml # 测试文件无用
|
|	
└───lib # allure依赖
|
└───outputs
|   |   logs # 存放日志
|   |   screenshot # 存放截图
|   |   report # 存放allure报告
|   |   |  allure_raw #  allure报告依赖文件
|   |   |  allure_report #  allure报告，每次运行生成报告可通过文件夹中index.html打开
|   |   |  allure_results # 
|
└───pagedata # 存放脚本测试数据
|
└───pagelocator # 存放脚本xpath定位数据
|
└───pageobject #　存放登录脚本
|
└───testcase # 存放测试脚本。每个文件包含一个模块的测试脚本，测试文件以test开头命名，文件中测试类以Test开头命名，测试方法以test_开头命名。
|   |    conftest.py # 测试脚本配置
|   |    test_case.py # 测试脚本 
│   run.py # 运行脚本，自动收集testcase中测试脚本运行，并生成报告
|   pytest.ini # pytest配置
│   conftest.py # 项目整体配置
│   README.md


测试脚本编写方法可参照test_a01servicemain.py 脚本中有具体注释信息

```
#### 注: 以上目录结构/命名可能并不合理, 还望海涵。


 

  

  

  
