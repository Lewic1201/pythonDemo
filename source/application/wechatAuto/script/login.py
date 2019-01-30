#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 22:07
# @Author  : Lewic
# @File    : login.py
# @Software: PyCharm Community Edition

from wxpy import *

bot = Bot(cache_path=True)


def login():
    bot = Bot(cache_path=True)
    return bot


def ftp_file(bot):
    bot.file_helper.send("hello")


@bot.register()
def print_message(msg):
    print(msg.text)
    return msg.text


embed()
