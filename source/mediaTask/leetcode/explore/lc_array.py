#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 18:44
# @Author  : Administrator
# @File    : lc_main.py
# @Software: PyCharm
# @context : 数组

from source.utils.decorators import *


class Solution:
    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
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

    @print_cls
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.

        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]
        """
        i = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                i -= 1
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                i -= 1
                n -= 1
        if n > 0:
            while n > 0:
                nums1[i] = nums2[n - 1]
                i -= 1
                n -= 1
        return nums1

    # ----------------------------------error-------------------------------------
    @print_cls
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
        # lnums = len(nums)
        #
        # ret = []
        # ret2 = []
        # for i in range(lnums - 2):
        #     for j in range(i + 1, lnums - 1):
        #         for k in range(j + 1, lnums):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 ret.append(set(tmp))
        #                 ret2.append(tmp)
        #
        # for i in range(len(ret))[::-1]:
        #     if ret[i] in ret[:i]:
        #         ret2.pop(i)
        #
        # return ret2
        dic = {}
        for ele in nums:
            if ele not in dic:
                dic[ele] = 0
            dic[ele] += 1

        if 0 in dic and dic[0] > 2:
            rst = [[0, 0, 0]]
        else:
            rst = []

        pos = [p for p in dic if p > 0]
        neg = [n for n in dic if n < 0]

        for p in pos:
            for n in neg:
                inverse = -(p + n)
                if inverse in dic:
                    if inverse == p and dic[p] > 1:
                        rst.append([n, p, p])
                    elif inverse == n and dic[n] > 1:
                        rst.append([n, n, p])
                    elif inverse < n or inverse > p or inverse == 0:
                        rst.append([n, inverse, p])

        return rst

    @print_cls
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dic = dict()
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 0

    @print_cls
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        i = 0
        while True:
            if i + count >= len(nums):
                break
            if nums[i + count] == val:
                count += 1
                continue
            nums[i] = nums[i + count]
            i += 1
        return count, nums

    @print_cls
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # diffs = []
        # ret = []
        # for word in strs:
        #     word_set = sorted(word)
        #     if word_set not in diffs:
        #         diffs.append(word_set)
        # for word_set in diffs:
        #     group = []
        #     for word in strs:
        #         if sorted(word) == word_set:
        #             group.append(word)
        #     ret.append(group)
        # return ret
        def prod(astr):
            res = 1
            for i in range(len(astr)):
                res *= hfunc[astr[i]]
            return res

        hfunc = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
                 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83,
                 'x': 89, 'y': 97, 'z': 101}
        pattern = {}
        for s in strs:
            tmp = prod(s)
            if not tmp in pattern.keys():
                pattern[tmp] = [s]
            else:
                pattern[tmp].append(s)
        return [pattern[i] for i in pattern.keys()]

    @print_cls
    def rotate(self, matrix):
        """
        旋转图像

        给定一个 n × n 的二维矩阵表示一个图像。
        将图像顺时针旋转 90 度。
        说明：
        你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

        示例 1:
        给定 matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

        原地旋转输入矩阵，使其变为:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]

        示例 2:
        给定 matrix =
        [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ],
        原地旋转输入矩阵，使其变为:
        [
          [15,13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7,10,11]
        ]
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # mlen = len(matrix)
        # import copy
        # matrix2 = copy.deepcopy(matrix)
        # for i in range(mlen):
        #     for j in range(mlen):
        #         matrix[j][mlen - 1 - i] = matrix2[i][j]
        # return matrix
        matrix[::] = zip(*matrix[::-1])
        return matrix

    @print_cls
    def isIsomorphic(self, s, t):
        """
        同构字符串
        eg:
            输入: s = "paper", t = "title"
            输出: true
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 位置的映射表
        # map = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
        # slen = len(s)
        # for i in range(slen):
        #     s = s.replace(s[i], t[i])
        # if s == t:
        #     return True
        # else:
        #     return False

        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    @print_cls
    def findMedianSortedArrays(self, nums1, nums2):
        """
        寻找两个有序数组的中位数
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        p, q = 0, 0
        # 获取中位数的索引
        mid = ((m + n) // 2 - 1, (m + n) // 2) if (m + n) % 2 == 0 else ((m + n) // 2, (m + n) // 2)
        all = []
        while p < m and q < n:
            if nums1[p] <= nums2[q]:
                all.append(nums1[p])
                p += 1
            else:
                all.append(nums2[q])
                q += 1
        else:
            if p >= m:
                while q < n:
                    all.append(nums2[q])
                    q += 1
            else:
                while p < m:
                    all.append(nums1[p])
                    p += 1
        ret = (all[mid[0]] + all[mid[1]]) / 2
        return ret

    @print_cls
    def pivotIndex(self, nums):
        """
        寻找数组的中心索引
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        sums = 0
        left_sum = 0
        for n in nums:
            sums += n
        for i in range(len(nums)):
            if sums - nums[i] == left_sum * 2:
                return i
            left_sum += nums[i]
        return -1

    @print_cls
    def dominantIndex(self, nums):
        """
        至少是其他数字两倍的最大数
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maxi]:
                maxi = i
        for j in range(len(nums)):
            if j != maxi and nums[maxi] < nums[j] * 2:
                return -1
        else:
            return maxi

    @print_cls
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        else:
            return len(nums)

    @print_cls
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i in range(len(numbers)):
            if numbers[i] not in s:
                s[target - numbers[i]] = i
            else:
                return [s[numbers[i]] + 1, i + 1]

    @print_cls
    def frequencySort(self, s):
        """
        根据字符出现频率排序
        :type s: str
        :rtype: str
        """
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic2 = dict()
        for j in dic:
            if dic[j] in dic2:
                dic2[dic[j]].append(j)
            else:
                dic2[dic[j]] = [j]
        ret = ''
        for k in sorted(dic2.keys(), reverse=True):
            for m in dic2[k]:
                ret += (m * k)
        return ret

    @prints
    def maxProduct(self, nums: list) -> int:
        """乘积的最大子序列"""
        max_num = nums[0]
        for i in range(len(nums)):
            tmp = nums[i]
            if tmp > max_num:
                max_num = tmp
            for j in range(i + 1, len(nums)):
                tmp *= nums[j]
                if tmp > max_num:
                    max_num = tmp

        return max_num

    @prints
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        """滑动窗口最大值"""
        # if len(nums) == 0 or k == 0:
        #     return []
        #
        # klist = sorted(nums[:k])
        # res = [klist[-1]]
        # times = len(nums) - k
        # for i in range(k, len(nums)):
        #     klist.remove(nums[i - k])
        #     new = nums[i]
        #     if len(klist) > times:
        #         scope = (len(klist) - times, len(klist))
        #     else:
        #         scope = (len(klist),)
        #     for j in range(*scope)[::-1]:
        #         if new >= klist[j]:
        #             klist.insert(j + 1, new)
        #             break
        #     else:
        #         klist.insert(0, new)
        #     res.append(klist[-1])
        #
        # return res
        if not nums or k <= 0 or k > len(nums):
            return []
        res = [max(nums[:k])]
        max_val = res[0]
        for i in range(k, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i - k] == max_val:
                max_val = max(nums[i - k + 1:i + 1])
            res.append(max_val)
        return res


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
    # ss.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    # ss.merge([1, 2, 3, 0, 0, 0], 3, [0, 5, 6], 3)
    # ss.merge([1, 2, 3, 0, 0, 0], 3, [1, 5, 6], 3)
    # ss.threeSum([-1, 0, 1, 2, -1, -4])
    # ss.removeElement([3, 2, 2, 3], 3)
    # ss.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    # ss.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    # ss.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # rr = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # rr2 = [
    #     [5, 1, 9, 11],
    #     [2, 4, 8, 10],
    #     [13, 3, 6, 7],
    #     [15, 14, 12, 16]
    # ]
    # ss.rotate(rr)
    # ss.rotate(rr2)
    # s = "egg"
    # t = "add"
    # s = "foo"
    # t = "bar"
    # s = "paper"
    # t = "title"
    # ss.isIsomorphic(s, t)
    # ss.findMedianSortedArrays([1, 2], [3, 4])
    # ss.findMedianSortedArrays([1, 3, 4, 12], [3, 4, 5])
    # ss.pivotIndex([-1, -1, -1, -1, -1, 0])
    # ss.dominantIndex([3, 6, 1, 0])
    # ss.dominantIndex([1, 2, 3, 4])
    # ss.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    # ss.twoSum([2, 7, 11, 15], 9)
    # ss.twoSum([2, 3, 4], 6)
    # ss.twoSum([1, 2, 3, 4, 4, 9, 56, 90], 8)
    # ss.threeSum([-1, 0, 1, 2, -1, -4])
    # ss.frequencySort("Aabb")
    # ss.maxProduct([2, 3, -2, 4])
    # ss.maxProduct([0, 2])
    # ss.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    # ss.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 5)
    ss.maxSlidingWindow([4, -2], 2)
