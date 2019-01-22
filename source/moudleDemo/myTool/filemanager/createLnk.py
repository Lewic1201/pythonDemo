#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 15:37
# @Author  : Administrator
# @File    : createLnk.py
# @Software: PyCharm
# @context :


def create_shortcut_to_desktop(target,title):
    """Create shortcut to desktop"""
    s = path.basename(target)
    fname = path.splitext(s)[0]
    winshell.CreateShortcut(
    Path = path.join(winshell.desktop(), fname + '.lnk'),
    Target = target,
    Icon=(target, 0),
    Description=title)