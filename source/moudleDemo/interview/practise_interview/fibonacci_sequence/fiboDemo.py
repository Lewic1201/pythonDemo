#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 22:29
# @Author  : Lewic
# @File    : fiboDemo.py
# @Software: PyCharm Community Edition

'''
1,1,2,3,5,8,13,21
'''


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        c = a + b
        a, b = b, c
    return a


def fibo2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo2(n - 1) + fibo2(n - 2)


def fibo3(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1


# print [fibo(i) for i in range(1, 11)]

print fibo2(6)
