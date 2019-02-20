#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0:07
# @Author  : Administrator
# @File    : lc_other.py
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
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        示例 1:
        输入: [3,0,1]
        输出: 2
        示例 2:
        输入: [9,6,4,2,3,5,7,0,1]
        输出: 8
        """
        # nlen = len(nums)
        # for i in range(nlen):
        #     if i not in nums:
        #         return i
        # else:
        #     return nlen
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def generateParenthesis(self, n):
        """
        括号生成
        :type n: int
        :rtype: List[str]

        eg: n=3
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
        """
        ret = []
        # while n:
        #     tmp = n
        #     str1 = ''
        #
        #     while tmp:
        #         str1+='('

    @prints
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # nstr = bin(n)[2:]
        # ret = 0
        # print(nstr)
        # for i in nstr:
        #     if i is '1':
        #         ret += 1
        # return ret
        temp = n
        res = 0
        while (temp):
            res += temp % 2
            temp = temp // 2
        return res


if __name__ == '__main__':
    ss = Solution()
    # ss.missingNumber([3, 0, 1])
    # ss.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    # ss.missingNumber([0])
    # ss.missingNumber([])
    ss.hammingWeight(100)
