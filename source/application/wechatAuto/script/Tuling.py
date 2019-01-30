#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 22:30
# @Author  : Lewic
# @File    : autoChat.py
# @Software: PyCharm Community Edition


import json
import requests


def auto_reply(text):
    """
    调用图灵机器人API，发送消息并获得机器人的回复
    :param text:
    :return:
    """
    url = "http://www.tuling123.com/openapi/api"
    api_key = "343bad09638b4d799bd876a77fca084b"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return "[tuling] " + result["text"]


def console():
    """
    控制台测试
    :return:
    """
    while True:
        send = input("YOU: ")
        if send == 'exit':
            break
        req = auto_reply(send)
        print("HE:", req)

if __name__ == '__main__':
    console()