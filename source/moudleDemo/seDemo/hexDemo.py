#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 23:26
# @Author  : Lewic
# @File    : hexDemo.py
# @Software: PyCharm


# bin(x) oct(x) int([number | string[, base]]) hex(x)
print(hex(12))

b = 0b1111011
o = 0o337
i = 19845
h = 0x1e2ab4


print(int(b))
print(int(str(b,encoding='unicode'),2))