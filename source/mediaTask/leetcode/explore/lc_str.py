#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 21:14
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
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ''
        for i in s:
            ret = i + ret
        return ret

    @prints
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2 ** 31 < x < 2 ** 31 - 1:
            pass
        else:
            return 0
        str_x = ''
        sign = '' if x > 0 else '-'
        x = -x if x < 0 else x
        for i in str(x):
            str_x = i + str_x
        ret = int(sign + str_x)
        if -2 ** 31 < ret < 2 ** 31 - 1:
            return ret
        else:
            return 0

    @prints
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        repeat = set()
        for i in range(slen - 1):
            if s[i] in repeat:
                continue
            for j in range(i + 1, slen):
                if s[i] == s[j]:
                    repeat.add(s[i])
                    break
                elif j == slen - 1:
                    return i
        else:
            if s[slen - 1] not in repeat:
                return slen - 1
            return -1

    @prints
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if s_sort == t_sort:
        #     return True
        # else:
        #     return False
        slen = len(s)
        if len(t) != slen:
            return False
        sset = set(s)
        for i in sset:
            if s.count(i) != t.count(i):
                return False
        else:
            return True

    @prints
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if not needle:
        #     return 0
        # if needle not in haystack:
        #     return -1
        # if needle in haystack:
        #     return haystack.index(needle)

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len):
            if haystack[i:i + needle_len] == needle:
                return i
        else:
            return -1

    @prints
    def countAndSay(self, n):
        """
        报数
            1
            11
            21
            1211
            111221
        :type n: int
        :rtype: str
        """
        index = 1
        ret = ['1']
        while index < n:
            now_str = ret[-1]
            tmp = 0
            newstr = ''
            for i in range(len(now_str)):
                before = now_str[i - 1] if i >= 1 else ''
                if now_str[i] == before:
                    tmp += 1
                else:
                    if before:
                        newstr += (str(tmp) + before)
                    before = now_str[i]
                    tmp = 1
                if i == len(now_str) - 1:
                    newstr += (str(tmp) + before)
            ret.append(newstr)
            index += 1
        return ret[-1]


if __name__ == '__main__':
    ss = Solution()
    # ss.reverseString('hello')
    # ss.reverse(123)
    # ss.reverse(120)
    # ss.reverse(-123)
    # ss.firstUniqChar("leetcode")
    # ss.firstUniqChar("loveleetcode")
    # ss.firstUniqChar("lleetcotdocdee")
    # ss.firstUniqChar("lleetcotdocdees")
    # ss.isAnagram("anagram", "nagaram")
    # ss.isAnagram("rat", "car")
    # ss.strStr('hello', 'll')
    # ss.strStr('aaaaa', 'bba')
    # ss.strStr('aaaaa', '')
    ss.countAndSay(4)
    ss.countAndSay(3)
    ss.countAndSay(5)
