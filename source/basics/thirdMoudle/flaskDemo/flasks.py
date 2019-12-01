#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:26
# @Author  : Lewic
# @File    : hello.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户的名称
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post %d' % post_id


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_form()


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run()
