#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 23:56
# @Author  : Administrator
# @File    : toSolution.py
# @Software: PyCharm
# @context :
import sys

sys.setrecursionlimit(10000)

options = [i for i in 'abcd']

j = 0

res = []


def select(group):
    # 题号
    num = len(group)

    # 第二题确定
    if num == 4:
        if group[1] == 'a':
            return select(group + ['c'])
        elif group[1] == 'b':
            return select(group + ['d'])
        elif group[1] == 'c':
            return select(group + ['a'])
        elif group[1] == 'd':
            return select(group + ['b'])

    # 第五题确定
    if num == 5:
        if group[4] != group[5]:
            return

    if len(group) == 10:
        res.append(group)
        return
    num += 1
    return select(group + ['a']), select(group + ['b']), \
           select(group + ['c']), select(group + ['d'])


select([])
print(res)
