#! /usr/bin/env python
# -*- code:utf-8 -*-

__author__ = 'v-tanjingfeng'

import tornado.web


class MonitorHandler(tornado.web.RequestHandler):

    def get(self):
        welcome = "Hello,Torngas!"
        self.render("monitor/index.html", welcome=welcome)


class DebugHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("debug/index.html")