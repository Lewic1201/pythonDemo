#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:00
# @Author  : Administrator
# @File    : nc_saolei.py
# @Software: PyCharm
# @context : https://ac.nowcoder.com/acm/problem/16491

"""
扫雷

input:
3 3
*??
???
?*?
output:
*10
221
1*1

input:
2 3
?*?
*??
output:
2*1
*21

"""


def get_param():
    row_col = input("请输入行列(空格分隔):\n")

    row, col = row_col.split(' ')
    row = int(row)
    col = int(col)

    matrix = []
    for i in range(row):
        matrix.append(list(input()))
    return matrix, row, col


def get_mine_count(x, y, matrix, row, col):
    if matrix[x][y] == '*':
        return '*'
    count = 0

    if x - 1 >= 0:
        if y - 1 >= 0:
            if matrix[x - 1][y - 1] == '*':
                count += 1
        if matrix[x - 1][y] == '*':
            count += 1
        if y + 1 < col:
            if matrix[x - 1][y + 1] == '*':
                count += 1
    if y - 1 >= 0:
        if matrix[x][y - 1] == '*':
            count += 1
    if y + 1 < col:
        if matrix[x][y + 1] == '*':
            count += 1
    if x + 1 < row:
        if y - 1 >= 0:
            if matrix[x + 1][y - 1] == '*':
                count += 1
        if matrix[x + 1][y] == '*':
            count += 1
        if y + 1 < col:
            if matrix[x + 1][y + 1] == '*':
                count += 1

    return str(count)


def calc(matrix, row, col):
    ret = ''
    for i in range(row):
        for j in range(col):
            ret += get_mine_count(i, j, matrix, row, col)
        ret += '\n'
    print(ret)
    return ret


if __name__ == '__main__':
    calc(*get_param())
