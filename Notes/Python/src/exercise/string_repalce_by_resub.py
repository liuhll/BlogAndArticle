# -*- coding:utf-8 -*-

from re import sub
from itertools import islice

'''
如何调整字符串的文本格式
'''
# 将日志文件中的日期格式转变为美国日期格式mm/dd/yyyy
# 使用正则表达式模块中的sub函数进行替换字符串
with open("./log.log","r") as f:
    for line in islice(f,0,None):
        #print sub("(\d{4})-(\d{2})-(\d{2})",r"\2/\3/\1",line)
        # 可以为每个匹配组起一个别名
        print sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})",r"\g<month>/\g<day>/\g<>",line)
