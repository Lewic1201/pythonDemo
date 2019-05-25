#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 11:06
# @Author  : Administrator
# @File    : base.py
# @Software: PyCharm
# @context :


import configparser
import os

CFG = configparser.ConfigParser()
CFG.read('base_param.ini')
PATH11 = CFG['path']['config_dir']
PATH21 = CFG['path']['lnk_dir']
PATH22 = CFG['path']['pre_dir']

BAK_FILE = CFG['bak']['file']
BAK_PRE_FILE = CFG['bak']['pre_file']

RE_PRE = [r'.*\\pre\\.*', r'.*\\pre_(mp4|avi)\\.*', r'.*\\java\\.*']
