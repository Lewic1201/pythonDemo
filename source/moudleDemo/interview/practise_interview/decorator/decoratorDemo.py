#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 12:00
# @Author  : Lewic
# @File    : decoratorDemo.py
# @Software: PyCharm Community Edition

from functools import wraps


def print_io(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("函数的输入：{}".format(*args, **kwargs))
        ret = func(*args, **kwargs)
        print("函数的输出：{}".format(ret))
        return ret

    return inner


@print_io
def test1(a):
    print 'test1:'+str(a)
    return str(a)[0]

test1(range(10))
