#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 15:38
# @Author  : Administrator
# @File    : foldname.py
# @Software: PyCharm
# @context : 文件名前添加0

import os
from source.utils.file_manager import FileManage

path = r'E:\GAME\RimWorld_ALL\RimWorld 0.18.1722 200MOD used\MODS'
os.chdir(path)

fileList = os.listdir(path)

for ff in fileList:
    ff_abs = os.path.abspath(ff)
    try:
        int(ff[:3])
    except Exception as e:
        try:
            int(ff[:2])
            print(ff, '-' * 10, '0' + ff)
            os.rename(ff,'0'+ff)
        except:
            pass

