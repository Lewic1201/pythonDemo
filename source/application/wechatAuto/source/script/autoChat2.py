#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 22:48
# @Author  : Lewic
# @File    : autoChat2.py
# @Software: PyCharm Community Edition


import json
import requests
from wxpy import *


def reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "73b9b3ea33654b2dbbceeed64a383d15"
    #73b9b3ea33654b2dbbceeed64a383d15
    #343bad09638b4d799bd876a77fca084b
    payload = {
        "key": api_key,
        "info": text,
        "userid": "666"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return "" + result["text"] + result["url"]
    else:
        return "" + result["text"]


bot = Bot(cache_path=True)  # 登录缓存
print('小新上线')
found = bot.friends().search('cute')
print(found)


@bot.register(found)
def message(msg):
    ret = reply(msg.text)
    return ret


@bot.register(found)
def forward_message(msg):
    ret = reply(msg.text)
    return ret


embed()
