#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:46
# @Author  : Administrator
# @File    : lc_teambition.py
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
                retStr += ((maxWidth - len(retStr)+1) * ' ')
                ret.append(retStr[:-1])
        return ret


if __name__ == '__main__':
    ss = Solution()
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    ss.fullJustify(words, maxWidth)
    ww = ["What", "must", "be", "acknowledgment", "shall", "be"]
    mm = 16
    ss.fullJustify(ww, mm)
    ww2 = ["This", "is", "an", "example", "of", "text", "justification."]
    ss.fullJustify(ww2, mm)
