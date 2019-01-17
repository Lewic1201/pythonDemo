#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 22:30
# @Author  : Lewic
# @File    : autoChat.py
# @Software: PyCharm Community Edition


import json
import requests
from wxpy import *


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
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


bot = Bot(console_qr=True, cache_path=True)


@bot.register(mp)
def forward_message(msg):
    return auto_reply(msg.text)


embed()