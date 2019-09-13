#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 21:26
# @Author  : Administrator
# @File    : lineReversed.py
# @Software: PyCharm
# @context : 文件行倒序
import datetime


def get_now_time(formats='%Y%m%d%H%M%S'):
    now_time = datetime.datetime.now().strftime(formats)
    return now_time


def reversed_row(input_file='input.txt', output_file=None):
    with open(input_file, 'r', encoding='utf8') as inf:
        lines = inf.readlines()
        lines.append('')
        reverse_lines = lines[::-2]

    if output_file is None:
        output_file = './output/' + get_now_time() + '.txt'
    #
    # for i in range(len(reverse_lines))[::-1]:
    #     if not reverse_lines[i]:
    #         reverse_lines.pop(i)
    #     if reverse_lines[i][-1] != '\n':
    #         reverse_lines[i] += '\n'

    with open(output_file, 'w') as ouf:
        ouf.writelines(reverse_lines)


if __name__ == '__main__':
    reversed_row()
