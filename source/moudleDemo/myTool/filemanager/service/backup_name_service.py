#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 19:49
# @Author  : Administrator
# @File    : backup_name_service.py
# @Software: PyCharm
# @context : 将文件名备份到Excel


from source.moudleDemo.myTool.filemanager.service.base import *
from source.moudleDemo.myTool.filemanager.file_manager import FileManage
from source.moudleDemo.myTool.filemanager.write_excel import *

all_fm = FileManage(PATH11)
pre_lnk_fm = FileManage(PATH22)


def save_all_fm():
    all_fm.save_all(BAK_FILE)


def save_pre_fm():
    pre_lnk_fm.save_all(BAK_PRE_FILE, lnk_target=True)


if __name__ == '__main__':
    save_all_fm()
    save_pre_fm()
