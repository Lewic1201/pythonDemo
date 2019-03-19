# !/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP
import time
import tarfile

"""
上传下载文件
"""


def ftpconnect(host, username, password):
    """
    :param host:
    :param username:
    :param password:
    :return:
    """
    ftp = FTP()
    # ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, 21)  # 连接
    ftp.login(username, password)  # 登录，如果匿名登录则用空串代替即可
    return ftp


def downloadfile(ftp, remotepath, localpath):
    """
    :param ftp: 已经连接的ftp对象
    :param remotepath: 远端目录
    :param localpath: 本地目录
    :return:
    """
    bufsize = 1024  # 设置缓冲块大小
    with open(localpath, 'wb') as fp:  # 以写模式在本地打开文件
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
        ftp.set_debuglevel(0)  # 关闭调试


def uploadfile(ftp, remotepath, localpath):
    """
    :param ftp: 已经连接的ftp对象
    :param remotepath: 远端目录
    :param localpath: 本地目录
    :return:
    """
    bufsize = 1024
    with open(localpath, 'rb') as fp:
        ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
        ftp.set_debuglevel(0)


if __name__ == "__main__":
    ftp = ftpconnect("******", "***", "***")
    downloadfile(ftp, "***", "***")
    uploadfile(ftp, "***", "***")

    ftp.quit()
