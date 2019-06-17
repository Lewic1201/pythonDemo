#!/usr/bin/env python
# -- coding: utf-8 --
'''
@author: Lewic
@file: dataStructure
@time: 2019/6/17 22:56
@desc:
'''
from util.char_transform import CharTransform as ct


class TableFields:

    def __init__(self):
        self.table_name = ''
        self.table_name_ch = ''
        self.entity_name = ''
        self.class_name = ''

        self.columns = []

    def set_table_name(self, table_name):
        self.table_name = table_name
        self.entity_name = ct.to_hump(table_name)
        self.class_name = ct.to_upper_hump(self.entity_name)

    def get_table_name(self):
        return self.table_name

    def set_table_name_ch(self, table_name_ch):
        self.table_name_ch = table_name_ch

    def get_table_name_ch(self):
        return self.table_name_ch

    def add_column(self, column_name, column_name_ch, column_type='varchar'):
        column_dict = dict()
        column_dict['column_name'] = column_name
        column_dict['column_name_ch'] = column_name_ch
        column_dict['column_type'] = column_type
        column_dict['param_name'] = ct.to_hump(column_name)

        self.columns.append(column_dict)

    def pop_column(self, column_name):
        i = 0
        for col in self.columns:
            if col['column_name'] == column_name:
                self.columns.pop(i)
                break
            i += 1

    def get_columns(self):
        return self.columns
