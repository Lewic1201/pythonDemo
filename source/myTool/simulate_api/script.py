#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
@author: Lewic
@file: flasks
@time: 2019/7/3 21:01
@desc: 模拟接口返回值
"""

import json
import schedule
import time
import datetime

from source.myTool.simulate_api.mq.send import send_mq

from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import redirect
from flask import url_for

app = Flask(__name__)


def init():
    schedule.every(30).seconds.do(send_mq())
    while True:
        schedule.run_pending()


@app.route('/api/monitor/monitorAlarm', methods=['POST', 'GET'])
def monitor_alarm():
    data = {
        'code': '200',
        'success': True,
        'id': '1231'
    }
    # a = render_template('index.html',res=data)
    res = Response(json.dumps(data), mimetype='application/json')
    print(res)
    return res


@app.route('/api/monitor/notifications', methods=['POST', 'GET'])
def notifications():
    data = {
        'code': '200',
        'success': True,
        'data': {
            'notificationName': '通知',
            'id': '123456',
            'monitorName': 'cpu监控',
            'monitorRule': 'cpu',
            'monitorObj': 'host',
            'createdTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'value': '80'
        }
    }
    # a = render_template('index.html',res=data)
    res = Response(json.dumps(data), mimetype='application/json')
    return res


@app.route('/api/monitor/monitorAlarm', methods=['POST'])
def monitorAlarm():
    data = {
        'code': '200',
        'success': True,
        'id': '123456789'
    }
    # a = render_template('index.html',res=data)
    res = Response(json.dumps(data), mimetype='application/json')
    return res


@app.route('/api/monitor/monitorAlarm', methods=['PUT'])
def monitorAlarm2():
    data = {
        'code': '200',
        'success': True,
    }
    # a = render_template('index.html',res=data)
    res = Response(json.dumps(data), mimetype='application/json')
    return res


if __name__ == '__main__':
    # init()
    app.run(host="localhost", port=9100, debug=True)
