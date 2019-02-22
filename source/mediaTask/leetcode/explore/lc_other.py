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
    def letterCombinations(self, digits):
        """
        电话号码的字母组合
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        num_map = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ret = []
        ldigits = len(digits)

        def inner(str0, index):
            # 终止条件
            if index >= ldigits:
                ret.append(str0)
                return

            tmp = []
            for i in num_map[int(digits[index])]:
                tmp.append(inner((str0 + i), index + 1))

        inner('', 0)
        return ret

    @prints
    def permute(self, nums):
        """
        全排列
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # return list(itertools.permutations(nums))

        ret = []

        def inner(list0):
            if len(list0) == len(nums):
                ret.append(list0)
                return

            for i in nums:
                tmp = list0[:]
                if i not in tmp:
                    tmp.append(i)
                    inner(tmp)

        inner([])
        return ret

    @prints
    def subsets(self, nums):
        """
        子集
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # 999ms
        # ret = []
        #
        # def inner(list0, ret):
        #
        #     set0 = set(list0)
        #     if len(list0) <= len(nums) and set0 not in ret:
        #         ret.append(set0)
        #
        #     for i in nums:
        #         tmp = list0[:]
        #         if i not in tmp:
        #             tmp.append(i)
        #             inner(tmp, ret)
        #
        # inner([], ret)
        #
        # return [list(i) for i in ret]

        # # 72ms
        # res = []
        #
        # def inner(start, num):  # 深度优先搜索
        #     res.append(num)
        #     for i in range(start, len(nums)):
        #         inner(i + 1, num + [nums[i]])
        #
        # inner(0, [])
        # return res

        # # 48ms
        res = [[]]
        for i in nums:
            nres = res.copy()
            for j in nres:
                res.append([i] + j)
                # 之所以要一次append [i] + j，是因为拷贝的结果会在每一次改变之后立刻传递给被拷贝的res，
                # 如果分开的话，比如先给 j 加上一个[i]，这时候结果已经返回给res了，然后res再去append就会导致后面出现重复。
        return res

    @prints
    def exist(self, board, word):
        """
        单词搜索
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ret = []

        # 下一步走法
        def inner(x, y, index, old_path):
            """
            :param x: 当前x坐标
            :param y: 当前y坐标
            :param index: 要找的字母
            :param old_path: 已经走过的坐标
            :return:
            """
            if (x, y) in old_path:
                return

            if board[x][y] == word[index]:
                old_path.append((x, y))

                if len(old_path) == len(word):
                    ret.append(old_path)
                    raise Exception("True")

                index += 1
                if x - 1 >= 0:
                    inner(x - 1, y, index, old_path[:])
                if x + 1 < len(board):
                    inner(x + 1, y, index, old_path[:])
                if y - 1 >= 0:
                    inner(x, y - 1, index, old_path[:])
                if y + 1 < len(board[x]):
                    inner(x, y + 1, index, old_path[:])

                # 遍历每一个初始位置

        for i in range(len(board)):
            for j in range(len(board[i])):
                try:
                    inner(i, j, 0, [])
                except Exception as err:
                    if err.args[0] == "True":
                        return True

        return False

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

    def getSum(self, a, b):
        """
        不使用运算符 + 和 - ，计算两整数 a、b 之和。
        :type a: int
        :type b: int
        :rtype: int
        """
        pass

    def partition(self, s):
        """
        分割回文串
        :type s: str
        :rtype: List[List[str]]

        输入: "aab"
        输出:
        [
          ["aa","b"],
          ["a","a","b"]
        ]
        """
        pass


if __name__ == '__main__':
    ss = Solution()
    # ss.missingNumber([3, 0, 1])
    # ss.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    # ss.missingNumber([0])
    # ss.missingNumber([])
    # ss.hammingWeight(100)
    # ss.generateParenthesis(3)
    # ss.letterCombinations('234')
    # ss.permute([1, 2, 3])
    # ss.subsets([1, 2, 3])

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # ss.exist(board, 'ABCCED')
    # ss.exist(board, 'SEE')
    # ss.exist(board, 'ABCB')

    # ss.exist([["a"]], "a")
    # ss.exist([["b", "a", "b"], ["b", "b", "a"], ["b", "b", "b"]], "ab")

    bb = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
           "a", "a", "a", "a", "a", "a", "a", "b"]]
    aa = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # ss.exist(bb, aa)

    ss.subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0])
