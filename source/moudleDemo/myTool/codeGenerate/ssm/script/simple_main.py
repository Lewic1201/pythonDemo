#!/usr/bin/env python
# -- coding: utf-8 --
"""
@author: Lewic
@file: main
@time: 2019/6/19 0:18
@desc:
"""
import os
from script.dataStructure import TableFields
from script.code_div import create_replace_map

BASE_FILES_DIR = os.path.abspath('../template/baseFiles/')
RES_DIR = os.path.abspath('../result/')


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


def generate_file(base_file, div_map):
    """
    :param base_file: 模板文件
    :param div_map: 代码块map
    :return:
    """
    with open(base_file, encoding='utf8') as bf:
        content = bf.read()
        new_content = content
        for div in div_map:
            new_content = new_content.replace(div[0], div[1])

    # 生成新的文件名
    new_dir = os.path.join(RES_DIR, div_map[13][1])
    os.makedirs(new_dir,exist_ok=True)
    new_file = os.path.join(new_dir, os.path.basename(base_file).replace(div_map[13][0], div_map[13][1]))
    with open(new_file, 'w', encoding='utf8') as nf:
        nf.write(new_content)

    print('create file success: %s' % os.path.basename(new_file))


def generate_group(table_field):
    """
    生成一个表的一组code
    :param table_field:
    :return:
    """
    div_map = create_replace_map(table_field)
    base_files = get_all_filelist(BASE_FILES_DIR)
    for bf in base_files:
        generate_file(bf, div_map)


if __name__ == '__main__':
    tf = TableFields('client_link', '客户资料', 'com.sc.hoperun', 'clientId')
    tf.add_column('user_name', '用户名')
    tf.add_column('password', '密码')
    tf.add_column('create_time', '创建时间', 'datetime')
    tf.add_column('level', '权限级别', 'int')

    generate_group(tf)
