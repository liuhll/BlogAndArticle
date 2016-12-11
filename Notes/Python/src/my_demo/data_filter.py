# -*- coding:utf-8 -*-

import string
#数组的数据过滤 

# 传统的做法，使用迭代的方式过滤数组  
def filter_iteration():
    data =[1,2,3,4-3,-4,34,3]
    res=[]
    for x in data:
        if x >= 0:
            res.append(x)

    print res


