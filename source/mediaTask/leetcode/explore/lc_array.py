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
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits[-1] += 1
        # return digits
        # digits = []
        dlen = len(digits)
        for k, v in enumerate(digits[::-1]):
            if v == 9:
                digits[dlen - k - 1] = 0
                if k == dlen - 1:
                    digits.insert(0, 1)
                    return digits
                continue
            else:
                digits[dlen - k - 1] += 1
                return digits

    @prints
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        for i in set1:
            m = nums1.count(i)
            if i in set2:
                n = nums2.count(i)
                if m > n:
                    for j in range(m - n):
                        nums1.remove(i)
            else:
                for j in range(m):
                    nums1.remove(i)
        return nums1

    @prints
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        ret = []
        nums_len = len(nums)
        for i in range(nums_len):
            num = []
            for j in range(i, nums_len):
                num.append(nums[j])
                ret.append(deepcopy(num))
        ret.append([])
        return ret

    @prints
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass

    @prints
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix_str = ""
        for i in strs[0]:
            prefix_str += i
            for j in strs:
                if not j.startswith(prefix_str):
                    return prefix_str[:-1]

    @prints
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in nums:
        #     if i == 0:
        #         nums.remove(0)
        #         nums.append(0)
        # return nums
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1
        for k in range(j, len(nums)):
            nums[k] = 0
        return nums

    @prints
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        input:
        [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
        return: true
        """
        board_col = []
        board_div = []
        for ri, row in enumerate(board):
            for ci, num in enumerate(row):
                if num == '.':
                    continue
                while ci >= len(board_col):
                    board_col.append([])
                board_col[ci].append(num)
                board_div_index = ci // 3 + (ri // 3) * 3
                while board_div_index >= len(board_div):
                    board_div.append([])
                board_div[board_div_index].append(num)

        for row in board:
            tmp = []
            for num in row:
                if num != '.':
                    tmp.append(num)
            if len(tmp) != len(set(tmp)):
                return False
        for row in board_col:
            tmp = []
            for num in row:
                tmp.append(num)
            if len(tmp) != len(set(tmp)):
                return False
        for row in board_div:
            tmp = []
            for num in row:
                tmp.append(num)
            if len(tmp) != len(set(tmp)):
                return False
        return True

    @prints
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dlen = len(digits)
        for k, v in enumerate(digits[::-1]):
            if v == 9:
                digits[dlen - k - 1] = 0
                if k == dlen - 1:
                    digits.insert(0, 1)
                    return digits
                continue
            else:
                digits[dlen - k - 1] += 1
                return digits

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

    @prints
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

        满足要求的三元组集合为：
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
        """
        min0 = []
        max0 = []
        ret = []
        for i in nums:
            if i < 0:
                min0.append(i)
            else:
                max0.append(i)

        for j in set(min0):
            for k in set(max0):
                m = -j - k
                if m in nums:
                    if m < 0:
                        group = [m, j, k]
                    elif m > 0:
                        group = [j, k, m]
                    else:
                        group = [j, m, k]

                    if group not in ret:
                        ret.append(group)

        return ret


if __name__ == '__main__':
    ss = Solution()
    # ss.removeDuplicates([1, 1, 2])
    # ss.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # ss.maxProfit([7, 1, 5, 3, 6, 4])
    # ss.maxProfit([1, 2, 3, 4, 5])
    # ss.maxProfit([7, 6, 4, 3, 1])
    # ss.plusOne([1, 2, 3])
    # ss.plusOne([4, 3, 2, 1])
    # ss.plusOne([4, 3, 2, 9])
    # ss.plusOne([9, 9, 9, 9])
    # ss.intersect([1, 2, 2, 1], [2, 2])
    # ss.intersect([4, 9, 5], [9, 4, 9, 8, 4])
    # ss.subsets([1,2,3])
    # ss.moveZeroes([0, 1, 0, 3, 12])
    # ss.moveZeroes([])
    # ss.moveZeroes([0])
    # jgg = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    # ss.isValidSudoku(jgg)
    ss.threeSum([-1, 0, 1, 2, -1, -4])
