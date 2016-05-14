#! /usr/bin/env python
# -*- code: utf-8 -*-
"""
Router
"""

from handlers.monitor.handlers import MonitorHandler, DebugHandler


handlers = [
    (r"/monitor", MonitorHandler),
    (r"/debug", DebugHandler),
]
