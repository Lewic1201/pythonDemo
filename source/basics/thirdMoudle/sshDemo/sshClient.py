#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 21:50
# @Author  : Administrator
# @File    : sshClient.py
# @Software: PyCharm
# @context : ssh utils tool

import paramiko


class SSHClient:
    def __init__(self):
        self.client = paramiko.SSHClient()

    def ssh_connect(self, hostname, username, password, port=22):
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname, username, password, port)

    def ssh_exec_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        res, err = stdout.read(), stderr.read()
        result = res if res else err
        return result

    def ssh_close(self):
        self.client.close()
