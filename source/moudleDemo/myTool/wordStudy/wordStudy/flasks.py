#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 22:26
# @Author  : Lewic
# @File    : hello.py
# @Software: PyCharm

import os
from flask import Flask, request, render_template, flash, redirect, url_for
from wordStudy.word import WordManage

app = Flask(__name__)


@app.route('/')
def index():
    print(os.path.abspath('index.html'))
    return render_template('index.html')


@app.route('/hello')
def hello_world():
    return 'Hello World!'



@app.route('/allWord', methods=['GET'])
def message():
    # getData = request.args
    # print('获取的get数据为:',getData)
    mm = WordManage()

    return render_template('word_table.html', datas=mm.datas)


@app.route('/know', methods=['POST'])
def save_msg():
    # getData = request.args
    # print('获取的get数据为:',getData)
    post_data = request.form
    print('获取的post数据为:', post_data)
    username = request.form.get('username')
    context = request.form.get('context')
    mm = WordManage()
    mm.add_message(username, context)
    mm.save_data()

    # 重定向
    return redirect(url_for('message'))


if __name__ == '__main__':
    app.run("0.0.0.0", 5004)
