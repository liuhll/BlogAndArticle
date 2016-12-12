# -*- coding:utf-8 -*-
# 字符串的对齐方法

# 1. 使用字符串的 ljust() rjust() 居中 center()

# 使用内置函数 格式化方法 format()方法
# - 左对齐format('<20')
# - 右对齐format('>20')
# - 居中对齐format('^20')


# demo

d = {
    "lodDist":100.0,
    "SamllCull":0.04,
    "trllinear":40,
    "farclip":477
}

#1.首先找到字典中字符串字符最长的那一项
# 使用map函数 ,传入内置函数len，得到每一项的字符长度，然后取最大值
# - max(map(len,d.keys()))

w = max(map(len,d.keys()))

for k in d.keys():
    print k.ljust(w), ":", d[k]  

print "*" * 20
for k in d.keys():
    print format(k,'<' + str(w)),":", d[k]    