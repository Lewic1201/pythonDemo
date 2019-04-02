#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 11:01
# @Author  : li_panfeng
# @File    : practice.py
# @Software: PyCharm
# @context :
from wordStudy.word import WordManage


class Practice:
    def __init__(self):
        wm = WordManage()
        all_word = wm.get_data()


