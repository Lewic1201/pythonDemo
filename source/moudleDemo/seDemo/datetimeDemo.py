"""
时间模块用法

time是归类在Generic Operating System Services中，它提供的功能是更加接近于操作系统层面的。
python标准文档中，time 模块是围绕着 Unix Timestamp 进行的

datetime 比 time 高级了不少，可以理解为 datetime 基于 time 进行了封装，提供了更多实用的函数
"""
import datetime
import time

# 常用 ================================================================================
# 获取当前时间
datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

# 获取当前时间根据指定格式
datetime.datetime.now()

# 获取当前时间戳
time.time()

# 日期转时间戳
dt = '2018-01-01 10:40:30'
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))

# 时间戳转日期
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
# ====================================================================================


# 使用time模块，首先得到当前的时间戳
time.time()
# 1408066927.208922

# 将时间戳转换为时间元组 struct_time
time.localtime(time.time())
time.struct_time((2014, 8, 15, 9, 42, 20, 4, 227, 0))

# 格式化输出想要的时间
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 接上文，不加参数时，默认就是输出当前的时间
time.strftime('%Y-%m-%d %H:%M:%S')

# 当然也可以透过datetime模块来实现，如下：
t = time.time()
datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# 同时，也可以只使用datetime模块
datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


# 2.获取时间差，计算程序的执行时间等：
# 使用time模块：
def t():
    start = time.time()
    time.sleep(3)
    end = time.time()
    print(end - start)


t()

# 使用datetime模块：
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)
