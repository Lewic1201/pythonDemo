#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:46
# @Author  : Administrator
# @File    : lc_teambition.py
# @Software: PyCharm
# @context :

from source.utils.decorators import print_cls


class Solution:

    @print_cls
    def fullJustify(self, words, maxWidth):
        """
        文本左右对齐
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        now_len = 0
        data = []
        ret = []
        for i in words:
            now_len += (len(i) + 1)
            if now_len <= maxWidth + 1:
                data.append(i)
            else:
                spaces = maxWidth - (now_len - len(i) - 2)
                retStr = ''
                if (len(data) - 1) == 0:
                    retStr += data[0]
                    retStr += ((maxWidth - len(retStr)) * ' ')
                    ret.append(retStr)
                else:
                    interval = spaces // (len(data) - 1)
                    remainder = spaces % (len(data) - 1)
                    for word in data:
                        retStr += (word + (interval + 1) * ' ')
                        if remainder > 0:
                            retStr += ' '
                        remainder -= 1
                    else:
                        retStr = retStr.strip()
                        ret.append(retStr)
                data = [i]
                now_len = len(i) + 1
        else:
            retStr = ''
            for word in data:
                retStr += (word + ' ')
            else:
                retStr += ((maxWidth - len(retStr) + 1) * ' ')
                ret.append(retStr[:-1])
        return ret

    @print_cls
    def judgePoint24(self, nums):
        """
        24点游戏
        eg:
            输入: [4, 1, 8, 7]
            输出: True
            解释: (8-4) * (7-1) = 24
        :type nums: List[int]
        :rtype: bool
        """
        """
        a+b+c+d
        a+b+c-d
        a+b-c-d
        """
        pass

    @print_cls
    def isInterleave(self, s1, s2, s3):
        """
        交错字符串
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        j = 0
        k = 0
        priority = 1
        if len(s3)!=len(s1)+len(s2):
            return False
        for i in range(len(s3)):
            if priority == 1:
                if j < len(s1) and s3[i] == s1[j]:
                    j += 1
                    priority = 1
                elif k < len(s2) and s3[i] == s2[k]:
                    k += 1
                    priority = 2
                else:
                    return False
            elif priority == 2:
                if k < len(s2) and s3[i] == s2[k]:
                    k += 1
                    priority = 2
                elif j < len(s1) and s3[i] == s1[j]:
                    j += 1
                    priority = 1
                else:
                    return False
        else:
            return True


if __name__ == '__main__':
    ss = Solution()
    # words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
    #          "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    # maxWidth = 20
    # ss.fullJustify(words, maxWidth)
    # ww = ["What", "must", "be", "acknowledgment", "shall", "be"]
    # mm = 16
    # ss.fullJustify(ww, mm)
    # ww2 = ["This", "is", "an", "example", "of", "text", "justification."]
    # ss.fullJustify(ww2, mm)

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s1 = "abbbb"
    # s2 = "dabsdca"
    # s3 = "dabbbabsbdca"
    ss.isInterleave(s1, s2, s3)
