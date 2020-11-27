import time
import datetime
'''
获取时间戳加在测试数据后避免数据唯一性导致运行失败
'''
t = time.time()

# print(t)                       # 原始时间数据
# print(int(t))                  # 秒级时间戳
# print(int(round(t * 1000)))    # 毫秒级时间戳
# print(int(round(t * 1000000)))  # 微秒级时间戳
nt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(nt)
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
dt1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
dt2 = datetime.datetime.now().strftime('%H%M%S')
dt3 = datetime.datetime.now().strftime('%H%M')
dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  # 含微秒的日期时间，来源 比特量化
# print(dt)
# print(dt_ms)
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
# print(ts)




