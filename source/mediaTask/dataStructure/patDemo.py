#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 0:24
# @Author  : Administrator
# @File    : patDemo.py
# @Software: PyCharm
# @context :


str_input = input()

num_list = str_input.split(' ')

A = num_list[0]
DA = num_list[1]

result_A = A.count(DA) * DA

B = num_list[2]
DB = num_list[3]

result_B = B.count(DB) * DB

if result_A == '':
    result_A = 0
if result_B == '':
    result_B = 0

print(int(result_A) + int(result_B))

