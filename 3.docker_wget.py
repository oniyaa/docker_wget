#!/usr/bin/env python3
# 功能：
# 使用wget下载，通过docker并行下载

import os


USER_DIR = os.getcwd()

PREFIX_NAME = "list_"      # 读取“list_” 为前缀的文件

list = os.listdir("INPUT")

for x in os.listdir("INPUT"):
    if x.startswith(PREFIX_NAME):
        os.system(f'mkdir OUTPUT/{x}')
        print("run docker ", x)
        os.system(f'docker run -d --rm --name {x} -v {USER_DIR}:/DOWNLOADS oniyaa/dwget wget -i INPUT/{x} -P OUTPUT/{x}')

