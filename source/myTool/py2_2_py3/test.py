#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 11:30
# @Author  : Lewic
# @File    : inheritDemo.py
# @Software: PyCharm Community Edition


class A(object):
    def go(self):
        print("go A go!")

    def stop(self):
        print("stop A stop!")

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        # super(B, self).go()
        print("go B go!")


class C(A):
    def go(self):
        # super(C, self).go()
        print("go C go!")

    def stop(self):
        super(C, self).stop()
        print("stop C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("go D go!")

    def stop(self):
        super(D, self).stop()
        print("stop D stop!")

    def pause(self):
        print("wait D wait!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

# 说明下列代码的输出结果

a.go()
print('------------')
b.go()
print('------------')
c.go()
print('------------')
d.go()
print('------------')
e.go()

# a.stop()
# b.stop()
# c.stop()
# d.stop()
# e.stop()
#
# a.pause()
# b.pause()
# c.pause()
# d.pause()
# e.pause()
