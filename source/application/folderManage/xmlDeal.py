#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/15 16:13
# @Author  : Administrator
# @File    : xmlDeal.py
# @Software: PyCharm
# @context :

# coding=utf-8

# 通过minidom解析xml文件
import xml.dom.minidom as xmldom
import os
import codecs
# from pprint import pprint as print
from source.utils.file_manager import FileManage
import re
import chardet
import math
import subprocess
import pickle
from shutil import copyfile


#
# '''
# XML文件读取
# <?xml version="1.0" encoding="utf-8"?>
# <catalog>
#     <maxid>4</maxid>
#     <login username="pytest" passwd='123456'>dasdas
#         <caption>Python</caption>
#         <item id="4">
#             <caption>测试</caption>
#         </item>
#     </login>
#     <item id="2">
#         <caption>Zope</caption>
#     </item>
# </catalog>
#
# '''

def test_xml():
    xmlfilepath = os.path.abspath("test.xml")
    print("xml文件路径：", xmlfilepath)

    # 得到文档对象
    domobj = xmldom.parse(xmlfilepath)
    print("xmldom.parse:", type(domobj))
    # 得到元素对象
    elementobj = domobj.documentElement
    print("domobj.documentElement:", type(elementobj))

    # 获得子标签
    subElementObj = elementobj.getElementsByTagName("login")
    print("getElementsByTagName:", type(subElementObj))

    print(len(subElementObj))
    # 获得标签属性值
    print(subElementObj[0].getAttribute("username"))
    print(subElementObj[0].getAttribute("passwd"))

    # 区分相同标签名的标签
    subElementObj1 = elementobj.getElementsByTagName("caption")
    for i in range(len(subElementObj1)):
        print("subElementObj1[i]:", type(subElementObj1[i]))
        print(subElementObj1[i].firstChild.data)  # 显示标签对之间的数据


def get_xml(path):
    xmlfilepath = os.path.abspath(path)
    # print("xml文件路径：", xmlfilepath)
    domobj = xmldom.parse(xmlfilepath)
    elementobj = domobj.documentElement
    subElementObj = elementobj.getElementsByTagName("ModMetaData")
    # print(subElementObj)
    name = elementobj.getElementsByTagName("name")
    print(type(name[0]))


path = r'E:\GAME\RimWorld_ALL\RimWorld_used\MODS'


def deal():
    fm = FileManage(path)
    about_file_list = fm.get_files_by_name(r'[aA]bout.xml', nameorpath=True)
    for f in about_file_list:
        pass
        # get_xml(f)
        # print(f)
        # rename_about_name(f)
        file_encode = get_encoding(f)
        print(file_encode)
        if file_encode == 'GB2312':
            try:
                os.startfile(f)
                convert(f, f)
                print('GB2312:\t' + f)
            except Exception as e:
                print(e)
                print(f)

        # elif file_encode == 'ascii':
        #     try:
        #         os.startfile(f)
        #         # convert(f, f,in_code='ascii')
        #         print('ascii:\t' + f)
        #     except Exception as e:
        #         print(e)
        #         print(f)
        # elif file_encode == 'ISO-8859-1':
        #     try:
        #         os.startfile(f)
        #         # convert(f, f,in_code='ISO-8859-1')
        #         print('ISO-8859-1:\t' + f)
        #     except Exception as e:
        #         print(e)
        #         print(f)

    # testf = about_file_list[0]
    # get_xml(testf)


def bak_file():
    with open('dump.txt', 'rb') as get_file:
        about_file_list = pickle.load(get_file)

    for f in about_file_list:
        os.system('copy "%s" "%s_bak"' % (f, f))
        print(f)


def open_file(page_num=21):
    # fm = FileManage(path)
    # about_file_list = fm.get_files_by_name(r'[aA]bout.xml', nameorpath=True)
    # with open('dump.txt', 'wb') as save_file:
    #     pickle.dump(about_file_list, save_file)

    with open('dump.txt', 'rb') as get_file:
        about_file_list = pickle.load(get_file)

    start, end = page(len(about_file_list), 10, page_num)
    for i in range(start, end):
        f = about_file_list[i]

        file_encode = get_encoding(f)
        print(i, file_encode, f)
        # if file_encode == 'GB2312':
        #     convert(f, f)

        os.startfile(f)
        #
        # os.startfile(f+'_bak')


def page(count, m, n):
    """每页显示m条数据，当前显示第n页"""
    page_count = (count + (m - 1)) // m
    if n > page_count:
        return n * m - m, count + 1
    return n * m - m, n * m


def paginator(current_page, num_page, max_page=10):
    middle = math.ceil(max_page / 2)
    # 一种特殊情况
    # 总页数,小于最大页数
    if num_page < max_page:
        start = 1
        end = num_page
    else:
        # 一般情况
        # 当前页在头部的时候
        if current_page <= middle:
            start = 1
            end = max_page
        # 当前页在中间时
        elif (current_page > middle) & (current_page < num_page - middle + 1):
            start = current_page - middle
            end = current_page + middle - 1
        else:
            # 当前页在尾部
            start = num_page - max_page + 1
            end = num_page
    return start, end


def rename_about_name(file):
    try:
        with open(file, encoding='utf8', errors='ignore') as ff:
            lines = ff.readlines()
        for line in lines:
            if re.match(r'<name>.*', line):
                print(line)
    except Exception:
        print(file)
        convert(file, file)
        os.system(r'' + file)


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']


def remove_git_file():
    fm = FileManage(path)
    git_file = fm.get_files_by_name(r'.*\.git.*', nameorpath=False)
    for f in git_file:
        os.remove(f)
        print(f)


def convert(file_name, file, in_code="GBK", out_code="UTF-8", if_bak=True):
    """
    该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到UTF-8
    :param file:    文件路径
    :param in_code:  输入文件格式
    :param out_code: 输出文件格式
    :return:
    """
    out_path = '输出文件路径'
    # try:
    #     os.system('copy "%s" "%s_bak"' % (file_name, file_name))
    # except:
    #     print('copy bug')

    try:

        with codecs.open(file_name, 'r', in_code) as f_in:
            new_content = f_in.read()
            f_out = codecs.open(os.path.join(out_path, file), 'w', out_code)
            f_out.write(new_content)
            f_out.close
    except IOError as err:
        print("I/O error: {0}".format(err))


if __name__ == '__main__':
    pass
    # test_xml()
    # deal()
    remove_git_file()
    # print(page(200, 10, 19))
    # open_file()
    # bak_file()

    # floders = [
    #     r'136量子冷却'
    #     ,r'142万人坑'
    #     ,r'151太阳耀斑护盾'
    #     ,r'152天花板吊灯'
    #     ,r'156恐龙 - A Dog Said补丁'
    #     ,r'159狮鹫'
    #            ]
    #
    # for floder in floders:
    #     ff = r'E:\GAME\RimWorld_ALL\RimWorld_used\MODS\%s\About\About.xml' % floder
    #     convert(ff, ff)
