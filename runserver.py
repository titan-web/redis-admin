#! /usr/bin/env python
# -*- code: utf-8 -*-
"""
Run Tornado Server
"""
__author__ = 'v-tanjingfeng'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=0, help="debug mode", type=int)


class BaseStaticFileHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")


def main():
    handlers = [
        (r"/(.*)", BaseStaticFileHandler, {"path": "www"})
    ]
    tornado.options.parse_command_line()
    server_settings = {'debug': options.debug}
    application = tornado.web.Application(handlers, **server_settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()