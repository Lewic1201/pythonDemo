#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/12 23:40
# @Author  : Administrator
# @File    : setDemo.py
# @Software: PyCharm
# @context :


def prints(func):
    def wrapper(self, *args, **kwargs):
        try:
            print('-' * 100)
            print("[METHOD]: {}()".format(func.__name__))
            print("[INPUT]: ", *args)
            ret = func(self, *args, **kwargs)
            print("[RESULT]: ", ret)
            return ret
        except Exception as err:
            print(err)

    return wrapper


class Solution:

    @prints
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        input: 19
        return: true
        explain:
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
        """
        queue = []
        while True:
            nums = []
            next_num = 0
            while n // 10:
                nums.append(n % 10)
                n //= 10
            else:
                nums.append(n)
            for i in nums:
                next_num += i ** 2
            if next_num == 1:
                return True
            elif next_num in queue:
                return False
            else:
                n = next_num
                queue.append(next_num)


if __name__ == '__main__':
    ss = Solution()
    ss.isHappy(19)
    ss.isHappy(2)
