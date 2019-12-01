#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 11:18
# @Author  : li_panfeng
# @File    : dbutil.py
# @Software: PyCharm
# @context : 

import sqlite3

con = sqlite3.connect('d:/test.db3')  # test.db3存在则直接读取，不存在则创建
cur = con.cursor()  # 游标，可以认为类似于recordset
cur.execute('CREATE TABLE Student(Stuid TEXT, Age INTERGER, Name TEXT)')

cur.execute('INSERT INTO Student VALUES("00001", 20, "Lucy")')
cur.execute('INSERT INTO Student VALUES("00002", 21, "Lily")')
con.commit()
cur.execute('SELECT * FROM Student')

con.text_factory = str  # sqlite默认为unicode输出，此处指定为str，即python默认的utf-8
print(cur.fetchone())
print(cur.fetchall())
cur.close()


# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./mytest1.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''

sql = '''create table students (
        name text,
        username text,
        id int)'''

cursor.execute(sql)

# '''使用游标关闭数据库的链接'''
cursor.close()
