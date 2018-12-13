# -*- coding: utf-8 -*-
""""""
from card import Card
from person import Person
import os
import pickle
import random
import time
import datetime

"""
信息存储:字典   键为卡号   值person()
起初定义一个user_dict = {}  写入到文件
第一次打开系统  字典为空
再次打开系统  加载所有用的用户信息
"""


class Operation:
    def __init__(self):
        self.load_user()
        self.load_userid()
        print(self.user_dict)

    def load_user(self):
        # 首先判断文件是否存在
        if os.path.exists("user.txt"):
            with open("user.txt", "rb") as f:
                self.user_dict = pickle.load(f)
        else:
            self.user_dict = {}

    def load_userid(self):
        if os.path.exists("userid.txt"):
            with open("userid.txt", "rb") as f:
                self.user_id_dict = pickle.load(f)
        else:
            self.user_id_dict = {}

    def register(self):
        """注册"""
        # 输入姓名
        name = input("请输入您的姓名:")
        # 输入身份证号
        userid = input("请输入您的身份证号:")
        # 输入手机号
        phone = input("请输入您的手机号:")
        # 设置密码
        password = self.get_pwd()
        # 生成卡号
        cardid = self.get_cardid()

        # 生成一张卡
        card = Card(cardid, password, 10000)
        # 通过卡找到用户
        user = Person(name, userid, phone, card)
        self.user_dict[cardid] = user
        self.user_id_dict[userid] = cardid
        print("恭喜%s开卡成功,您的卡号为:%s,卡的额度为%s元!" % (name, cardid, card.money))

    def get_pwd(self):
        """设置密码"""
        while True:
            pwd1 = input("请输入您的密码:")
            pwd2 = input("请确认您的密码:")
            if pwd1 == pwd2:
                return pwd1
            else:
                print("两次密码不一致，请重新输入!")

    def get_cardid(self):
        """生成卡号"""
        while True:
            cardid = random.randint(100000, 999999)
            if cardid not in self.user_dict:
                return cardid

    def query(self):
        """查询功能"""
        # 拿到一张卡
        card = self.get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                print("卡被锁了!")
            else:
                # 检测密码
                if self.check_pwd(card):
                    print("卡内余额%s元" % (card.money))

    def check_pwd(self, card):
        """检测卡密码"""
        count = 1
        while count < 4:
            pwd = input("请输入您的密码:")
            # 判断用户输入的密码是否和卡内的密码一致
            if pwd == card.password:
                return True
            else:
                count += 1
                print("密码错误,还有%s次机会!" % (4 - count))
                if count == 4:
                    card.islock = True
                    print("密码输入三次失败,卡已被冻结!")

    def get_card_info(self):
        """获取卡的信息"""
        cardid = int(input("请输入您的卡号:"))
        if cardid not in self.user_dict:
            return False
        else:
            # 通过卡号找到用户
            user = self.user_dict[cardid]
            # 通过用户找到卡
            card = user.card
            return card

    def repay_money(self):
        """还款"""
        # 拿到一张卡
        card = self.get_card_info()
        # 通过卡找到用户
        user = self.user_dict[card.cardid]
        # 判断卡是否存在
        if not card:
            print("卡不存在!")
        else:
            # 检测卡是否被锁
            if card.islock:
                print("卡被冻结，请先解卡!")
            else:
                print("您存入的账户名为:%s." % (user.name))
                sure = input("确认存款请按1,回主页面请按0:")
                if sure == "1":
                    # 输入存款金额
                    money = int(input("请输入存款金额:"))
                    if money < 0:
                        print("输入的存款金额不正确!")
                    else:
                        card.money += money
                        print("成功存入%s元。" % (money))
                elif sure == "0":
                    return

    def get_money(self):
        """取钱"""
        # 拿到一张卡
        card = self.get_card_info()
        if not card:
            print("卡不存在!")
        else:
            if card.islock:
                print("卡已经被冻结，请先解卡！")
            else:
                if self.check_pwd(card):
                    money = int(input("请输入取款金额:"))
                    if money > 0 and money <= card.money:
                        card.money -= money

                        print("成功取走-%s元,卡内额度为%s元。" % (money, card.money))
                    else:
                        print("输入金额有误,请重新输入!")

    def trans_money(self):
        """转账"""
        card = self.get_card_info()
        if not card:
            print("卡不存在!")
        else:
            if card.islock:
                print("卡已被冻结,请先解卡！")
            else:
                if self.check_pwd(card):
                    otherid = int(input("请输入对方账号:"))
                    if otherid not in self.user_dict:
                        print("刚账号不存在!")
                    else:
                        other_user = self.user_dict[otherid]
                        sure = input("您将给%s进行转账,确认请输入1,返回主菜单输入其他键:" % (other_user.name))
                        if sure == "1":
                            money = int(input("请输入转账金额:"))
                            if money > 0 and money <= card.money:
                                card.money -= money
                                other_user.card.money += money
                                print("您向%s成功转账%s元" % (other_user.name, money))
                            else:
                                print("转账金额有误!")
                        else:
                            return

    def change_pwd(self):
        """改密"""
        card = self.get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                print("账户已被冻结，请先解卡!")
            else:
                choice = input("请选择改密方式:原密码改密:1 身份信息验证:2")
                if choice == "1":
                    if self.check_pwd(card):
                        password = self.get_pwd()
                        card.password = password
                        print("======改密成功=====")
                elif choice == "2":
                    userid = input("请输入身份证号:")
                    user = self.user_dict[card.cardid]
                    if userid == user.userid:
                        password = self.get_pwd()
                        card.password = password
                        print("======改密成功=====")
                    else:
                        print("身份信息有误！")
                else:
                    print("请输入正确的选项!")

    def lock(self):
        """锁卡"""
        card = self.get_card_info()
        if not card:
            print("卡不存在!")
        else:
            if card.islock:
                print("卡已被冻结")
            else:
                choice = input("使用密码冻结:1  使用身份证号冻结:2")
                if choice == "1":
                    if self.check_pwd(card):
                        card.islock = True
                        print("======锁卡成功======")
                elif choice == "2":
                    userid = input("请输入身份证号:")
                    user = self.user_dict[card.cardid]
                    if userid == user.userid:
                        card.islock = True
                        print("======锁卡成功======")

    def unlock(self):
        """解锁"""
        card = self.get_card_info()
        if not card:
            print("卡不存在!")
        else:
            userid = input("请输入身份证号:")
            user = self.user_dict[card.cardid]
            if userid == user.userid:
                card.islock = False
                print("******解卡成功******")

    def new_card(self):
        """补卡"""
        userid = input("请输入您的身份证号:")
        if userid in self.user_id_dict:
            # 通过身份证号找到卡号
            cardid = self.user_id_dict[userid]
            # 通过卡号找到用户
            user = self.user_dict[cardid]
            # 通过用户找到卡
            card = user.card
            # 生成卡号
            new_cardid = self.get_cardid()
            print(new_cardid)
            # 更换字典的键
            self.user_dict[new_cardid] = self.user_dict.pop(card.cardid)
            # 更换卡号
            card.cardid = new_cardid
            # 更换身份证对应的卡号
            self.user_id_dict[userid] = new_cardid
            print(card.cardid)

    def save(self):
        """存储用户信息"""
        with open("user.txt", "wb") as f:
            pickle.dump(self.user_dict, f)
        with open("userid.txt", "wb") as f:
            pickle.dump(self.user_id_dict, f)
