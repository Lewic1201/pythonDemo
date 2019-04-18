#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:26
# @Author  : Lewic
# @File    : hello.py
# @Software: PyCharm

from flask import Flask, request, render_template, redirect, url_for
from source.application.mainWeb.controller import common

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/countCodeLine')
def show_now_code_line():
    # 显示用户的名称
    res = common.count_code_line()
    return render_template('simple_res.html', res=res)


@app.route('/dirPath')
def dir_path():
    res = common.show_dir_path()
    return render_template('dir_path.html', datas=res)


@app.route('/showRepeatFile', methods=['GET'])
def show_repeat_file():
    getData = request.args
    if 'dirPath' in getData:
        res = common.show_repeat_file(getData['dirPath'])
        return render_template('simple_res.html', res=res)


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


def main():
    app.run(host="localhost", port=8088, debug=True)


if __name__ == '__main__':
    main()
