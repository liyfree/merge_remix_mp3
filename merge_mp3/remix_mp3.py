#!/usr/bin/env python3
# -*-coding:utf-8-*-
import os
from pydub import AudioSegment


def remix_mp3(input_mp3_dir, out_mp3_dir, background_mp3_dir):
    mp3_list = os.listdir(input_mp3_dir)
    background_mp3 = AudioSegment.from_mp3(background_mp3_dir)
    # 这里叠加背景音是防止背景音时长不够后面出现无背景音
    background_mp3_long = background_mp3 + background_mp3
    print(background_mp3.dBFS)
    # 背景音降低20分贝
    background_mp3 -= 20
    print(background_mp3.dBFS)
    # 获取背景音时长
    len1 = len(background_mp3)

    for mp3_name in mp3_list:
        print('*' * 50)
        print('开始混音')

        # 获取音频去掉后缀的名称
        pre_name = os.path.splitext(mp3_name)[0]
        mp3 = AudioSegment.from_file(input_mp3_dir + '\\' + mp3_name)
        len2 = len(mp3)
        print('背景音时长= {0}'.format(len1 / 1000))
        print('MP3时长= {0}'.format(len2 / 1000))

        # 这里存在背景音时长小于待混音时长，需要添加背景音时长
        if len1 < len2:
            out_mp3 = background_mp3_long.overlay(mp3)
            print('=' * 100)
        else:
            out_mp3 = background_mp3.overlay(mp3)

        # 截取音频时长
        out_mp3 = out_mp3[:len2]
        print('混音后时长= {0}'.format((len(out_mp3)) / 1000))

        out_mp3.export(out_mp3_dir + '\\' + pre_name + '.mp3', format='mp3')

        print('混音完成')
        print('*' * 50)


if __name__ == '__main__':
    input_dir = 'F:\\python混音练习\\待混音MP3'
    out_dir = 'F:\\python混音练习\\混音后MP3'
    background = 'F:\\python混音练习\\背景音\\夜的钢琴曲_背景音.mp3'
    remix_mp3(input_dir, out_dir, background)
