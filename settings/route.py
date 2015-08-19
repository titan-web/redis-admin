#! /usr/bin/env python
# -*- code: utf-8 -*-
"""
Router
"""
__author__ = 'v-tanjingfeng'

from redisadmin.BaseStaticFileHandler import BaseStaticFileHandler


handlers = [
    (r"/", BaseStaticFileHandler)
]