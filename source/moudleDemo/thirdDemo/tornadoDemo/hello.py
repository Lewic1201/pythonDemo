#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/19 11:40
# @Author  : li_panfeng
# @File    : hello.py
# @Software: PyCharm
# @context : 

import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # http://localhost:8000
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
