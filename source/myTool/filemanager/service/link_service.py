#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 10:35
# @Author  : Administrator
# @File    : link_service.py
# @Software: PyCharm
# @context :

from source.myTool.filemanager.file_manager import FileManage
from source.myTool.filemanager.write_excel import *

fm = FileManage(PATH11)


def create_link():
    # 创建所有文件快捷方式
    fm.create_lnks(PATH21)


def create_pre_link():
    # 创建pre的快捷方式
    fl = fm.get_files_by_name(RE_PRE, nameorpath=False)
    fm.create_lnks(PATH22, fl)


if __name__ == '__main__':
    # create_link()
    create_pre_link()
    pass
