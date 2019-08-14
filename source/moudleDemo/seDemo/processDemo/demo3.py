#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 23:19
# @Author  : Administrator
# @File    : demo3.py
# @Software: PyCharm
# @context : 管道传递父子进程间的数据

import os
from multiprocessing import Process, Pipe


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


def son(child):
    get_info()
    print('child-recv:', child.recv())
    child.send('ilu,father')
    child.send('ilu2,father')
    child.send('ilu3,father')


if __name__ == '__main__':
    get_info()
    parent, child = Pipe()
    p = Process(target=son, args=(child,))
    p.start()
    p.join()
    parent.send("ilu,son")
    while True:
        print(parent.recv())
