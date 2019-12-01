#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 13:09
# @Author  : Administrator
# @File    : ffmpegDeal.py
# @Software: PyCharm
# @context :


import PIL.Image as Image
import pylab
import imageio
# 注释的代码执行一次就好，以后都会默认下载完成
# imageio.plugins.ffmpeg.download()  #第一次运行是删除注释，下载ffmpeg工具
import skimage
import numpy as np
import os
from subprocess import call
from tqdm import tqdm
import pandas as pd


# 视频的绝对路径和图片存储的目标路径
def extract_frames(src_path, target_path):
    new_path = target_path

    for video_name in tqdm(os.listdir(src_path)):
        # video_name = "ZJL35.mp4"
        filename = src_path + video_name
        cur_new_path = new_path + video_name.split('.')[0] + '/'
        if not os.path.exists(cur_new_path):
            os.mkdir(cur_new_path)
        dest = cur_new_path + video_name.split('.')[0] + '-%04d.jpg'
        call(["ffmpeg", "-i", filename, "-r", "5", dest])  # 这里的5为5fps，帧率可修改

