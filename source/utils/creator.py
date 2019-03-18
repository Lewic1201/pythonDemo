#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:44
# @Author  : li_panfeng
# @File    : auto_queue.py
# @Software: PyCharm
# @context : 
import os


def create_queue_name(filename):
    """
    根据 所给文件名 生成 新的序列文件名
    """

    origin_name = os.path.abspath(filename)
    splitext = os.path.splitext(origin_name)
    suff = 0

    new_name = filename
    while True:
        if os.path.exists(new_name):
            suff += 1
            new_name = splitext[0] + '_' + str(suff) + splitext[1]
        else:
            print('new file: %s' % os.path.basename(new_name))
            return new_name


if __name__ == '__main__':
    create_queue_name('txt.123.312.txt')
