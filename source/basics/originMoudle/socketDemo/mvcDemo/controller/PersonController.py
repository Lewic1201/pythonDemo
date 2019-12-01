#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 21:17
# @Author  : Administrator
# @File    : PersonController.py
# @Software: PyCharm
# @context : 模拟简单的mvc

from model.calendar import Calendar


def read_static(file_name):
    with open(file_name) as ff:
        content = ff.read()
    return content


def index():
    content = read_static('view/index.html')
    p = Calendar('nanjing')
    current_time = p.current
    content = content.replace("@@abc", current_time)
    return content


def home():
    content = read_static('view/home.html')
    return content


