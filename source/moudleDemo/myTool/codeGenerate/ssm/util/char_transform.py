#!/usr/bin/env python
# -- coding: utf-8 --
"""
@author: Lewic
@file:
@time: 2019/6/17 9:02
@desc:
"""


class CharTransform:

    # 变量名由驼峰式转换为下划线式
    @classmethod
    def to_large(cls, word):
        new_word = ''
        first = True
        for i in word:
            if first:
                new_word += i.lower()
                first = False
                continue
            if i.isupper():
                new_word += ('_' + i.lower())
            else:
                new_word += i
        return new_word

    # 下划线连接转换为驼峰式
    @classmethod
    def to_hump(cls, word):
        new_word = ''
        flag = False
        for i in word:
            if i == '_':
                flag = True
                continue
            if flag:
                new_word += i.upper()
                flag = False
            else:
                new_word += i
        return new_word
