#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 16:31
# @Author  : li_panfeng
# @File    : common.py
# @Software: PyCharm
# @context : 
from source.basics.myTool.count_code_line import ccl_main
from source.basics.myTool.filemanager.file_manager import FileManage
from source.application.mainWeb.utils.sqlutil import SqliteManage


def count_code_line():
    return ccl_main.main()


def show_repeat_file(dir_path):
    fm = FileManage(dir_path)
    res = fm.get_same_file()
    return res


def show_dir_path():
    sm = SqliteManage()
    sm.fetchall()


def add_path(path):
    sm = SqliteManage()
    sm.exec("insert into dirpath(path) values ('%s')" % path)
    sm.close_all()
    return 'success'


def show_dir_path():
    sm = SqliteManage()
    res = sm.fetchall('select pid,path from dirpath')
    sm.close_all()
    return res


def delete_path(pid):
    sm = SqliteManage()
    sm.exec('delete from dirpath where pid=%d' % pid)
    sm.close_all()
    return 'success'
