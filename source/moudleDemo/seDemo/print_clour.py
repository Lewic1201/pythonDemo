#!/usr/bin/env python
# -- coding: utf-8 --
'''
@author: lewic
@file: print_clour.py
@time: 2018/7/14 21:05
@desc:
'''

file_name = 'sdfgsdf'
new_name = '21312'
err_message = 'warning: ' + '\033[5;31;0m' + 'file "' + file_name + '" not found' + '\033[0m'
message = 'info: ' + '\033[5;33;0m' + file_name + '\033[5;34;0m' + ' ---->>>> ' + '\033[5;33;0m' + new_name + '\033[0m'
print(err_message)
print(message)

import six

print(six.PY2)
print(six.PY3)
if six.PY2:
    # with open('F:\ a.txt', 'a') as f:  # 以写的方式打开
    #     print >> f, "Hello world, I'm writting to file", 11  # 用print往文件描述符里写内容，可以输入数字
    #     # 等价于
    #     f.write("Hello world, I'm writting to file: " + str(11))  # 用write不能输入数字要先str函数转换为字符串或者格式化("%d\n" % i)
    #
    # print >> sys.stderr, "Hello world, I'm writting to file", 11  # 向标准错误输入内容
    pass
