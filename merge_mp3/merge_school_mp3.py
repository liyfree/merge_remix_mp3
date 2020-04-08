#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os, re
from pydub import AudioSegment

input_dir = 'F:\\python处理音频\\院校\\before\\非重点院校\\综合类6'
out_dir = 'F:\\python处理音频\\院校\\after\\非重点院校\\综合类6'

start_mp3 = AudioSegment.from_mp3('F:\\python处理音频\\院校\\开始结尾\\前缀.mp3')
end_mp3 = AudioSegment.from_mp3('F:\\python处理音频\\院校\\开始结尾\\后缀.mp3')

mp3_list = os.listdir(input_dir)
print('开始处理')
print('*' * 50)
for each_mp3 in mp3_list:
    filename = re.findall(r"(.*?)\.mp3", each_mp3)  # 取出.mp3后缀的文件名
    if filename:
        print('正在处理' + each_mp3 + '......')
        filename[0] += '.mp3'
        mp3 = AudioSegment.from_mp3(input_dir + '\\' + filename[0])  # 打开mp3文件
        out_mp3 = start_mp3 + mp3 + end_mp3
        out_mp3.export(out_dir + '\\' + filename[0], format='mp3')
        print('处理完成')
        print('*' * 50)
print('全部处理结束！！！！！！！！！！！！！！！')
