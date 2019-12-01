#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 21:41
# @Author  : Administrator
# @File    : demo.py
# @Software: PyCharm
# @context :


import time
import threading
import multiprocessing
import os


# 获取进程信息
def get_info():
    info = {
        'name': __name__,
        # 获取父进程id
        'ppid': os.getppid(),
        # 获取当前进程id
        'pid': os.getpid(),
    }
    print(info)


def run2(b):
    print(time.time())
    time.sleep(3)
    get_info()
    print(b)


def run1(a):
    print(time.time())
    time.sleep(5)
    t2 = threading.Thread(target=run2, args=(10 + a,))
    get_info()
    t2.start()
    print(a)


if __name__ == '__main__':
    for i in range(2):
        get_info()
        p = multiprocessing.Process(target=run1, args=(i,))
        p.start()
        # p.join()
