import os
'''
获取项目在使用机器中的目录
在定义程序运行目录
'''

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir)
logs_dir = os.path.join(base_dir, r"OutPuts\logs")
# print(logs_dir)
screenshot_dir = os.path.join(base_dir, r'OutPuts\screenshot')
# print(screenshot_dir)
# log_path1 = os.path.normpath(logs_dir)
# print(log_path1)
data_dir = os.path.join(base_dir, 'data')
# print(data_dir)
ini_path = os.path.join(base_dir, 'data', 'config.ini')
# print(ini_path)
lib_dir = os.path.join(base_dir, 'lib')
# print(lib_dir)
report_dir = os.path.join(base_dir, r'OutPuts\report')
# print(report_dir)
tests_dir = os.path.join(base_dir, 'test_case')
# print(tests_dir)
db_dir = os.path.join(base_dir, 'data', 'db_data.yaml')

