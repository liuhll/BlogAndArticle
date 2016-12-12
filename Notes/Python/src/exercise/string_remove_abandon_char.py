# -*-coding: utf-8 -*-

# 1.使用字符串的 strip() lstrip() rstrip() 方法
# 缺陷：不能删除中间的字符，只能删除字符串两边的字符
print " sdsd ".strip()
print " sdsd ".lstrip()
print " sdsd ".rstrip()
print "+++++++abc--------".strip("+-")

# 2.删除字符串某个固定位置的字符可以使用切片的方式
s = "abc:123"
print s[:3] + s[4:]

# 3. 使用字符串的replace() 字符串替换方式 或是正则表达式模块下的的re.sub()方法
#  删除任意位置的指定字符
# 字符串只能替换一种字符，如果替换多种的话，则使用re.sub
print s.replace(':','')
from re import sub
s1 = "wew\t\rdsd\t\rdsdw3e\t\r"
print sub('[\t\r]','',s1)


# 4.字符串的translate()方法，可以同时删除多种不同的字符
# translate ->翻译； 作用就是：将一个字符映射成为另外一个字符

import string

transtable = string.maketrans('wew','xyz')
# 第二个参数为指定的要删除的字符
print s1.translate(transtable,"\t\r")