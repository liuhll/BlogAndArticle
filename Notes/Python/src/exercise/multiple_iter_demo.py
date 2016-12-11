# -*- coding:utf-8 -*-

from random import randint

'''
使用 zip内置函数实现多个可迭代对象的的for并行迭代
'''
chinese = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]
math =  [randint(60, 100) for _ in xrange(40)]

total =[]

for c,e,m in zip(chinese,english,math):
    total.append(c + e + m)


print total


# 使用itertools 包下的chain 函数实现串行迭代

from itertools import chain

class1 = [randint(60,100) for _ in xrange(20)]
class2 = [randint(60,100) for _ in xrange(25)]
class3 = [randint(60,100) for _ in xrange(15)]

count = 0 
for x in chain(class1,class2,class3):
    if x > 90:
        count +=1

print count

