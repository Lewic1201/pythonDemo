#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Lewic
@file: req
@time: 2019/7/13 11:40
@desc:
"""

def auth():
    url = "http://%s:8081/api/csg/v1/auth/token" % host
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    request_param = {
        "username": "test01",
        "password": "1111111"
    }
    response = requests.post(url, data=json.dumps(request_param), headers=headers)
    # print(response.text)
    data = json.loads(response.text)
    print(data)
    return data['data']['token']
