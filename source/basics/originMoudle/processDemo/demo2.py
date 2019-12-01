#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 22:33
# @Author  : Administrator
# @File    : demo2.py
# @Software: PyCharm
# @context : 主进程与子进程queue之间的传递

import queue
import multiprocessing
import threading
from multiprocessing import Queue


def run():
    print(q.get())
    print("test")


def run2(qq):
    print(qq.get())
    print("test")


if __name__ == '__main__':
    q = queue.Queue()
    q.put([1, [22, 'a']])
    q.put([2, [33, 'c']])

    # # 1 父子进程queue传递,传入失败
    # p1 = multiprocessing.Process(target=run, )
    # p1.start()

    # # 2 父子进程queue传递,传入失败,未进行序列化
    # p1 = multiprocessing.Process(target=run2, args=(q,))
    # p1.start()

    # 3 父子进程queue传递,先进行序列化,然后进行反序列化
    q2 = Queue()
    q2.put([1, [22, 'a']])
    q2.put([2, [33, 'c']])
    p1 = multiprocessing.Process(target=run2, args=(q2,))
    p1.start()

    # # 父子线程 共享对象
    # t1 = threading.Thread(target=run, )
    # t1.start()

    print(q.get())
