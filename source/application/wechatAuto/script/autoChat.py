#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 22:48
# @Author  : Lewic
# @File    : autoChat2.py
# @Software: PyCharm Community Edition


import json
import requests
# from wxpy import *
from wxpy import Bot
from wxpy import embed
from wxpy import Group, TEXT


def reply(text):
    """
    图灵机器人api
    :param text: 发送文字
    :return: 机器人回答
    :rtype: str
    """
    url = "http://www.tuling123.com/openapi/api"
    api_key = "73b9b3ea33654b2dbbceeed64a383d15"
    # 73b9b3ea33654b2dbbceeed64a383d15
    # 343bad09638b4d799bd876a77fca084b
    payload = {
        "key": api_key,
        "info": text,
        "userid": "666"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    if 'url' in result.keys():
        return "" + result["text"] + result["url"]
    else:
        return "" + result["text"]


# 登录缓存
bot = Bot(cache_path=True)
print('小新上线')


# 查找好友
my_friend = bot.friends().search('cute')[0]
print(my_friend)


# # 发送文本
# my_friend.send('Hello, WeChat!')
# # 发送图片
# my_friend.send_image('my_picture.png')
# # 发送视频
# my_friend.send_video('my_video.mov')
# # 发送文件
# my_friend.send_file('my_file.zip')
# # 以动态的方式发送图片
# my_friend.send('@img@my_picture.png')


@bot.register(my_friend)
def message(msg):
    ret = reply(msg.text)
    return ret


@bot.register(my_friend)
def forward_message(msg):
    ret = reply(msg.text)
    return ret


# 回复 my_friend 发送的消息
@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)


# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)


# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        msg.reply(msg.text)


# 获取所有类型的消息（好友消息、群聊、公众号，不包括任何自己发送的消息）
# 并将获得的消息打印到控制台
@bot.register()
def print_others(msg):
    print(msg)


# 通过机器人对象 Bot 的 chats(), friends()，groups(), mps() 方法, 可分别获取到当前机器人的 所有聊天对象、好友、群聊，以及公众号列表。
bot.chats()
bot.friends()
bot.groups()
bot.mps()

# 堵塞线程 进入Python 命令行 让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()
