#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : samplesConfig.py
# @Author   : jade
# @Date     : 2022/6/15 16:40
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from jade import JadeLogging
try:
    JadeLog = JadeLogging("log")
except Exception as e:
    print("日志写入失败,失败原因为:{}".format(e))
    pass
