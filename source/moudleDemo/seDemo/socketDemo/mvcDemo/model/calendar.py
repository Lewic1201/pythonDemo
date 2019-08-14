#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 21:15
# @Author  : Administrator
# @File    : Person.py
# @Software: PyCharm
# @context :

import datetime


class Calendar:
    def __init__(self, city):
        self.current = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.city = city
