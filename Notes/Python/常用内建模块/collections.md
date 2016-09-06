# collections模块
@(Python内置模块)[集合]

> **集合模块**，提供了许多有用的集合类

## namedtuple
- `namedtuple`是一个函数，它用来创建一个**自定义的`tuple`对象**，并且规定了`tuple`元素的个数，并可以用属性而不是索引来引用`tuple`的某个元素。

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```

- `Point`对象是`tuple`的一种子类

- 具备`tuple的`**不变性**，又可以**根据属性来引用**，使用十分方便

## deque
- `list`存储数据时，按索引访问元素很快，但是**插入和删除元素就很慢了**
   > `list`是**线性存储**，数据量大的时候，插入和删除效率很低

- `deque`是为了高效实现插入和删除操作的`双向列表`，适合用于`队列`和`栈`：
```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```
- `deque`除了实现`list`的`append()`和`pop()`外，还支持`appendleft()`和`popleft()`，
  > 这样就可以非常高效地往头部添加或删除元素

## defaultdict
- 使用`dict`时，如果引用的`Key`不存在，就会抛出`KeyError`
- 如果希望`key`不存在时，返回一个默认值，就可以用`defaultdict：`

```python
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'
```  

## OrderedDict
- `dict`时，`Key`是无序的
- 要保持`Key`的顺序，可以用`OrderedDict`  －－－有序字典
  - `OrderedDict`的`Key`会按照插入的顺序排列，不是`Key`本身排序
- OrderedDict可以实现一个`FIFO（先进先出）`的`dict`，当容量超出限制时，先删除最早添加的`Key`

```python
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)
```

## Counter
- `Counter`是一个简单的计数器
  - Counter实际上也是dict的一个子类
