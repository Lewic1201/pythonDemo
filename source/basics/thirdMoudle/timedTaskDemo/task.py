#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: task
@time: 2019/7/4 10:00
@desc: reference: https://www.jianshu.com/p/b77d934cc252
"""
import time


def timer(n):
    """
    每n秒执行一次
    """
    while True:
        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        # TODO yourTask()  # 此处为要执行的任务
        time.sleep(n)
