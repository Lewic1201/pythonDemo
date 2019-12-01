#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 23:46
# @Author  : Administrator
# @File    : demo4.py
# @Software: PyCharm
# @context : 进程之间共享数据用manager

import os
import time
from multiprocessing import Process
from multiprocessing import Manager


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


def son(d, l):
    d[os.getpid()] = time.time()
    l.append(os.getpid())


if __name__ == '__main__':
    with Manager() as manage:
        dict1 = manage.dict()
        list1 = manage.list()

        dict1[os.getpid()] = time.time()
        list1.append(os.getpid())

        process_list = []
        for i in range(5):
            p = Process(target=son, args=(dict1, list1))
            p.start()
            process_list.append(p)

        for pp in process_list:
            pp.join()

        print(dict1)
        print(list1)
