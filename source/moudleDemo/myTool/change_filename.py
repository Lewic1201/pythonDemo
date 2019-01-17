#!/usr/bin/env python
# -- coding: utf-8 --
'''
@author: lewic
@file: change_filename.py
@time: 2018/7/14 19:30
@desc:
'''

import os
import os.path as op
import pprint
import re

file_path = u'H:\Lenovo Limited Warranty_V1.2_UHD\config\java'
os.chdir(file_path)


def change_name(file_abspath):
    file_up_path = op.split(file_abspath)[0]
    file_name = op.split(file_abspath)[1]
    new_name = deal_file_name(file_name)
    os.chdir(file_up_path)
    if file_name != new_name:
        print(op.abspath(file_name))
        try:
            os.rename(file_name, new_name)
            message = 'info: ' + '\033[5;33;0m' + file_name + '\033[5;34;0m' + ' ---->>>> ' + '\033[5;33;0m' \
                      + new_name + '\033[0m'
            print(message)
        except FileNotFoundError:
            err_message = 'warning: ' + '\033[5;31;0m' + 'file "' + file_name + '" not found' + '\033[0m'
            print(err_message)
    # print(file_up_path)


def deal_file_name(file_name):
    pattern_01 = re.compile(r'^(\w\d{3})(\s{3,})(.*)(\.\w{2,4})$')
    pattern_02 = re.compile(r'^.*(阳光电影www\.ygdy8\.com\.).*$')
    check_result = pattern_01.match(file_name)
    check_result_2 = pattern_02.match(file_name)
    new_name = file_name

    if check_result:  # 查找头部，没有匹配
        # print(check_result.group(0))
        prefix = check_result.group(1)
        speace = check_result.group(2)
        file_name_content = check_result.group(3)
        suffix = check_result.group(4)

        new_name = prefix + '                       ' + file_name_content + suffix
        return new_name

    if check_result_2:
        # print(check_result_2.group(0))
        extra = check_result_2.group(1)

        new_name = file_name.replace(extra, '')
        return new_name
    return new_name


file_list = os.listdir()
for file_name in file_list:
    change_name(op.abspath(file_name))

# file_name = 'A023         阳光电影www.ygdy8.com.一纸婚约.HD.1080p.国语中字.mp4'
# try:
#     os.rename('阳光电影www.ygdy8.com.陈翔六点半之铁头无敌.HD.720p.国语中字.mkv', '陈翔六点半之铁头无敌.HD.720p.国语中字.mkv')
# except FileNotFoundError:
#     print('阳光电影www.ygdy8.com.陈翔六点半之铁头无敌.HD.720p.国语中字.mkv' + '  文件未找到')
# change_name(op.join(file_path,file_list[1]))
# pprint.pprint(file_list)
