#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 12:09
# @Author  : Lewic
# @File    : dictDemo.py
# @Software: PyCharm Community Edition

d = {"k": 1, "v": 2}
print(d.items())

k = d.pop('k')
s = d.pop('s',None)

print(k)
print(d)
print(s)
print(d)
