#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os

list = os.listdir('F:\院校解说音频\非重点')
print(len(list))
sql = "select * from jc_xx where XXMC = "

for each in list:
    tuple_sp = os.path.splitext(each)
    print(tuple_sp[0])
    sql += "'" + tuple_sp[0] + "' or XXMC = "
print(sql)
