#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 10:46
# @Author  : li_panfeng
# @File    : setting.py
# @Software: PyCharm
# @context : https://www.cnblogs.com/mysql-dba/p/6070258.html


# 调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://username:password@ip:port/dbname"

