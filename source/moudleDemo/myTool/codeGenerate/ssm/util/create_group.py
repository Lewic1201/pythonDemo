#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: create_group
@time: 2019/7/16 20:36
@desc:
"""

import os


def get_all_filelist(rootdir):
    """
    获取当前目录下所有文件路径
    :return: 路径列表
    :rtype: list
    """
    if not rootdir or not os.path.exists(rootdir):
        return []

    def list_all_files(dir_path):
        _files = []
        # 列出文件夹下所有的目录与文件
        file_list = os.listdir(dir_path)
        for i in range(0, len(file_list)):
            file_name = os.path.join(dir_path, file_list[i])
            if os.path.isdir(file_name):
                _files.extend(list_all_files(file_name))
            if os.path.isfile(file_name):
                _files.append(file_name)
        return _files

    result = list_all_files(rootdir)
    # 过滤文件夹
    for i in range(len(result)):
        if os.path.isdir(result[i]):
            result.pop(i)
    return result


def generate_file(base_file, div_map, res_dir):
    """
    :param base_file: 模板文件
    :param div_map: 代码块map
    :param res_dir: 返回目录
    :return:
    """
    with open(base_file, encoding='utf8') as bf:
        content = bf.read()
        new_content = content
        for div in div_map:
            new_content = new_content.replace(div[0], div[1])

    # 生成新的文件名
    new_dir = os.path.join(res_dir, div_map[11][1])
    os.makedirs(new_dir, exist_ok=True)
    new_file = os.path.join(new_dir, os.path.basename(base_file).replace(div_map[11][0], div_map[11][1]))
    with open(new_file, 'w', encoding='utf8') as nf:
        nf.write(new_content)

    print('create file success: %s' % os.path.basename(new_file))


