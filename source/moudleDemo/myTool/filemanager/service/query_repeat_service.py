#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 19:54
# @Author  : Administrator
# @File    : query_repeat_service.py
# @Software: PyCharm
# @context :

import datetime
import pprint
import json
from source.moudleDemo.myTool.filemanager.service.base import *
from source.moudleDemo.myTool.filemanager.file_manager import FileManage
from source.moudleDemo.myTool.filemanager.file_manager import get_now_time


# 获取文件列表
def get_all_file():
    path1 = r'E:\resource'
    path2 = r'F:\install_package'
    fm = FileManage(path1)
    fm2 = FileManage(path2)
    res = fm.get_files_by_name(RE_PACKAGE) + fm2.get_files_by_name(RE_PACKAGE)
    return res


# 获取重复文件
def query_repeat_service(file_list):
    fm = FileManage('.\\')
    return fm.get_same_file(file_list)


def write_res(res_dict):
    date = get_now_time('%Y%m%d-%H%M%S')
    with open(r".\res\res-%s.json" % date, 'w', encoding='utf-8') as ff:
        json.dump(res_dict, ff, ensure_ascii=False)


if __name__ == '__main__':
    file_list = get_all_file()
    same_file = query_repeat_service(file_list)
    pprint.pprint(same_file)
    write_res(same_file)
