#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 22:03
# @Author  : Administrator
# @File    : common.py
# @Software: PyCharm
# @context : simple tool object

import datetime


def get_now_time(formats='%Y-%m-%dT%H:%M:%S'):
    """
    :param formats:
    :return:
    """
    now_time = datetime.datetime.now().strftime(formats)
    return now_time


def get_now_time_num():
    """
    :return: now time: %Y%m%d%H%M%S
    """
    return get_now_time('%Y%m%d%H%M%S')




