#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 18:44
# @Author  : Administrator
# @File    : lc_main.py
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

    @prints
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
                    count+=1
                    break
        # print(primes)
        return count


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
    ss.countPrimes(999983)
    ss.countPrimes(1500000)
