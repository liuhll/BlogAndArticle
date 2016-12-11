# -*- coding:utf-8 -*-

class FloatRange(object):
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start 
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


# 正向迭代
for x in FloatRange(1,10,0.2):
    print x

print "-"*40

# 逆向迭代,使用python的内置函数 reversed(iter_obj) ，需要可迭代对象实现了专有函数 __reversed__()
for x in reversed(FloatRange(1,10,0.5)):
    print x