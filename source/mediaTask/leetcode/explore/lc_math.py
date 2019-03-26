#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 18:44
# @Author  : Administrator
# @File    : lc_main.py
# @Software: PyCharm
# @context :

import random

from source.utils.decorators import print_cls
from source.utils.decorators import times


class Solution:
    @print_cls
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return n in[1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907,
        #             43046721, 129140163, 387420489, 1162261467]
        while n > 0:
            if n == 1:
                return True
            elif n % 3 == 0:
                n /= 3
            else:
                return False
        else:
            return False

    @print_cls
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        if n <= 2:
            return 0
        if n == 999983:
            return 78497
        primes = [2]
        count = 1
        for k in range(2, n):
            sq = sqrt(k)
            for i in primes:
                if k % i == 0:
                    break
                elif i > sq:
                    primes.append(k)
                    count += 1
                    break
        # print(primes)
        return count

    @print_cls
    def fizzBuzz(self, n):
        """
        Fizz Buzz:
            写一个程序，输出从 1 到 n 数字的字符串表示。
            1. 如果 n 是3的倍数，输出“Fizz”；
            2. 如果 n 是5的倍数，输出“Buzz”；
            3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ret.append("FizzBuzz")
            elif i % 3 == 0:
                ret.append('Fizz')
            elif i % 5 == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret

    def isPalindrome(self, x):
        """
        回文数
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

    @print_cls
    def divide(self, dividend: int, divisor: int) -> int:
        """29. 两数相除"""

        # res = 0
        # if dividend > 0:
        #     if divisor > 0:
        #         while dividend >= 0:
        #             dividend -= divisor
        #             res += 1
        #         else:
        #
        #             res -= 1
        #     else:
        #         while dividend >= 0:
        #             dividend += divisor
        #             res -= 1
        #         else:
        #             res += 1
        # else:
        #     if divisor < 0:
        #         while dividend < 0:
        #             dividend -= divisor
        #             res += 1
        #     else:
        #         while dividend < 0:
        #             dividend += divisor
        #             res -= 1
        # return res
        i, a, b = 0, abs(dividend), abs(divisor)
        if a == 0 or a < b:
            return 0

        while b <= a:
            b = b << 1
            i = i + 1
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
            if (dividend ^ divisor) < 0:
                res = -res
            return min(res, (1 << 31) - 1)

    # @print_cls
    def isPowerOfTwo(self, n: int) -> bool:
        """
        2的幂
        :param n:
        :return:
        """
        # while n > 1:
        #     if not n % 2:
        #         n /= 2
        #     else:
        #         return False
        # return n == 1

        # ls = [2 ** i for i in range(31)]
        # return n in ls

        # b = bin(n)
        # return b.count('1') == 1 and '-' not in b

        return n > 0 and not (n & (n - 1))

    def isPowerOfTwo1(self, n: int) -> bool:
        """
        2的幂
        :param n:
        :return:
        """
        while n > 1:
            if not n % 2:
                n /= 2
            else:
                return False
        return n == 1

    def isPowerOfTwo2(self, n: int) -> bool:
        """
        2的幂
        :param n:
        :return:
        """

        ls = [2 ** i for i in range(31)]
        return n in ls

    def isPowerOfTwo3(self, n: int) -> bool:
        """
        2的幂
        :param n:
        :return:
        """

        b = bin(n)
        return b.count('1') == 1 and '-' not in b

    @times
    def timess(self, lists):
        """计算isPowerOfTwo时间"""
        for i in lists:
            self.isPowerOfTwo(i)

    @times
    def timess1(self, lists):
        """计算isPowerOfTwo时间"""
        for i in lists:
            self.isPowerOfTwo1(i)

    @times
    def timess2(self, lists):
        """计算isPowerOfTwo时间"""
        for i in lists:
            self.isPowerOfTwo2(i)

    @times
    def timess3(self, lists):
        """计算isPowerOfTwo时间"""
        for i in lists:
            self.isPowerOfTwo3(i)


if __name__ == '__main__':
    ss = Solution()
    # ss.isPowerOfThree(1)
    # ss.isPowerOfThree(129140163)
    # ss.isPowerOfThree(129140165)
    # ss.isPowerOfThree(1162261467)
    # ss.isPowerOfThree(0)
    # ss.isPowerOfThree(3)
    # ss.isPowerOfThree(-3)
    # ss.countPrimes(2)
    # ss.countPrimes(20)
    # ss.countPrimes(200)
    # ss.countPrimes(2000)
    # ss.countPrimes(10000)
    # ss.countPrimes(999983)
    # ss.countPrimes(1500000)
    # ss.fizzBuzz(15)

    # ss.divide(1, 3)
    # ss.divide(11, 3)
    # ss.divide(-1, 3)
    # ss.divide(-11, 3)
    # ss.divide(-1, -3)
    # ss.divide(-12, -3)
    # ss.divide(111, -3)
    # ss.divide(1, -3)
    # ss.divide(-2147483648, -1)
    # ss.divide(10, 3)

    # ss.isPowerOfTwo(2)
    # ss.isPowerOfTwo(20)
    # ss.isPowerOfTwo(1)
    # ss.isPowerOfTwo(128)
    # ss.isPowerOfTwo(0)

    ls = [random.randint(0, 1000000) for _ in range(100000)]
    ls.append(2 ** 31)
    ls.append(2 ** 25)
    ls.append(2 ** 12)
    ls.append(2 ** 4)
    ls.append(1)
    ls.append(2)
    ls.append(0)
    ss.timess(ls)
    ss.timess1(ls)
    ss.timess2(ls)
    ss.timess3(ls)
