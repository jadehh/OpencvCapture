#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : samplesMain.py
# @Author   : jade
# @Date     : 2022/6/15 16:32
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from src.samplesProcess import *
import numpy as np
def main(camera_ip,camera_username,camera_passwd,use_gpu):
    rtsp_url = "rtsp://{}:{}@{}:554/h264/ch1/main/av_stream".format(camera_username,camera_passwd,camera_ip)
    videoReadThread = VideoReadThread(rtsp_url,use_gpu)
    videoReadThread.start()