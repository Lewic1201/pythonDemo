#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/5 17:02
# @Author  : Administrator
# @File    : person.py
# @Software: PyCharm
# @context :

from card import Card


class Person:
    def __init__(self, name, userId, phone, card):
        self.name = name
        self.userId = userId
        self.phone = phone
        self.card = card

    def register(self):
        """注册"""
        # 输入姓名
        name = input("请输入您的姓名:")
        # 输入身份证号
        userId = input("请输入您的身份证号:")
        # 输入手机号
        phone = input("请输入您的手机号:")
        # 设置密码
        password = self.set_pwd()
        # 生成卡号
        cardid = self.set_cardid()

        # 生成一张卡
        card = Card(cardid, password, 10000)
        # 通过卡找到用户
        user = Person(name, userid, phone, card)
        self.user_dict[cardid] = user
        self.user_id_dict[userid] = cardid
        print("恭喜%s开卡成功,您的卡号为:%s,卡的额度为%s元!" % (name, cardid, card.money))

