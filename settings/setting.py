#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'v-tanjingfeng'

import os

settings = dict(
    template_path=os.path.join(os.path.realpath(os.path.dirname(os.path.dirname(__file__))), "templates"),
    static_path=os.path.join(os.path.realpath(os.path.dirname(os.path.dirname(__file__))), "static"),
    xsrf_cookies=True,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    autoescape=None,
    debug=True,
)
