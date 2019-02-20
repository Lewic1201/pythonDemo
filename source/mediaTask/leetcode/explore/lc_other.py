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

    @prints
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
        left = '('
        right = ')'
        lnum = 0
        rnum = 0

        str0 = ''

        def add(str0, lnum, rnum):
            if len(str0) == 2 * n:
                ret.append(str0)
                return str0
            if lnum < n:
                if lnum == rnum:
                    return add(str0 + left, lnum + 1, rnum)
                elif lnum > rnum:
                    return add(str0 + left, lnum + 1, rnum), add(str0 + right, lnum, rnum + 1)
            else:
                return add(str0 + right, lnum, rnum + 1)

        add(str0, lnum, rnum)
        return ret

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
    # ss.hammingWeight(100)
    ss.generateParenthesis(3)
