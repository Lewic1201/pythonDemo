# coding: utf-8
import random

data = [[1, 32, 45], [1, 32, 45], [1, 3412, 12], [1, 3412, 12], [1, 3412, 12], [1, 3412, 12]]

# 取出每个月随机的几天
result_data = []
for mon in range(36):
    # month 月
    day_list = []
    while True:
        # j 每个月取的第j天
        day = random.randint(0, 29)
        if day not in day_list:
            day_list.append(day)
        if len(day_list) == 10:
            break
    for day in day_list:
        result_data.append(data[(mon * 30 + day) * 24:(mon * 30 + day) * 24 + 24])
