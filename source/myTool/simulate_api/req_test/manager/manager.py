#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: manager
@time: 2019/7/9 15:18
@desc:
"""
import requests, json
import pprint
from req_test.common.configs import manager

HOST = manager.host
PORT = manager.port
URL_PRE = 'http://%s:%s/api/csg/v1/' % (HOST, PORT)


# HOST = "169.254.219.4"


def auth():
    url = "%s/auth/token" % URL_PRE
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    request_param = {
        "username": "zhaner",
        "password": "1111111"
    }
    response = requests.post(url, data=json.dumps(request_param), headers=headers)
    # print(response.text)
    data = json.loads(response.text)
    print(data)
    return data['data']['token']


def req_get(uri, data={}):
    url = 'http://%s:8081/api/csg/v1' % HOST + uri
    token = auth()
    # token =''
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'X-ACCESS-TOKEN': token}
    response = requests.get(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def post(uri, data):
    url = 'http://%s:8081/api/csg/v1' % HOST + uri
    token = auth()
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'X-ACCESS-TOKEN': token}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def put(uri, data):
    url = 'http://%s:8081/api/csg/v1/monitor' % HOST + uri
    token = auth()
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'X-ACCESS-TOKEN': token}
    response = requests.put(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def delete(uri, data):
    url = 'http://%s:8081/api/csg/v1/' % HOST + uri
    token = auth()
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               'X-ACCESS-TOKEN': token}
    response = requests.delete(url, data=json.dumps(data), headers=headers)
    if response.text:
        res = json.loads(response.text)
        pprint.pprint(res)
        return res
    else:
        print(response.content)
        print(response)


def alertTp():
    url = 'http://localHOST:8081/api/csg/v1/monitor/alertTp/'
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               "X-ACCESS-TOKEN": auth()}
    print(headers)
    request_param = [{
        "currentPage": "1",
        "pageSize": "10"
    }]
    response = requests.get(url, data=json.dumps(request_param), headers=headers)
    data = json.loads(response.text)
    pprint.pprint(data)
    return


def alertTp2():
    url = 'http://localHOST:8081/api/csg/v1/monitor/alertTp/55'
    headers = {'Content-Type': 'application/json;charset=UTF-8',
               "X-ACCESS-TOKEN": auth()}
    request_param = {}
    response = requests.get(url, data=json.dumps(request_param), headers=headers)
    data = json.loads(response.text)
    pprint.pprint(data)
    return


def alarm():
    uri = '/monitor/alarm/'
    request_param = {
        "startTime": "2019-07-12 18:00:00",
        "currentPage": "1",
        "pageSize": "2"
    }
    return req_get(uri, request_param)


def add_alarm():
    uri = '/alarm'
    request_param = {
    }
    return post(uri, request_param)


def alarm_test():
    uri = 'alarmTest'
    request_param = {}
    return post(uri, request_param)


def rate():
    uri = '/service/rates/44'
    return req_get(uri, {})


def add_rate():
    uri = '/service/rates'
    return post(uri, {"id": 63, "evaluation": 5})


def get_rate():
    uri = '/service/rates/63'
    return req_get(uri)


def del_alarm():
    uri = '/monitor/alarm/1'
    return delete(uri, {})


def resource_apply():
    uri = '/api/csg/v1/service/resourceApprove'
    return post(uri,{})


if __name__ == '__main__':
    pass
    # token = auth()
    # alertTp()
    # alertTp2()
    # del_alarm()
    # alarm()
    # alarm_test()
    # rate()
    # add_rate()
    # get_rate()
    resource_apply()
