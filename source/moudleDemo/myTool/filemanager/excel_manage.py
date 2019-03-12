#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 15:13
# @Author  : Administrator
# @File    : save_info.py
# @Software: PyCharm
# @context : 操作Excel

import os
import time
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy
from source.utils.decorators import print_def


class ReadExcel:
    """
    读取Excel
    """
    """
    file = 'test3.xlsx'

    def read_excel():

        wb = xlrd.open_workbook(filename=file)#打开文件
        print(wb.sheet_names())#获取所有表格名字

        sheet1 = wb.sheet_by_index(0)#通过索引获取表格
        sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
        print(sheet1,sheet2)
        print(sheet1.name,sheet1.nrows,sheet1.ncols)

        rows = sheet1.row_values(2)#获取行内容
        cols = sheet1.col_values(3)#获取列内容
        print(rows)
        print(cols)

        print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
        print(sheet1.cell_value(1,0))
        print(sheet1.row(1)[0].value)"""

    def __init__(self, filename, rwb=None):
        """
        :param filename: 文件名
        :param rb: 读取Excel的workbook
        """
        self.filename = filename
        # 创建工作簿
        self.rwb = rwb if rwb else xlrd.open_workbook(filename)

    def get_sheets_name(self):
        """
        获取表格列表
        :return:
        """
        return self.rwb.sheet_names()

    def get_datas(self, sheet_name):
        """获取sheet每行的数据"""
        sheet = self.rwb.sheet_by_name(sheet_name)
        ret = []
        for row in range(sheet.nrows):
            ret.append(sheet.row_values(row))
        return ret


class WriteExcel:
    """
    写入Excel
    """

    def __init__(self, filename, wwb=None):
        self.filename = filename
        # 创建工作簿
        self.wwb = wwb if wwb else xlwt.Workbook(filename)

    def add_sheet(self, sheet_name):
        """添加一个工作表"""
        worksheet = self.wwb.add_sheet(sheet_name)
        return worksheet

    def set_col_width(self, datas, worksheet):
        """
        自动设置列宽

        :param datas:
        :param worksheet:
        :return:
        """
        width_list = []

        # 获取每列最大数据宽度
        for data in zip(*datas):
            # 2340默认宽度
            max_len = 2340
            for txt in data:
                # width = 256 * 20    # 256为衡量单位，20表示20个字符宽度
                if max_len < len(str(txt)) * 256:
                    max_len = len(str(txt)) * 256
            width_list.append(max_len)

        # 设置列宽
        for i in range(0, len(width_list)):
            worksheet.col(i).width = width_list[i]

    def set_style(self):
        # TODO
        pass

    def write_data(self, datas, worksheet):
        """
        写入数据
        :param datas:[[,...],...]
        :return:
        """
        try:
            for row in range(len(datas)):
                # TODO 设置表头格式
                if datas[row] is None:
                    continue
                data = datas[row]
                for col in range(len(data)):
                    if data[col] is None:
                        continue
                    worksheet.write(row, col, data[col])

            # 设置列宽
            self.set_col_width(datas, worksheet)
        except Exception:
            raise

    def save(self):
        """
        保存文件
        """

        while True:
            try:
                self.wwb.save(self.filename)
                print('SAVE SUCCESS IN %s' % self.filename)
                break
            except PermissionError:
                print('其它程序正在使用此文件，进程无法访问，请关闭。')
                time.sleep(2)
            # except Exception as err:
            #     print('保存失败', err)
        # 校验文件是否保存成功
        if os.path.exists(self.filename):
            return True
        return False


class EditManage(ReadExcel, WriteExcel):
    def __init__(self, filename):
        # 读取Excel对象
        rwb = xlrd.open_workbook(filename, formatting_info=True)
        # 复制得到 写入Excel的workbook对象
        wwb = copy(rwb)
        ReadExcel.__init__(self, filename, rwb)
        WriteExcel.__init__(self, filename, wwb)


def save_info(file_name, sheet_name, datas, cover=False, toOpen=True):
    """
    保存数据到Excel

    :param file_name: 文件名
    :param sheet_name: 表名
    :param datas: 数据[[]]
    :param cover: 是否覆盖文件,否的话追加新表
    :return: 文件名
    """
    # 防止检测不到文件是否存在
    if not file_name[-4:] == '.xls':
        file_name += '.xls'

    if os.path.exists(file_name) and not cover:
        # 在Excel里新增一个表(表名不能重复)
        excel = EditManage(file_name)
    else:
        # 直接覆盖或创建新文件
        excel = WriteExcel(file_name)

    sheet = excel.add_sheet(sheet_name)
    excel.write_data(datas, sheet)
    excel.save()
    if toOpen:
        # 打开文件
        os.system('"%s"' % file_name)
    return file_name


@print_def
def get_excel_data(file_name, sheet_name=None):
    """
    获取Excel数据
    :param file_name:
    :param sheet_name:
    :return:{sheetname:[[1,2,...],...],...}
    """
    ex = ReadExcel(file_name)
    ret = {}
    if sheet_name:
        data = ex.get_datas(sheet_name)
        ret[sheet_name] = data
    else:
        sheets_name = ex.get_sheets_name()
        for sheet_name in sheets_name:
            data = ex.get_datas(sheet_name)
            ret[sheet_name] = data
    return ret


if __name__ == '__main__':
    file0 = r'E:\tmp.xls'
    file1 = r'D:\task\20190312 整理项目中openstack的api文档\项目中openstack的api补充文档.xlsx'
    # datas = [['12000000000000000003', None, 43, 5, 45], [1, 23]]

    # save_info(file0, 'test11113', datas, False)
    # get_excel_data(file0, 'test11113')
    data = get_excel_data(file1)
    # print(data)
    pass
