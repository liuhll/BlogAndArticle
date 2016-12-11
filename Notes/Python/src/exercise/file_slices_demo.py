# -*- coding:utf-8 -*-

from itertools import islice

with open("yield_demo.py") as f:
    '''
    读取文件最好的方式还是使用迭代器
    使用 f.readlines()方法，如果文件过大的话，会导致撑爆内存
    如果需要对文件进行切片的话，则通过itertools包下的islice进行  --> 如何对迭代器对象实现切片操作
    '''
    for x in islice(f,4,10):
        print x