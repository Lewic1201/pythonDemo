#!/usr/bin/env bash
# -*- coding: utf-8 -*-

import os


def generate_requirements():
    """
    默认追加到文件中
    :return:
    """
    os.system("pip freeze > ./testFile/req.bak")
    # TODO 将生成的req.bak更新到requirements.txt上,


if __name__ == '__main__':
    generate_requirements()
