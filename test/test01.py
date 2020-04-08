#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os, re
from pydub import AudioSegment


def join_mp3(input_dir, out_dir, start_mp3_dir, end_mp3_dir):
    # 获取输入目录的MP3文件
    mp3_list = os.listdir(input_dir)
    # 获取开始MP3
    start_mp3 = AudioSegment.from_mp3(start_mp3_dir)
    # 获取结束MP3
    end_mp3 = AudioSegment.from_mp3(end_mp3_dir)

    for mp3_name in mp3_list:
        print('*' * 50)
        print('开始处理')
        # 获取每个待处理的MP3
        mp3 = AudioSegment.from_mp3(input_dir + '\\' + mp3_name)
        # 拼接MP3
        out_mp3 = start_mp3 + mp3 + end_mp3
        out_mp3.export(out_dir + '\\' + mp3_name, format='mp3')
        print('处理完成')
        print('*' * 50)


def join2_mp3(input_dir, out_dir, start_mp3_dir, end_mp3_dir):
    # 获取输入目录的MP3文件
    mp3_list = os.listdir(input_dir)
    # 获取开始MP3
    start_mp3 = AudioSegment.from_mp3(start_mp3_dir)
    # 获取结束MP3
    end_mp3 = AudioSegment.from_mp3(end_mp3_dir)

    for mp3_name in mp3_list:
        print('*' * 50)
        print('开始处理')
        # 获取每个待处理的MP3
        mp3 = AudioSegment.from_mp3(input_dir + '\\' + mp3_name)
        # 拼接MP3
        out_mp3 = start_mp3 + mp3 + end_mp3
        out_mp3.export(out_dir + '\\' + mp3_name, format='mp3')
        print('处理完成')
        print('*' * 50)


if __name__ == '__main__':
    input_dir = 'F:\\python处理音频\\院校\\before\\非重点院校\\综合类6'
    # out_dir = 'F:\\python处理音频\\院校\\after\\非重点院校\\综合类6'
    out_dir = 'out_dir'

    start_mp3_dir = 'F:\\python处理音频\\院校\\开始结尾\\前缀.mp3'
    end_mp3_dir = 'F:\\python处理音频\\院校\\开始结尾\\后缀.mp3'

    join_mp3(input_dir, out_dir, start_mp3_dir, end_mp3_dir)
    print('全部处理完成！')
