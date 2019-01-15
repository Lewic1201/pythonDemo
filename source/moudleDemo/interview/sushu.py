#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 23:39
# @Author  : Administrator
# @File    : sushu.py
# @Software: PyCharm
# @context :
import math


def 素数判定(数字):
    if 数字<2:
        return False
    elif 数字==2:
        return True

    for i in range(2,int(math.sqrt(数字))+1):
        if 数字 % i == 0:
            return False
    else:
        return True

for j in range(100):
    if 素数判定(j):
        print(j,end=' ')
