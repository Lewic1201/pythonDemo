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
err_message = 'warning: '+'\033[5;31;0m'+'file "'+file_name+'" not found'+'\033[0m'
message = 'info: '+'\033[5;33;0m'+file_name+'\033[5;34;0m'+' ---->>>> '+'\033[5;33;0m'+new_name+'\033[0m'
print(err_message)
print(message)