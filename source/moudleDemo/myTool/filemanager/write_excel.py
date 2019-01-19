#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 15:13
# @Author  : Administrator
# @File    : save_info.py
# @Software: PyCharm
# @context :

import os
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy

"""
from os.path import join
from xlrd import open_workbook
rb = open_workbook(join(text_files,'testall.xls'))
然后使用xlutils.copy模块将xlrd.Book对象拷贝为一个xlwt.workbook对象(体现了xlutils库桥梁的作用)：

from xlutils.copy import copy
wb = copy(rb)
再使用xlwt的方法操作xlwt.workbook对象:

wb.get_sheet(0).write(0,0,'changed')
wb.save(join(temp_dir,'output.xls'))
"""


class EditExcel:
    def __init__(self, filename):
        # 文件名后缀不对,添加后缀
        if not filename[-4:] == '.xls':
            filename += '.xls'
        self.filename = filename
        # 读取Excel对象
        self.rb = xlrd.open_workbook(filename,formatting_info=True)
        # 写入Excel的workbook对象
        self.wb = copy(self.rb)
        self.workbook = self.wb
        self.worksheets = []

    def add_a_sheet(self, sheet_name):
        """添加一个工作表"""
        worksheet = self.workbook.add_sheet(sheet_name)
        self.worksheets.append(worksheet)
        return worksheet

    def write_data(self, datas, worksheet):
        """
        写入数据
        :param datas:[[,...],...]
        :return:
        """
        try:
            for row in range(len(datas)):
                if row is None:
                    continue
                data = datas[row]
                for col in range(len(data)):
                    if data is None:
                        continue
                    worksheet.write(row, col, data[col])
        except Exception as err:
            print(row, col, err)
            raise

    def save(self):
        self.workbook.save(self.filename)
        print('save success')


class WriteExcel:
    def __init__(self, filename, sheet_name='data'):
        self.filename = filename
        # 文件名后缀不对,添加后缀
        if not self.filename[-4:] == '.xls':
            self.filename += '.xls'
        # 创建一个工作簿
        self.workbook = xlwt.Workbook('ascii')
        # 默认创建一个工作表
        self.worksheet = self.workbook.add_sheet(sheet_name)

    def add_a_sheet(self, sheet_name):
        """添加一个工作表"""
        worksheet = self.workbook.add_sheet(sheet_name)
        return worksheet

    def write_data(self, datas, worksheet=None):
        """
        写入数据
        :param datas:[[,...],...]
        :return:
        """
        try:
            if worksheet is None:
                worksheet = self.worksheet
            for row in range(len(datas)):
                if row is None:
                    continue
                data = datas[row]
                for col in range(len(data)):
                    if data is None:
                        continue
                    worksheet.write(row, col, data[col])
        except Exception as err:
            print(row, col, err)
            raise

    def save(self):
        self.workbook.save(self.filename)
        print('save success')


def save_info(file_name, sheet_name, datas):
    """
    保存数据到Excel表,如果文件存在,则在文件里新增一个表
    :param file_name: 文件名
    :param sheet_name: 表名
    :param datas: 数据[[]]
    :return:
    """
    if os.path.exists(file_name):
        ew = EditExcel(file_name)
        sheet = ew.add_a_sheet(sheet_name)
        ew.write_data(datas, sheet)
        ew.save()
    else:
        we = WriteExcel(file_name, sheet_name)
        we.write_data(datas)
        we.save()

# save_info('G:\\Lenovo Limited Warranty_V1.2_UHD\\files', 'test', [[12, 3, 4], [53]])

# path3 = 'E:\\import_file\\disk_file'
# ew = EditExcel(path3)
# sheet = ew.add_a_sheet('1234')
# ew.write_data([[123, 43, 5, 45],[1, 23]], sheet)
# ew.save()
