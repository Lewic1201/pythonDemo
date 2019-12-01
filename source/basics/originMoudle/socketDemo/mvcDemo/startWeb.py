#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 21:47
# @Author  : Administrator
# @File    : startWeb.py
# @Software: PyCharm
# @context :

from wsgiref.simple_server import make_server
from controller.PersonController import index
from controller.PersonController import home

URI_MAP = {'/index': index,
           '/home': home,
           }


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    current_uri = environ['PATH_INFO']

    if current_uri in URI_MAP.keys():
        return [URI_MAP[current_uri]().encode("utf8")]
    else:
        return ['<h1>404</h1>'.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8001, run_server)
    print("server on port 8001")
    httpd.serve_forever()
