#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 20:19
# @Author  : Lewic
# @File    : pracDemo1.py
# @Software: PyCharm
# @params  : 擅长编程M,擅长算法N
# @description  :

# N = int(input("请输入N:"))
# while True:
#     if N >=1:
#         break
#     else:
#         N = int(input("请重新输入N:"))
#
# M = int(input("请输入M:"))
# while True:
#     if M <= 1000000000:
#         break
#     else:
#         M = int(input("请重新输入M:"))
#
# group_num = 0
#
# if M>=2*N:
#     group_num = M//2
#
# if M<2*N and 2*M>N:
#     group_num = (M+N)//3
#
# if 2*M<=N:
#     group_num = N//2
#
# print("最多组成%s组队伍"%str(group_num))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/6 20:19
# @Author  : Lewic
# @File    : pracDemo1.py
# @version : python3.7


# def abc(group_num):
#     print(group_num)
#     print(group_num)
#     print(group_num/0)
#     print(group_num)
#     print(group_num)
#     print(group_num)

NM = input("请输入N M(空格分隔,回车确定):")
while True:
    try:
        N = int(NM.split(' ')[0])
        M = int(NM.split(' ')[1])
    except Exception as e:
        print('error:' + e)
        NM = input("输入格式有误,请重新输入N:")
        continue
    if N >= 1 and M <= 100000000:
        break
    else:
        NM = input("输入大小不在范围,请重新输入N:")

group_num = 0

try:

    if M >= 2 * N:
        group_num = M // 2

    if M < 2 * N and 2 * M > N:
        group_num = (M + N) // 3


    if 2 * M <= N:
        group_num = N // 2

    # abc(group_num)
    #
    # print(group_num)
    # print(group_num)
    # print(group_num)
    # print(group_num)


except Exception:
    print('pppp')


