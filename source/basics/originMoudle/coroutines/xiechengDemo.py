#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 22:51
# @Author  : Administrator
# @File    : xiechengDemo.py
# @Software: PyCharm
# @context : 协程(高并发时候使用,在操作IO时切换协程节省大量时间)


import time
import gevent
from greenlet import greenlet


# greenlet 切换之后不会再切换回来,单向的
def test1():
    print(123)
    gr2.switch()
    print(128)
    time.sleep(3)
    gr2.switch()
    print(145)


def test2():
    print(345)
    gr1.switch()
    time.sleep(7)
    print(456)


gr1 = greenlet(test1)  # 启动一个协程
gr2 = greenlet(test2)
gr1.switch()


# gevent优先选择io执行快的进行切换
def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')


def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo),  # 生成，
    gevent.spawn(bar),
    gevent.spawn(func3),
])
