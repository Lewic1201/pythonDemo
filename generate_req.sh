#!/usr/bin/env bash
# 导出requirements.txt
pip freeze > requirements.txt
# 安装 requirements.txt
pip install -r requirements.txt