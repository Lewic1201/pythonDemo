# coding:utf-8
'''
Created on 2018-12-17

@author: li_panfeng
'''

# from scipy.special import comb, perm
from functools import wraps


def prints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("FUNCTION: {func}()".format(func=func.__name__))
        print('PARAMS  : %s,%s' % (args[1:], kwargs))
        ret = func(*args, **kwargs)
        print("RESULT  : {ret}".format(ret=ret))
        return ret

    return wrapper


class Solution(object):
    def __init__(self):
        pass

    @prints
    def printA(self, a, c, d=6, b=6):
        return a * c

    @prints
    def pow(self, x, n):
        # @param x, a float
        # @param n, a integer
        # @return a float

        if n >= 0:
            return self.power(x, n)
        else:
            return 1 / self.power(x, -n)

    def power(self, x, n):
        if n == 0:
            return 1
        print(x, n)
        if n % 2 == 0:
            return self.power(x * x, n // 2)
        else:
            return x * self.power(x * x, (n - 1) // 2)

    @prints
    def merge(self, a, b):
        # @param A  a list of integers
        # @param m  an integer, length of A
        # @param B  a list of integers
        # @param n  an integer, length of B
        # @return nothing
        m = len(a) - 1
        n = len(b) - 1
        clen = len(a) + len(b) - 1
        c = [999 for i in range(clen + 1)]

        while m >= 0 and n >= 0:
            if a[m] >= b[n]:
                c[clen] = a[m]
                m -= 1
            else:
                c[clen] = b[n]
                n -= 1
            clen -= 1

        if m >= 0:
            for i in range(m + 1):
                c[i] = a[i]
        if n >= 0:
            for j in range(n + 1):
                c[j] = b[j]
        return c

    @prints
    def search(self, A, target):
        # @param A, a list of integers
        # @param target, an integer to be searched
        # @return an integer
        m = len(A)
        index = 0
        for i in range(m - 1):
            if A[i] > A[i + 1]:
                index = i
                break
        return self.erfen(A, target, index + 1)

    #    @prints
    def erfen(self, nums, target, index=0):
        nlen = len(nums)
        start = 0 + index
        end = nlen - 1 + index
        while start < end:
            middle = (start + end) // 2
            if middle >= nlen:
                m = middle - nlen
            else:
                m = middle
            print(start, end, middle, m)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                end = middle - 1
            else:
                start = middle + 1
        return - 1

    @prints
    def hasPathSum(self, root, sum):
        # @param root, a tree node
        # @param sum, an integer
        # @return a boolean
        pass

    @prints
    def climbStairs(self, n):
        # @param n, an integer
        # @return an integer

        a = []
        a.append(1)
        a.append(1)
        for i in range(2, n + 1):
            a.append(a[i - 1] + a[i - 2])
        print(a)
        return a[n]

    @prints
    def merge_Intervals(self, itvs):

        '''
            For example,
            Given [1,3],[2,6],[8,10],[15,18],
            return [1,6],[8,10],[15,18].
        '''
        # itvs = [[1, 3], [2, 6], [8, 10], [15, 18]]
        m = len(itvs)

        for i in range(m - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                print(itvs, itvs[i], itvs[j])
                if itvs[i][1] < itvs[j][0] or itvs[i][0] > itvs[j][1]:
                    continue
                else:
                    if itvs[i][0] <= itvs[j][0]:
                        if itvs[i][1] <= itvs[j][1]:
                            itvs[i][1], itvs[j][0] = itvs[j][1], itvs[i][0]
                        #                            itvs[j][0], itvs[j][0] = itvs[i][0], itvs[i][0]
                        else:
                            itvs[j][0], itvs[j][1] = itvs[i][0], itvs[i][1]
                    else:
                        if itvs[i][1] <= itvs[j][1]:
                            itvs[i][0], itvs[i][1] = itvs[j][0], itvs[j][1]
                        else:
                            itvs[i][1], itvs[j][1] = itvs[j][1], itvs[i][1]
        #        for i in range(m-1,0,-1):
        #            for j in range(i-1, -1, -1):

        return itvs

    @prints
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        [1,2,3,4,3,4,2,3,4,2,2,1,0,4,3,2,4,2,4,2,3,8]
        """
        pass
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i - 1, -1, -1):
                    if i - j < nums[j]:
                        break
                else:
                    return False
        else:
            return True

    @prints
    def gongyueshu(self, a, b):
        return self.zhanzhuanxiangchu(a, b)

    def zhanzhuanxiangchu(self, a, b):
        r = a % b
        print(b, r)
        if r == 0:
            return b
        else:
            return self.zhanzhuanxiangchu(b, r)

    @prints
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # num = ''
        # for i in str:
        #     if i in '+-0123456789':
        #         if num and i in '-+':
        #             break
        #         else:
        #             num += i
        # if not num or num in '+-':
        #     return 0
        #
        # n = int(num)
        # if n < -2 ** 31:
        #     return -2 ** 31
        # elif n > 2 ** 31 - 1:
        #     return 2 ** 31 - 1
        # return n
        num = ''
        for i in str:
            if not num:
                if i == ' ':
                    continue
                elif i in '+-0123456789':
                    num += i
                else:
                    return 0
            else:
                if i in '0123456789':
                    num += i
                else:
                    break
        if not num or num in '+-':
            return 0

        n = int(num)
        if n < -2 ** 31:
            return -2 ** 31
        elif n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return n

    @prints
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        optimize = ''
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                optimize += i
        for j in range((len(optimize) + 1) // 2):
            if optimize[j] != optimize[-j - 1]:
                return False
        else:
            return True

    @prints
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #         nlen = len(nums)
        #         for i in range(nlen-1):
        #             for j in range(i+1,nlen):
        #                 if nums[i]+nums[j]==target:
        #                     return [i,j]
        for k, v in enumerate(nums):
            if target - v in nums:
                k2 = nums.index(target - v)
                if k2 != k:
                    return [k, k2]

    @prints
    def reverseBits(self, n):
        # @param n, an integer
        # @return an integer
        bin_str = str(bin(n))[2:]
        bnum = bin_str[::-1]
        ret = 0
        for i in bnum:
            ret += int(i) * 2
        else:
            return ret // 2

    @prints
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def inner(m, cs=0):
            if cs >= 10:
                return False
            sum = 0
            for i in str(m):
                sum += (int(i) ** 2)
            if sum == 1:
                return True
            else:
                return inner(sum, cs + 1)

        ret = inner(n)
        return ret

    @prints
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = [i for i in nums]
        nlen = len(nums)
        for i in range(nlen):
            while i + k >= nlen - 1:
                k -= nlen
            nums[i + k] = tmp[i]
        return nums


if __name__ == '__main__':
    ss = Solution()
    # ss.printA('aa', 12, d=23, b=65)
    # ss.pow(0.5, -10)
    # ss.merge([113, 213, 765, 787], [2, 5, 7])
    #
    # ss.erfen([1, 2, 4, 33, 54, 57, 71, 168, 681, 683, 777], 70)
    # ss.search([1111, 2121, 1, 2, 4, 33, 54, 57, 71, 168, 681, 683, 777], 71)
    # ss.climbStairs(30)
    # ss.merge_Intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
    # ss.merge_Intervals([[2, 5], [0, 1], [0, 3], [0, 6], [3, 4], [4, 6], [6, 7]])
    # ss.gongyueshu(144, 456)
    # ss.canJump([1, 2, 3, 4, 3, 4, 2, 3, 5, 2, 2, 1, 0, 4, 3, 2, 1, 0, 4, 2, 3, 8])
    # ss.myAtoi('42')
    # ss.myAtoi('   -42')
    # ss.myAtoi('4194 with words')
    # ss.myAtoi('wrew 984')
    # ss.myAtoi('-91283472332')
    # ss.myAtoi('-91+283472332')
    # ss.myAtoi('+')
    # ss.myAtoi('++')
    # ss.myAtoi('+--')
    # ss.myAtoi('-')
    # ss.myAtoi('"words and 987"')
    # ss.isPalindrome("A man, a plan, a canal: Panama")
    # ss.isPalindrome("A man, a plan, a ca")
    # ss.twoSum([2, 7, 11, 15], 9)
    # ss.twoSum([3, 2, 4], 6)
    # ss.reverseBits(4)
    # ss.isHappy(19)
    ss.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    ss.rotate([-1, -100, 3, 99], 2)
    ss.rotate([-1],2)

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
#
# def stringToListNode(input):
#     import json
#     # Generate list from the input
#     numbers = json.loads(input)
#
#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next
#
#     ptr = dummyRoot.next
#     return ptr
#
#
# def prettyPrintLinkedList(node):
#     import sys
#     while node and node.next:
#         sys.stdout.write(str(node.val) + "->")
#         node = node.next
#
#     if node:
#         print(node.val)
#     else:
#         print("Empty LinkedList")
#
#
# def main():
#     import sys
#
#     def readlines():
#         for line in sys.stdin:
#             yield line.strip('\n')
#
#     lines = readlines()
#     while True:
#         try:
#             line = lines.next()
#             node = stringToListNode(line)
#             prettyPrintLinkedList(node)
#         except StopIteration:
#             break
