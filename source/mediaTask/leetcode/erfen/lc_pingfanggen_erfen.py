#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 0:00
# @Author  : Administrator
# @File    : lc_pingfanggen_erfen.py
# @Software: PyCharm
# @context :
'''
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

'''


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        queue = range(1, x + 1)
        left, right = 0, x - 1

        while left <= right:
            mid = (left + right) // 2
            if queue[mid] * queue[mid] == x:
                return queue[mid]
            elif queue[mid] * queue[mid] > x:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return mid


if __name__ == '__main__':
    print(Solution().mySqrt(3))
