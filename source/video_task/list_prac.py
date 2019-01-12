#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 23:43
# @Author  : Administrator
# @File    : listDemo.py
# @Software: PyCharm
# @context :


product = [[1, 'iphone', 5800], [2, 'Mac Pro', 12000], [3, 'Starbuck Latte', 31], [4, 'Alex Pythn', 81],
           [5, 'Bike', 800]]

salary = input('input your salary:')
if salary.isdigit():
    salary = int(salary)
else:
    raise Exception
while True:
    for i in product:
        print(i)
    buy = input('please input you buy num:')
    if buy == 'q':
        break
    for i in product:
        if i[0] == int(buy):
            salary -= i[2]
    else:
        print('you balance:' + str(salary))

print('Thank')
