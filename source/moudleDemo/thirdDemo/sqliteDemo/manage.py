#!/usr/bin/env python
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
    def __init__(self, db_file='./mytest.db'):
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


    def fetchall(self, sql):
        """查询所有数据"""
        if sql is not None and sql != '':
            cu = self.cursor
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self, sql, data):
        """查询一条数据"""
        if sql is not None and sql != '':
            if data is not None:
                # Do this instead
                d = (data,)
                cu = self.cursor
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, data))
                cu.execute(sql, d)
                r = cu.fetchone()
                if len(r) > 0:
                    for e in range(len(r)):
                        print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    # def update(conn, sql, data):
    #     """更新数据"""
    #     if sql is not None and sql != '':
    #         if data is not None:
    #             cu = get_cursor(conn)
    #             for d in data:
    #                 if SHOW_SQL:
    #                     print('执行sql:[{}],参数:[{}]'.format(sql, d))
    #                 cu.execute(sql, d)
    #                 conn.commit()
    #             close_all(conn, cu)
    #     else:
    #         print('the [{}] is empty or equal None!'.format(sql))
    #
    # def delete(conn, sql, data):
    #     """删除数据"""
    #     if sql is not None and sql != '':
    #         if data is not None:
    #             cu = get_cursor(conn)
    #             for d in data:
    #                 if SHOW_SQL:
    #                     print('执行sql:[{}],参数:[{}]'.format(sql, d))
    #                 cu.execute(sql, d)
    #                 conn.commit()
    #             close_all(conn, cu)
    #     else:
    #         print('the [{}] is empty or equal None!'.format(sql))
    #
    # ############################################################
    # #            数据库操作CRUD     END
    # ############################################################
    #
    # ############################################################
    # #            测试操作     START
    # ############################################################
    # def drop_table_test():
    #     """删除数据库表测试"""
    #     print('删除数据库表测试...')
    #     conn = self.get_conn(DB_FILE_PATH)
    #     drop_table(conn, TABLE_NAME)
    #
    # def create_table_test():
    #     """创建数据库表测试"""
    #     print('创建数据库表测试...')
    #     create_table_sql = """CREATE TABLE `student` (
    #                           `id` int(11) NOT NULL,
    #                           `name` varchar(20) NOT NULL,
    #                           `gender` varchar(4) DEFAULT NULL,
    #                           `age` int(11) DEFAULT NULL,
    #                           `address` varchar(200) DEFAULT NULL,
    #                           `phone` varchar(20) DEFAULT NULL,
    #                            PRIMARY KEY (`id`)
    #                         )"""
    #     conn = self.get_conn(DB_FILE_PATH)
    #     create_table(conn, create_table_sql)
    #
    # def save_test():
    #     """保存数据测试..."""
    #     print('保存数据测试...')
    #     save_sql = """INSERT INTO student values (?, ?, ?, ?, ?, ?)"""
    #     data = [(1, 'Hongten', '男', 20, '广东省广州市', '13423****62'),
    #             (2, 'Tom', '男', 22, '美国旧金山', '15423****63'),
    #             (3, 'Jake', '女', 18, '广东省广州市', '18823****87'),
    #             (4, 'Cate', '女', 21, '广东省广州市', '14323****32')]
    #     conn = self.get_conn(DB_FILE_PATH)
    #     save(conn, save_sql, data)
    #
    # def fetchall_test():
    #     """查询所有数据..."""
    #     print('查询所有数据...')
    #     fetchall_sql = """SELECT * FROM student"""
    #     conn = self.get_conn(DB_FILE_PATH)
    #     fetchall(conn, fetchall_sql)
    #
    # def fetchone_test():
    #     """查询一条数据..."""
    #     print('查询一条数据...')
    #     fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
    #     data = 1
    #     conn = self.get_conn(DB_FILE_PATH)
    #     fetchone(conn, fetchone_sql, data)
    #
    # def update_test():
    #     """更新数据..."""
    #     print('更新数据...')
    #     update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
    #     data = [('HongtenAA', 1),
    #             ('HongtenBB', 2),
    #             ('HongtenCC', 3),
    #             ('HongtenDD', 4)]
    #     conn = self.get_conn(DB_FILE_PATH)
    #     update(conn, update_sql, data)
    #
    # def delete_test():
    #     """删除数据..."""
    #     print('删除数据...')
    #     delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
    #     data = [('HongtenAA', 1),
    #             ('HongtenCC', 3)]
    #     conn = self.get_conn(DB_FILE_PATH)
    #     delete(conn, delete_sql, data)
    #
    # ############################################################
    # #            测试操作     END
    # ############################################################
    #
    # def init():
    #     """初始化方法"""
    #     # 数据库文件绝句路径
    #     global DB_FILE_PATH
    #     DB_FILE_PATH = 'c:\\test\\hongten.db'
    #     # 数据库表名称
    #     global TABLE_NAME
    #     TABLE_NAME = 'student'
    #     # 是否打印sql
    #     global SHOW_SQL
    #     SHOW_SQL = True
    #     print('show_sql : {}'.format(SHOW_SQL))
    #     # 如果存在数据库表，则删除表
    #     drop_table_test()
    #     # 创建数据库表student
    #     create_table_test()
    #     # 向数据库表中插入数据
    #     save_test()

    def create_init(self):
        words = """
CREATE TABLE 'words' (
    'wid' int(8) NOT NULL,
    'index' varchar(2) NOT NULL,
    'queue_num' varchar(4) DEFAULT NULL,
    'en' varchar(50) DEFAULT NULL,
    'ch' varchar(200) DEFAULT NULL,
    'time' varchar(200) DEFAULT NULL,
    'translate_if' int DEFAULT 0,
    'spell_if' int DEFAULT 0,
    'remember' int DEFAULT 0,
    PRIMARY KEY ('wid')
    )
"""
        self.create_table(words)
        student = "create table student('id' int(5),'name' varchar(30))"
        self.create_table(student)
        self.close_all()


if __name__ == '__main__':
    sm = SqliteManage()
    sm.create_init()
