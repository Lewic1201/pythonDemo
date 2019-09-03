#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 23:22
# @Author  : Administrator
# @File    : oneLineCode.py
# @Software: PyCharm
# @context :

# 1. 一行代码启动一个Web服务
# python -m SimpleHTTPServer 8080  # python2
# python3 -m http.server 8080  # python3

# 2. 一行代码实现变量值互换
a, b = 1, 2;
a, b = b, a

# 3. 一行代码解决FizzBuzz问题
# FizzBuzz问题：打印数字1到100, 3的倍数打印“Fizz”, 5的倍数打印“Buzz”, 既是3又是5的倍数的打印“FizzBuzz”
# for x in range(1, 101): print("fizz"[x % 3 * 4:]+"buzz"[x % 5 * 4:] or x)

# 一行代码输出特定字符”Love”拼成的心形
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

print('\n'.join([''.join([('ar'.join('S''a')[(x-y) % len('1314')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(13, -11, -1)]))

