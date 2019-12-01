#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@author: Lewic
@file: flasks
@time: 2019/7/3 21:01
@desc: 模拟接口返回值
"""

import json

from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/hello1/<username>')
def hello1(username):
    # 显示用户的名称
    return 'User %s' % username


@app.route('/hello2/<int:post_id>')
def hello2(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post %d' % post_id


@app.route('/hello3', methods=['POST', 'GET'])
def hello3():
    data = {
        'success': True,
    }
    res = render_template('index.html', res=data)
    return res


@app.route('/hello4', methods=['POST', 'GET'])
def hello4():
    data = {
        'success': True,
    }
    res = Response(json.dumps(data), mimetype='application/json')
    return res




if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
