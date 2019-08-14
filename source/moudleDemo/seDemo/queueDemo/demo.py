#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 22:15
# @Author  : Administrator
# @File    : demo.py
# @Software: PyCharm
# @context :

import queue

a = queue.Queue()
a.put([1,'12',['a']])
a.put([2,'21',['v']])
print(a.get())
print(a.get())
print(a.get())


