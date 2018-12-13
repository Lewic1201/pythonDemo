#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 23:34
# @Author  : Administrator
# @File    : lc_base_erfen.py
# @Software: PyCharm
# @context :

class Solution:
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


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
