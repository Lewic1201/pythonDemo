#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 23:35
# @Author  : Lewic
# @File    : Demo_007.py
# @Software: PyCharm

a = [1,2,3]
b = [2,3,4]

result = a

for i in b:
    if i not in a:
        result.append(i)
else:
    print(result)