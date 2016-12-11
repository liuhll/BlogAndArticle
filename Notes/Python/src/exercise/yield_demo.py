# -*- coding:UTF-8 -*-

def f():
    '''
    - 包含 `yield` 关键字的函数 成为一个生成器函数
    - 生成器对象既实现了迭代器接口 也实现了可迭代接口
    - 专有方法__iter__()返回的就是生成器对象本身
    可以通过 print g.__iter__() is g    # ->返回True 得到验证
    '''
    print "in f(). 1"
    yield 1

    print "in f(). 2"
    yield 2

    print "in f(). 3"
    yield 3

# g = f()

# print g.__iter__() is g

# print g.next()

# for x in g:
#     x # or print x     


class PrimeNumber(object):
    def __init__(self,startNum,endNum):
        self.startNum = startNum
        self.endNum = endNum

    def isPrimeNumber(self,k):
        if k < 2:
            return False
        for i in xrange(2,k):
            if k % i == 0:
                return False
        return True    


    def __iter__(self):
        for k in xrange(self.startNum,self.endNum + 1):
            if self.isPrimeNumber(k):
                yield k
                

for x in PrimeNumber(1,100):
    print x                                  