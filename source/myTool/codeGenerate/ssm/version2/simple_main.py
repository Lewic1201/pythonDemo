#!/usr/bin/env python
# -- coding: utf-8 --
"""
@author: Lewic
@file: main
@time: 2019/6/19 0:18
@desc:
"""
import os
from util.dataStructure import TableFields
from util.create_group import get_all_filelist
from util.create_group import generate_file
from version2.code_div import create_replace_map

BASE_FILES_DIR = os.path.abspath('../template/baseFiles2/')
RES_DIR = os.path.abspath('../result/')


def generate_group(table_field):
    """
    生成一个表的一组code
    :param table_field: 表结构
    :return:
    """
    div_map = create_replace_map(table_field)
    base_files = get_all_filelist(BASE_FILES_DIR)
    for bf in base_files:
        generate_file(bf, div_map,RES_DIR)


if __name__ == '__main__':
    tf = TableFields('monitor_node', '节点监控', 'com.hoperun.aimanager', 'id')
    tf.add_column('node_name', '节点名称', 'varchar')
    tf.add_column('status', '状态', 'integer')
    tf.add_column('ip_address', 'ip地址', 'varchar')
    tf.add_column('app_name', '应用名称', 'varchar')
    tf.add_column('alarm_num', '告警数', 'integer')
    tf.add_column('server_log', '服务器日志', 'varchar')
    tf.add_column('update_time', '更新时间', 'varchar')
    tf.add_column('create_time', '创建时间', 'varchar')

    generate_group(tf)
