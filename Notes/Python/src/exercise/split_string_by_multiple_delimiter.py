# -*- coding:utf-8 -*-

# 如何拆分含有多种分隔符的字符串

# 方法1  --》提供了一种解决问题的思路
def mySplit(str,ds):
    res = [str]
    
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)),res)
        res = t
    
    # 只有当字符串为非空的情况下才保留字符串    
    return [x for x in res if x]

s = "dasd;d;xx,da,\tdasda\t|dsd;asfa;|sds,swd,w"

print mySplit(s,";,\t|") 


# 方法2
# 推荐使用正则表达式的方法
import re
print "-" * 40
print re.split("[;,\t|]+",s)