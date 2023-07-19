#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : packing.py
# @Author   : jade
# @Date     : 2022/6/15 17:17
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from jade import *
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--extra_sys_str', type=str,
                        default="/usr/local/opencv-4.5.2-gpu-cuda11.2-cudnn8,/usr/local/opencv-4.5.2/,/opencv-4.8.0/build/lib/python3,/usr/local/opencv,/usr/local/site-packages")  ## sys.path.append需要额外打包的路径

    parser.add_argument('--extra_path_list', type=list,
                        default=[])  ## 需要额外打包的路径

    parser.add_argument('--use_jade_log', type=str,
                        default="True")  ##是否使用JadeLog
    parser.add_argument('--full', type=str,
                        default="True")  ## 打包成一个完成的包
    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效

    parser.add_argument('--app_version', type=str,
                        default=get_app_version())  ##需要打包的文件名称
    parser.add_argument('--app_name', type=str,
                        default="OpencvCapture")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="OpencvCapture")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="False")  ## 是否打包成AppImage
    parser.add_argument('--lib_path', type=str, default="")  ## 是否lib包分开打包
    parser.add_argument('--is_qt', type=str, default="False")  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument('--exclude_files', type=str, default="")  ## 指定编译的文件
    parser.add_argument("--zip_lib",type=str,default='False')
    parser.add_argument('--main', type=str, default="from samplesMain import main\n"
                                                    "import os\n"
                                                    "import argparse\n"
                                                    "if __name__ == '__main__':\n"
                                                    "\tparser = argparse.ArgumentParser()\n"
                                                    "\tparser.add_argument('-camera_ip', type=str, help='please input camera ip')\n"
                                                    "\tparser.add_argument('-camera_username', type=str, help='please input camera username')\n"
                                                    "\tparser.add_argument('-camera_passwd', type=str, help='please input camera passwd')\n"
                                                    "\tparser.add_argument('--use_gpu', type=str, help='please input use_gpu',default='False')\n" \
                                                    "\targs = parser.parse_args()\n" \
                                                    "\tif args.camera_ip is None or args.camera_username is None or args.camera_passwd is None:\n" \
                                                    "\t\tprint('请输入指定的参数')\n" \
                                                    "\t\tos._exit(0)\n" \
                                                    "\telse:\n" \
                                                    "\t\tmain(args.camera_ip,args.camera_username,args.camera_passwd,args.use_gpu)\n")
    args = parser.parse_args()
    build(args)
    packAPP(args)
    zip_lib_package(args)


