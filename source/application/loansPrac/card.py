#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/5 16:59
# @Author  : Administrator
# @File    : card.py
# @Software: PyCharm
# @context :
from random import randint
import os
import pickle


class Card:
    def __init__(self, cardId, password, money):
        self.cardId = cardId
        self.password = password
        self.money = money
        self.isLock = False

        # [{time_id:123;borrow:123;refund:0},...]
        self.operation_timestamp = []
        self.limit_money = 10000 - self.get_limit_money()
        self.balance = self.get_limit_money() + self.get_interest()

    def load_user(self):
        # 首先判断文件是否存在
        if os.path.exists("user.txt"):
            with open("user.txt", "rb") as f:
                self.user_dict = pickle.load(f)
        else:
            self.user_dict = {}

    def set_pwd(self):
        """设置密码"""
        while True:
            pwd1 = input("请输入您的密码:")
            pwd2 = input("请确认您的密码:")
            if pwd1 == pwd2:
                return pwd1
            else:
                print("两次密码不一致，请重新输入!")

    def get_cardId(self):
        """生成卡号"""
        while True:
            cardId = randint(100000, 999999)
            if cardId not in self.user_dict:
                return cardId

    def set_change_money(self, change_money, timestamp, flag='b'):
        """ 每次贷款记录到operation_timestamp对象里, flag: b是借,r是还 """
        error_message = ''
        for record in self.operation_timestamp:
            # 过滤重复记录
            if timestamp in record:
                error_message += 'time error or record repeat;'
        a_record = {}
        if error_message is not None:
            a_record['time_id'] = timestamp
            if flag == 'b':
                a_record['borrow'] = change_money
                a_record['refund'] = 0
            elif flag == 'r':
                a_record['borrow'] = 0
                a_record['refund'] = change_money
            else:
                error_message += 'flag error;'
            self.operation_timestamp.append(a_record)
            self.money += change_money
            print('======贷款成功=====')
            print('-' * 50)

    def get_interest(self, now_timestamp):
        """获取每次贷款的利息之合"""
        try:
            interest = 0
            for record in self.operation_timestamp:
                interest += (now_timestamp - record['time_id']) * record['borrow'] * 0.0005
        except Exception:
            print('获取利息失败')
        return interest

    def get_limit_money(self):
        """获取贷款钱数"""
        sum_borrow_money = 0
        for record in self.operation_timestamp:
            sum_borrow_money += record.get('modify_money', 0)
            sum_borrow_money -= record.get('refund', 0)
        return sum_borrow_money
