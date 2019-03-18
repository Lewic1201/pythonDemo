#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 9:52
# @Author  : li_panfeng
# @File    : demo.py
# @Software: PyCharm
# @context : python win32 简单操作 (这个模块类似于按键精灵)

import win32gui

# 根据类名及标题名查询句柄，
hwnd = win32gui.FindWindow("WeChat", "微信")
# 查找指定句柄的子句柄，后两个参数为子类的类名与标题，如果没有或不确定，可以写None
# hwnd = win32gui.FindWindow(hwnd, None, "sub_class", "sub_title")

# 没有直接修改窗口大小的方式，但可以曲线救国，几个参数分别表示句柄,起始点坐标,宽高度,是否重绘界面 ，如果想改变窗口大小，就必须指定起始点的坐标，没果对起始点坐标没有要求，随便写就可以；如果还想要放在原先的位置，就需要先获取之前的边框位置，再调用该方法即可
win32gui.MoveWindow(hwnd, 20, 20, 405, 756, True)
