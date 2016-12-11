# -*- coding:UTF-8 -*-

from collections import OrderedDict
from random import randint
from time import time

d = OrderedDict()
players = list("ABCDEFGH")
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0,7 - i))
    end = time()
    print i+1, p ,end - start
    d[p] = (i+i,end - start)

print 
print '-' * 40

for item in d:
    print item,d[item]


