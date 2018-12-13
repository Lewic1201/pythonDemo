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
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        for i in range(nums_len - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

    @prints
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # profit = 0
        # p_len = len(prices)
        # for i in range(p_len):
        #     for j in range(i + 1, p_len):
        #         if prices[j] > prices[i]:
        #             profit += (prices[j] - prices[i])
        #         i = j + 1
        # return profit
        profit = 0
        p_len = len(prices)
        for day in range(p_len - 1):
            differ = prices[day + 1] - prices[day]
            if differ > 0:
                profit += differ
        return profit

    @prints
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # else:
        #     return False
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

    @prints
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set_ = set()
        # for i in nums:
        #     if i in set_:
        #         set_.remove(i)
        #     else:
        #         set_.add(i)
        # return set_[0]
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    ss = Solution()
    # ss.removeDuplicates([1, 1, 2])
    # ss.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # ss.maxProfit([7, 1, 5, 3, 6, 4])
    # ss.maxProfit([1, 2, 3, 4, 5])
    # ss.maxProfit([7, 6, 4, 3, 1])
    # ss.containsDuplicate([1, 2, 3, 1])
    # ss.containsDuplicate([1, 2, 3, 4])
    # ss.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    ss.singleNumber([2, 2, 1])
    ss.singleNumber([4, 1, 2, 1, 2])
