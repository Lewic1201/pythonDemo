#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 11:28
# @Author  : li_panfeng
# @File    : sqlutil.py
# @Software: PyCharm
# @context : 
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 11:22
# @Author  : li_panfeng
# @File    : manage.py
# @Software: PyCharm
# @context :

import sqlite3
import os

# 是否打印sql
SHOW_SQL = True

class SqliteManage:
    def __init__(self, db_file='./db/web.db'):
        self.db_file = db_file
        self.connect = sqlite3.connect(self.db_file)
        self.cursor = self.connect.cursor()

    def _get_cursor(self):
        return self.cursor

    ############################################################
    #            创建|删除表操作     START
    ############################################################
    def drop_table(self, table):
        """如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！"""
        sql = 'DROP TABLE IF EXISTS ' + table
        if table is not None and table != '':
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu = self._get_cursor()
            cu.execute(sql)
            self.connect.commit()
            print('删除数据库表[{}]成功!'.format(table))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def create_table(self, sql):
        """创建数据库表：student"""
        if sql is not None and sql != '':
            cu = self._get_cursor()
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            self.connect.commit()
            print('create table success!')
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self):
        """关闭数据库游标对象和数据库连接对象"""
        try:
            if self.cursor is not None:
                self.cursor.close()
        finally:
            if self.connect is not None:
                self.connect.close()

    ############################################################
    #            数据库操作CRUD     START
    ############################################################
    def exec(self, sql):
        """执行增删改命令"""
        if sql is not None and sql != '':
            cu = self._get_cursor()
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            self.connect.commit()
            print('create table success!')
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, sql):
        """查询所有数据"""
        if sql is not None and sql != '':
            cu = self.cursor
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            return r

    def create_init(self):
        # 表不存在则创建表
        dirpath = """
CREATE TABLE IF NOT EXISTS 'dirpath'(
    pid INTEGER PRIMARY KEY AUTOINCREMENT,
    path VARCHAR(60) NOT NULL
    )
"""
        self.create_table(dirpath)
        # student = "create table student('id' int(5),'name' varchar(30))"
        # self.create_table(student)


if __name__ == '__main__':
    sm = SqliteManage('../db/web.db')
    sm.create_init()
    sm.exec("insert into dirpath(path) values ('E:/bak')")
    paths = sm.fetchall("select * from dirpath")
    print(paths)
