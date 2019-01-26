#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 23:34
# @Author  : Administrator
# @File    : lc_base_erfen.py
# @Software: PyCharm
# @context :
from source.utils.decorators import print_cls


class Solution:
    @print_cls
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        min_index = 0
        max_index = nums_len - 1

        while max_index >= min_index:
            middle_index = (max_index + min_index) // 2
            if target == nums[middle_index]:
                return middle_index
            elif target < nums[middle_index]:
                max_index = middle_index - 1
            elif target > nums[middle_index]:
                min_index = middle_index + 1
        else:
            return -1

    @print_cls
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # while True:
        #     pick = int(input())
        #     if pick > n:
        #         return 1
        #     elif pick < n:
        #         return -1
        #     else:
        #         break
        # return 0
        pass

    @print_cls
    def findDuplicate(self, nums):
        """
        寻找重复数
        :type nums: List[int]
        :rtype: int
        """
        # return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))

        if len(nums) < 2:
            return None
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]  # 相当于走了一步
            fast = nums[nums[fast]]  # 相当于走了两步
        fast = 0
        while fast != slow:
            fast = nums[fast]  # 相当于走了一步
            slow = nums[slow]  # 相当于走了一步
        return slow


if __name__ == '__main__':
    ss = Solution()
    # ss.search([-1, 0, 3, 5, 9, 12], 9)
    # ss.findDuplicate([1, 3, 4, 2, 2])
    ss.findDuplicate([3, 1, 3, 4, 2, 5])
