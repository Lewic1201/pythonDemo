#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 23:47
# @Author  : Administrator
# @File    : socketDemo.py
# @Software: PyCharm
# @context : 实现http

import socket


def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind()


