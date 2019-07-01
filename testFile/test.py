import time


# t = time.time()
#
# print(t)  # 原始时间数据
# print(int(t))  # 秒级时间戳
# print(int(round(t * 1000)))  # 毫秒级时间戳
#
# sec = int(round(t * 1000) % 1000)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t))) + ".%sZ" % sec)  # 日期格式化
#
#
# def TimeStampToTime(timestamp, format='%Y-%m-%d %H:%M:%S'):
#     """把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12"""
#     timeStruct = time.localtime(timestamp)
#     return time.strftime(format, timeStruct)


def str_to_timestamp(str_time=None, format='%Y-%m-%d %H:%M:%S'):
    if str_time:
        time_tuple = time.strptime(str_time, format)  # 把格式化好的时间转换成元祖
        result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
        return int(result)
    return int(time.time())


str1 = '2019-04-27 07:01:46.123Z'
time_tuple = time.strptime(str1[:-5], '%Y-%m-%d %H:%M:%S')  # 把格式化好的时间转换成元祖
result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
print(int(result))
