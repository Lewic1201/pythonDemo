#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: task2
@time: 2019/7/4 10:08
@desc:
"""

import random
import json
import time
import datetime

from source.moudleDemo.myTool.simulate_api.mq.send import send_mq


def job1():
    print('Job2:每隔30秒执行一次，每次执行5秒')
    print('Job2-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(5)
    send_mq()
    print('Job2-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('------------------------------------------------------------------------')


def timer(sec, func, *param, is_random=False):
    """
    每n秒执行一次
    """
    while True:
        if is_random:
            sec = random.randint(20, 200)
        print(time.strftime('%Y-%m-%d %X', time.localtime()))
        # yourTask()
        func(*param)
        time.sleep(sec)


def send_notification():
    res = {
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
    json_str = json.dumps(res)
    # print(type(json_str))
    send_mq('notifications', json_str)


if __name__ == '__main__':
    # schedule.every(30).seconds.do(job1)
    # while True:
    #     schedule.run_pending()

    timer(30, send_notification, is_random=True)
