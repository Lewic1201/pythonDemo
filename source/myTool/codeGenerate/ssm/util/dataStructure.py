#!/usr/bin/env python
# -- coding: utf-8 --
'''
@author: Lewic
@file: dataStructure
@time: 2019/6/17 22:56
@desc:
'''
from util.char_transform import CharTransform as ct

TYPE_MAP = {'varchar': 'String',
            'int': 'Integer',
            'integer': 'Integer',
            'double': 'Double',
            'datetime': 'String'}
JDBC_MAP = {'datetime': 'TIMESTAMP',
            'int': 'INTEGER',
            'integer': 'INTEGER',
            'varchar': 'VARCHAR',
            'double': 'DOUBLE',
            }


class TableFields:

    def __init__(self, table_name, table_name_ch='', package_pre='com.sc.hoperun', column_id='id'):
        self.package_pre = package_pre
        self.table_name = table_name
        self.table_name_ch = table_name_ch
        self.column_id = column_id

        self.entity_name = ct.to_hump(table_name)
        self.class_name = ct.to_upper_hump(self.entity_name)

        self._columns = []

    def set_table_name(self, table_name):
        self.table_name = table_name
        self.entity_name = ct.to_hump(table_name)
        self.class_name = ct.to_upper_hump(self.entity_name)

    def add_column(self, column_name, column_name_ch='', column_type='varchar'):
        column_dict = dict()
        column_dict['column_name'] = column_name
        column_dict['column_name_ch'] = column_name_ch
        column_dict['column_type'] = column_type
        column_dict['param_name'] = ct.to_hump(column_name)
        column_dict['param_type'] = TYPE_MAP[column_type]
        column_dict['jdbc_type'] = JDBC_MAP[column_type]

        self._columns.append(column_dict)

    def pop_column(self, column_name):
        i = 0
        for col in self._columns:
            if col['column_name'] == column_name:
                self._columns.pop(i)
                break
            i += 1

    def get_columns(self):
        return self._columns
