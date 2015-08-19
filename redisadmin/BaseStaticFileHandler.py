#! /usr/bin/env python
# -*- code:utf-8 -*-

__author__ = 'v-tanjingfeng'

import tornado.web


class BaseStaticFileHandler(tornado.web.RequestHandler):

    def get(self):
        welcome = "Hello,Torngas!"
        self.render("index.html", welcome=welcome)