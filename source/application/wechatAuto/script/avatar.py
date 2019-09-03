#!/usr/bin/env python
# -*- coding:utf-8 -*-
#! python3
"""
@author: Lewic
@file: avatar
@time: 2019/6/27 20:46
@desc:
"""

# coding="utf-8"
from wxpy import *
import math
from PIL import Image
import os


def creat_filepath():
    """创建头像存放文件夹"""
    avatar_dir = os.getcwd() + "\\wechat\\"
    if not os.path.exists(avatar_dir):
        os.makedirs(avatar_dir)
    return avatar_dir


def save_avatar(avatar_dir):
    """初始化机器人，扫码登入"""
    bot = Bot()
    friends = bot.friends(update=True)
    num = 0
    count = len(friends)
    print("您共有 %d 个好友！" % count)
    for friend in friends:
        friend.get_avatar(avatar_dir + "\\" + str(num) + ".jpg")
        num += 1
        percent = int(100 * num / count)
        progress(percent)
    print("")


def joint_avatar(path):
    """拼接头像"""
    # 1、获取文件夹内的头像数目
    length = len(os.listdir(path))
    # 2、设置画布大小
    image_size = 2560
    # 3、设置每个头像的大小
    each_size = math.ceil(2560 / math.floor(math.sqrt(length)))
    # 4、计算所需各行列的头像数目
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new("RGB", (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (each_size * x, each_size * y))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print("头像读取失败")
    img = image.save(os.getcwd() + "/wechat.png")
    print("拼接好友头像完成")


def progress(percent, width=30):
    if percent >= 100:
        percent = 100
    show_str = ('正在下载好友头像：[%%-%ds]' % width) % (int(width * percent / 100) * "#")
    print('\r%s %d%%' % (show_str, percent), end='')


if __name__ == '__main__':
    avatar_dir = creat_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)
