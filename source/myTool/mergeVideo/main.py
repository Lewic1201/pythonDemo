#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 22:02
# @Author  : Administrator
# @File    : main.py
# @Software: PyCharm
# @context : 合并缓存视频


import os
import shutil
import time


def merge(dir_path):
    """
    合并缓存视频
    :param dir_path: 缓存视频路径
    :return:
    """
    # TODO 文件夹校验
    shutil.copytree(dir_path, dir_path + r'_bak')
    dir_path = dir_path + '_bak'

    os.chdir(dir_path)

    try:
        file_list = os.listdir(dir_path)
        int_list = []

        # 找出序号最大的文件
        for file in file_list:
            try:
                fileint = int(file)
            except ValueError:
                fileint = 0
                os.remove(file)
            int_list.append(fileint)
        maxname = max(int_list)
        namelen = len(str(maxname))

        # 修改文件名
        old_list = []
        new_list = []
        for i in range(1, maxname + 1):
            # 给文件名前面加0,防止乱序
            old_list.append(str(i))
            new_list.append(('{:0>%s}' % namelen).format(i))

        # 写入文件
        with open('tmp.bat', 'w') as bat:
            for i in range(maxname):
                cmd = 'ren ' + old_list[i] + ' ' + new_list[i] + '\n'
                bat.write(cmd)

        # 重命名缓存,防止乱序
        rename = os.popen('tmp.bat')
        print(rename.read())
        os.remove('tmp.bat')

        # 校验是否存在额外文件
        file_list = os.listdir(dir_path)
        for file in file_list:
            try:
                int(file)
            except ValueError:
                raise
        # 合并文件
        file_name = os.path.basename(dir_path)[1:-11] + '.mp4'
        # 防止文件名中有特殊符号
        file_name = '"%s"' % file_name
        result = os.popen('copy /b * %s' % file_name)
        print(result.read())

        # 移动到上层目录,去除""
        if os.path.exists(file_name[1:-1]):
            shutil.move(file_name[1:-1], "..\\")
            print('move success')

            # 删除临时文件
            # os.chdir('..\\')
            # os.remove(dir_path)
        else:
            raise Exception('file not exists')

    except Exception as error:
        print(error)
        raise


if __name__ == '__main__':
    # merge('E:\\video\\huancun\\.无名之辈(2018)-云播资源-在线播放---80s手机电影.m3u8.d')
    merge(r'E:\video\huancun\.《西虹市首富》备用DVD - 八哥网手机版.m3u8.d')
    # result = os.popen("ipconfig")
    # print(result.read())
    # print(os.path.exists('0001'))
    # os.chdir("E:\\video")
    # print(os.listdir('./'))
    # os.chdir('..\\')
    # print(os.listdir('./'))
