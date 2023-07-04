#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : samplesProcess.py
# @Author   : jade
# @Date     : 2022/6/15 16:32
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
import cv2
from src.samplesConfig import JadeLog
import os
from threading import Thread
import time
class VideoReadThread(Thread):
    def __init__(self, video_path,use_gpu):
        self.video_path = video_path
        self.use_gpu = use_gpu
        self.reopen_times = 0
        self.capture = None
        JadeLog.INFO(cv2)
        Thread.__init__(self)

    def open_gpu_capture(self):
        if (hasattr(cv2, "cudacodec")):
            try:
                self.capture = cv2.cudacodec.createVideoReader(self.video_path)
                if self.capture.nextFrame()[0]:
                    self.reopen_times = 0
                    JadeLog.INFO(
                        "相机打开成功,使用GPU对视频解码,相机地址为{}".format(self.video_path))
                else:
                    time.sleep(30)
                    self.reopen_times = self.reopen_times + 1
                    self.capture = None
                    JadeLog.ERROR("相机第{}次打开失败,相机地址为{}".format(self.reopen_times, self.video_path))
            except Exception as e:
                if "CUDA_ERROR_FILE_NOT_FOUND" in str(e):
                    JadeLog.ERROR("相机打开失败,检查用户名,密码和IP地址是否正确,相机地址为{}".format(self.video_path))
                elif "CUDA_ERROR_INVALID_DEVICE" in str(e):
                    JadeLog.ERROR("不支持该显卡,请检查显卡驱动环境")
                else:
                    JadeLog.ERROR("未知错误,错误原因为:{}".format(str(e)))
                time.sleep(1)
                os._exit(500)

        else:
            JadeLog.ERROR("opencv没有GPU解码功能,请重新编译OpencvGPU")
            time.sleep(1)
            os._exit(500)

    def GPUReader(self):
        self.open_gpu_capture()
        index = 0
        if self.capture:
            while True:
                try:
                    ret, frame = self.capture.nextFrame()
                    if ret:
                        frame = frame.download()
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                        index = index + 1
                        if index % 100 == 0:
                            JadeLog.INFO("正在使用GPU解码第{}张图片".format(index), True)
                    else:
                        self.open_gpu_capture()
                except:
                    self.open_gpu_capture()



    def opencv_cpu_capture(self):
        self.capture = cv2.VideoCapture(self.video_path)
        if self.capture.isOpened():
            self.reopen_times = 0
            JadeLog.INFO(
                "相机打开成功,使用CPU对视频解码,相机地址为{}".format(self.video_path))
        else:
            time.sleep(30)
            self.reopen_times = self.reopen_times + 1
            self.capture = None
            JadeLog.ERROR("相机第{}次打开失败,相机地址为{}".format(self.reopen_times, self.video_path))

    def CPUReader(self):
        self.opencv_cpu_capture()
        index = 0
        if self.capture:
            while True:
                try:
                    ret, frame = self.capture.read()
                    if ret:
                        index = index + 1
                        if index % 100 == 0:
                            JadeLog.INFO("正在使用CPU解码第{}张图片".format(index), True)
                    else:
                        self.opencv_cpu_capture()
                except Exception as e:
                    print(e)
                    self.opencv_cpu_capture()


    def run(self):
        if self.use_gpu == "True":
            self.GPUReader()
        else:
            self.CPUReader()

