#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ! python3
"""
@author: Lewic
@file: script
@time: 2019/7/3 11:35
@desc:
"""

from source.utils.decorators import prints


@prints
def upper_word(word=''):
    if isinstance(word, str):
        return word.upper()


if __name__ == '__main__':
    upper_word('listMonitorAlarm')
    upper_word('getMonitorAlarm')
    upper_word('notification')
    upper_word('')
    upper_word('')
    upper_word('')
