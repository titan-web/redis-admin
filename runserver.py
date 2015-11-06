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
from settings.route import handlers
from settings.setting import settings

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="debug mode", type=int)


def main():
    tornado.options.parse_command_line()
    settings['debug'] = options.debug
    application = tornado.web.Application(handlers, **settings)

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()