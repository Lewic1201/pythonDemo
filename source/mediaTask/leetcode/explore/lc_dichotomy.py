#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 23:34
# @Author  : Administrator
# @File    : lc_dichotomy.py
# @Software: PyCharm
# @context : 二分法
from source.utils.decorators import print_cls


class Solution:
    @staticmethod
    def binarySearch1(nums, target):
        """
        二分法模板
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1

    @staticmethod
    def binarySearch2(nums, target):
        """
        二分法高级模板
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if left != len(nums) and nums[left] == target:
            return left
        return -1

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

    @print_cls
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        queue = range(1, x + 1)
        left, right = 0, x - 1
        mid = 0
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

    @print_cls
    def search2(self, nums, target):
        """
        搜索旋转排序数组
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        bound = 0
        maxi = len(nums) - 1
        for i in range(maxi):
            if nums[i] > nums[i + 1]:
                bound = i + 1
        new_nums = nums[bound:] + nums[:bound]

        left, right = 0, maxi
        while left <= right:
            mid = (left + right) // 2
            if new_nums[mid] == target:
                if mid + bound <= maxi:
                    return mid + bound
                else:
                    return mid + bound - maxi - 1
            elif new_nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def isBadVersion(version):
        err_version = 1702766719
        return version >= err_version

    @print_cls
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                if not self.isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == '__main__':
    ss = Solution()
    # ss.search([-1, 0, 3, 5, 9, 12], 9)
    # ss.findDuplicate([1, 3, 4, 2, 2])
    # ss.findDuplicate([3, 1, 3, 4, 2, 5])
    # ss.mySqrt(3)
    # ss.search2([4, 5, 6, 7, 0, 1, 2], 0)
    # ss.search2([3, 1], 3)
    # ss.firstBadVersion(10)
    # ss.firstBadVersion(5)
    # ss.firstBadVersion(7)
    # ss.firstBadVersion(15)
    ss.firstBadVersion(2126753390)
