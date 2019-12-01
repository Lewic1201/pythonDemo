#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 22:35
# @Author  : Lewic
# @File    : sumDemo.py
# @Software: PyCharm Community Edition

num_list = []
num = input('请输入数据:')
while True:
    if isinstance(num, float) or isinstance(num, int):
        num_list.append(num)
        print("和为" + str(sum(num_list)))
    else:
        print('输入格式有误,请重新输入')
    num = input('请再次输入数据:')
