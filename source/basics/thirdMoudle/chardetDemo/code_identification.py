#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 14:07
# @Author  : li_panfeng
# @File    : code_identification.py
# @Software: PyCharm
# @context : 字符串编码识别


import chardet

data = u'12312中国'.encode('gbk')
data2 = u'12312中国'.encode('utf-8')
data3 = u'12312abc'.encode('gbk')
data4 = u'12312abc'.encode('utf-8')
print(chardet.detect(data))
print(chardet.detect(data2))
print(chardet.detect(data3))
print(chardet.detect(data4))
