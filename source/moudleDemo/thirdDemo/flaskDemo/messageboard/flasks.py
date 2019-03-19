#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:26
# @Author  : Lewic
# @File    : hello.py
# @Software: PyCharm

import os
from flask import Flask, request, render_template
from source.moudleDemo.thirdDemo.flaskDemo.messageboard import MessageManage

app = Flask(__name__)


@app.route('/')
def index():
    print(os.path.abspath('index.html'))
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/message', methods=['GET', 'POST'])
def message():
    # getData = request.args
    # print('获取的get数据为:',getData)
    post_data = request.form
    print('获取的post数据为:', post_data)
    username = request.form.get('username')
    context = request.form.get('context')
    mm = MessageManage()
    mm.add_message(username, context)
    mm.save_data()

    # send data
    return render_template('board.html', datas=mm.datas[::-1])


if __name__ == '__main__':
    app.run("0.0.0.0", 5002)
