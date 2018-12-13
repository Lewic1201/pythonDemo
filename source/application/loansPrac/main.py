#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
类名:card
属性:卡号,密码,余额

类名:person
属性:姓名，身份证号，手机号，卡

类名:view
属性:无

类名:ATM机功能
"""
from view import View
from operation import Operation

v = View()


def main():
    if v.login():
        o = Operation()
        while True:
            v.opration_view()
            choice = input("请选择需要办理的业务:")
            if choice == "1":  # 开户
                o.register()
            elif choice == "2":  # 查询
                o.query()
            elif choice == "3":  # 还款
                o.repay_money()
            elif choice == "4":  # 取钱
                o.get_money()
            elif choice == "5":  # 转账
                o.trans_money()
            elif choice == "6":  # 改密
                o.change_pwd()
            elif choice == "7":  # 锁卡
                o.lock()
            elif choice == "8":  # 解卡
                o.unlock()
            elif choice == "9":  # 补卡
                o.new_card()
            elif choice == "0":  # 退出
                o.save()
                break


if __name__ == '__main__':
    main()
