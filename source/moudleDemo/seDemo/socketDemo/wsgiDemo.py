#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 23:51
# @Author  : Administrator
# @File    : wsgiDemo.py
# @Software: PyCharm
# @context :


from wsgiref.simple_server import make_server


def run_server(environ, start_response):
    print(1)
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return '<h1>Hello,web!</h1>'
    return ['<h1>Hello,web!</h1>'.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print("server on port 8000")
    httpd.serve_forever()
