# itertools

## itertools
- 会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出

```python
>>> import itertools
>>> natuals = itertools.count(1)
>>> for n in natuals:
...     print n
...
1
2
3
...
```
## cycle()
- `cycle()`会把传入的一个序列无限重复下去

## repeat()
- 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
```python
>>> ns = itertools.repeat('A', 10)
>>> for n in ns:
...     print n
...
打印10次'A'
```

## takewhile()

## chain()
- chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
```python
for c in itertools.chain('ABC', 'XYZ'):
    print c
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
```

## groupby()

## imap()
- `imap()`和`map()`的区别在于，`imap()`可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。

## filter()

- `ifilter()`就是`filter()`的惰性实现。