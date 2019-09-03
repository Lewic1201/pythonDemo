#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: monitor
@time: 2019/7/10 9:56
@desc:
"""
import requests
import json
import pprint

host = 'localhost'
port = '8082'

url_prefix = 'http://%s:%s/' % (host, port)


def req_get(uri, data={}, prefix=url_prefix, is_token=False):
    if 'http://' not in uri:
        url = prefix + uri
    else:
        url = uri

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    if is_token:
        token = ''
        headers['token'] = token
    response = requests.get(url, data=json.dumps(data), headers=headers)

    if response.text:
        try:
            res = json.loads(response.text)
        except Exception as e:
            res = response.text
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def post(uri, data={}, prefix=url_prefix, is_token=False):
    url = prefix + uri

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    if is_token:
        token = ''
        headers['token'] = token

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def put(uri, data={}, prefix=url_prefix, is_token=False):
    url = prefix + uri

    headers = {'Content-Type': 'application/json;charset=UTF-8'}

    if is_token:
        token = ''
        headers['token'] = token

    response = requests.put(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def alarm_test():
    uri = 'alarmTest'
    req_get(uri)


# def alert_tp():
#     uri = 'http://localhost:8081/api/csg/v1/monitor/alert_tp/55'
#     body = {"id": 55}
#     req_get(uri, body)


if __name__ == '__main__':
    pass
    alarm_test()
    # alert_tp()
