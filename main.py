#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : main.py
# @Author   : jade
# @Date     : 2022/6/15 16:34
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from src.samplesMain import main
import os
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-camera_ip', type=str, help='please input camera ip')
    parser.add_argument('-camera_username', type=str, help='please input camera username')
    parser.add_argument('-camera_passwd', type=str, help='please input camera passwd')
    parser.add_argument('--use_gpu', type=str, help='please input use_gpu',default='False')

    args = parser.parse_args()
    if args.camera_ip is None or args.camera_username is None or args.camera_passwd is None:
        print('请输入指定的参数')
        os._exit(0)
    else:
        main(args.camera_ip,args.camera_username,args.camera_passwd,args.use_gpu)
