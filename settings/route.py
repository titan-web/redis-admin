#! /usr/bin/env python
# -*- code: utf-8 -*-
"""
Router
"""
__author__ = 'v-tanjingfeng'

from handlers.monitor.Handlers import MonitorHandler, DebugHandler


handlers = [
    (r"/monitor", MonitorHandler),
    (r"/debug", DebugHandler),
]