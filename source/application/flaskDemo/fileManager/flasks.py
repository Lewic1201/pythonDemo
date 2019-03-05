#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:26
# @Author  : Lewic
# @File    : hello.py
# @Software: PyCharm

import os
from flask import Flask, request, render_template
from view import FileService

app = Flask(__name__)
fs = FileService()

@app.route('/')
def index():
    print(os.path.abspath('index.html'))
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello user!'


@app.route('/filelist', methods=['GET', 'POST'])
def get_filelist():
    get_data = request.args
    print('获取的get数据为:',get_data)
    # post_data = request.form
    # print('获取的post数据为:', post_data)

    data = fs.get_filelist(get_data)

    return render_template('fileView.html', data=data)


# @app.route('/filelist', methods=['GET', 'POST'])
# def get_dirlist():
#     # getData = request.args
#     # print('获取的get数据为:',getData)
#     post_data = request.form
#     get_data = request
#     print(get_data)
#     print('获取的post数据为:', post_data)
#     # username = request.form.get('username')
#     # context = request.form.get('context')
#
#     fs = FileService()
#     data = fs.get_filelist()
#
#     return render_template('fileView.html', data=data)


if __name__ == '__main__':
    app.run("0.0.0.0", 5002)
