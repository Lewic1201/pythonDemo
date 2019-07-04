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


@app.route('/api/monitor/monitorAlarm', methods=['POST', 'GET'])
def monitor_alarm():
    data = {
        'code': '200',
        'success': True,
        'id': '1231'
    }
    # a = render_template('index.html',res=data)
    res = Response(json.dumps(data), mimetype='application/json')
    return res


if __name__ == '__main__':
    app.run(host="localhost", port=9100, debug=True)
