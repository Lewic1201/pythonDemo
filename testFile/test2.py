a = 'import tornado.httpserver\r\nimport tornado.ioloop\r\nimport tornado.options\r\nimport tornado.web\r\n\r\nfrom tornado.options import define, options\r\ndefine("port", default=8000, help="run on the given port", type=int)\r\n\r\nclass IndexHandler(tornado.web.RequestHandler):\r\n    def get(self):\r\n        greeting = self.get_argument(\'greeting\', \'Hello\')\r\n        self.write(greeting + \', friendly user!\')\r\n\r\nif __name__ == "__main__":\r\n    tornado.options.parse_command_line()\r\n    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])\r\n    http_server = tornado.httpserver.HTTPServer(app)\r\n    http_server.listen(options.port)\r\n    tornado.ioloop.IOLoop.instance().start()'
print(a)

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()