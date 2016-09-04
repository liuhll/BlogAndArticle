# IO编程
@(Python)[IO编程]

## 输入和输出
- `IO`在计算机中指`Input/Output`
- IO接口
  - 涉及到**数据交换**的地方，通常是*磁盘*、*网络*等
  - 程序完成**IO操作**会有`Input`和`Output`两个数据流
  > 从磁盘读取文件到内存，就只有`Input操作`，反过来，把数据写到磁盘文件里，就只是一个`Output操作`
### Stream（流）
- 把流想象成一个水管，数据就是水管里的水，但是**只能单向流动**
- `Input Stream`就是数据从外面（磁盘、网络）流进内存
- `Output Stream`就是数据从内存流到外面去

- *CPU和内存的速度远远高于外设的速度*
   > 在IO编程中，就存在**速度严重不匹配的问题**
- 如何解决IO编程中速度不匹配的问题？
  - 同步IO
  > **CPU等着**，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行
  - 异步IO
  > **CPU不等待**，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，**后续代码可以立刻接着执行**

- *同步和异步的区别:* **就在于是否等待IO执行的结果**  

- IO性能：
  > 异步IO来编写程序性能会远远高于同步IO  
  > 异步IO的缺点是编程模型复杂,异步IO的复杂度远远高于同步IO

- IO异步编程中如何通知程序IO读写完成？
  - 回调模式
     > 服务员跑过来找到你
  - 轮询模式
     > 如果服务员发短信通知你，你就得不停地检查手机

> 操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用

## 文件读写
- 读写文件是最常见的IO操作。Python内置了读写文件的函数，*用法和`C`是兼容的*
- 磁盘上读写文件的功能都是**由操作系统提供的**，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个`文件对象`（通常称为`文件描述符`）

### 读文件
- 通过操作系统提供的接口从这个文件对象中读取数据
- 以读文件的模式打开一个`文件对象`，使用Python内置的`open()`函数，传入文件名和标示符

```python
f = open('/Users/michael/test.txt', 'r')
```
  - 标示符`r`表示读
  - 文件不存在，`open()`函数就会抛出一个`IOError`的错误，并且给出错误码和详细的信息告诉你文件不存在
  - 调用`read()`方法可以一次读取文件的全部内容，Python把内容读到内存，用一个`str`对象表示
  - 调用`close()`方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
  - 于文件读写时都有可能产生`IOError`，一旦出错，后面的`f.close()`就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用`try ... finally`来实现
```python
try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()
```

- Python引入了`with语句`来自动帮我们调用`close()`方法
```python
with open('/path/to/file', 'r') as f:
    print f.read()
```
- `read()`会**一次性读取文件的全部内容**，如果文件有10G，内存就爆了
- 可以反复调用`read(size)`方法，每次最多读取`size`个字节的内容
> 文件很小，`read()`一次性读取最方便；  
>如果不能确定文件大小，反复调用`read(size)`比较保险；  
>如果是配置文件，调用`readlines()`最方便： 

### file-like Object
- 像`open()`函数返回的这种有个`read()`方法的对象,`file-like Object`
- 内存的字节流，网络流，自定义流
- file-like Object不要求从特定类继承，只要写个`read()`方法就行
- `StringIO`就是在内存中创建的file-like Object，常用作临时缓冲

### 二进制文件
- 要读取二进制文件，比如图片、视频等等，用`rb`模式打开文件即可

### 字符编码
- 要读取`非ASCII`编码的文本文件，就必须以二进制模式打开，**再解码**
```python
>>> f = open('/Users/michael/gbk.txt', 'rb')
>>> u = f.read().decode('gbk')
>>> u
u'\u6d4b\u8bd5'
>>> print u
测试
```
- codecs模块

```python
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'
```


### 写文件
- 把数据写入这个文件对象
- 传入标识符`w`或者`wb`表示写文本文件或写二进制文件
- 反复调用`write()`来写入文件，但是务必要调用`f.close()`来关闭文件
- 操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用`close()`方法时，操作系统才保证把没有写入的数据全部写入磁盘
- `with`语句

> 文件读写是通过`open()`函数打开的文件对象完成的。使用`with语句`操作文件IO是个好习惯


## 操作文件和目录
- 我们要**操作文件**、**目录**，可以在命令行下面输入操作系统提供的各种命令来完成。比如`dir`、`cp`等命令
- `os`模块

### 环境变量
- 操作系统中定义的环境变量，全部保存在`os.environ`这个`dict`中
- 要获取某个环境变量的值，可以调用`os.getenv()`函数

### 操作文件和目录
- 操作文件和目录的函数一部分放在`os模块`中，一部分放在`os.path模块`中
```python
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
# 拆分目录
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

```
- **复制文件的函数居然在os模块中不存在**！原因是复制文件并非由操作系统提供的系统调用

- shutil模块
  - 在`shutil模块`中找到很多实用函数，它们可以看做是os模块的补充
- 如何利用Python的特性来过滤文件?
  - 要列出当前目录下的所有目录，只需要一行代码
  ```python
  >>> [x for x in os.listdir('.') if os.path.isdir(x)]
   ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Adlm', 'Applications', 'Desktop', ...]
  ```
  
  - 要列出所有的`.py`文件，也只需一行代码

```python
    >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
   ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
 ```


## 序列化
- 序列化: 把变量从内存中变成可存储或传输的过程称之为序列化
   - 对象： 内存中--->可存储｜可传输
   - Python中叫`pickling`   
   - 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上

- 反序列化
   - 把变量内容从序列化的对象重新读到内存里称之为反序列化
   - 对象：磁盘，网络中--->读取到内存中
   - `unpickling`

- `cPickle`和`pickle`模块
   > 这两个模块功能是一样的，区别在于`cPickle`是`C语言`写的，速度快，`pickle`是纯`Python`写的，速度慢，跟`cStringIO`和`StringIO`一个道理。用的时候，先尝试导入`cPickle`，如果失败，再导入`pickle`
   
   ```python
   try:
     import cPickle as pickle
   except ImportError:
     import pickle
   
   ```

- 尝试把一个对象序列化并写入文件   
  - `pickle.dumps()`方法把任意对象序列化成一个`str`，然后，就可以把这个`str`写入文件。
  - 或者用另一个方法`pickle.dump()`直接把对象序列化后写入一个`file-like Object`：

  ```python
  >>> d = dict(name='Bob', age=20, score=88)
  >>> pickle.dumps(d)
  "(dp0\nS'age'\np1\nI20\nsS'score'\np2\nI88\nsS'name'\np3\nS'Bob'\np4\ns."
  ```
  ```python
  >>> f = open('dump.txt', 'wb')
  >>> pickle.dump(d, f)
  >>> f.close()
  ```

- 反序列化
  - 要把对象从磁盘读到内存时，可以先把内容读到一个`str`，然后用`pickle.loads()`方法反序列化出对象，
  - 也可以直接用`pickle.load()`方法从一个`file-like Object`中直接反序列化出对象

  ```python
  >>> f = open('dump.txt', 'rb')
  >>> d = pickle.load(f)
  >>> f.close()
  >>> d
  {'age': 20, 'score': 88, 'name': 'Bob'}
  ```

  - 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已
  > Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，**只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。**

## JSON
- 不同的编程语言之间传递对象，就必须把对象序列化为标准格式
  - xml
  - JSON
    > 更好的方法是序列化为`JSON`，因为`JSON`表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输  
    > `JSON`不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取 
- JSON类型与Python类型    

| Json类型|Python类型   |
|:---------:|:--------:|
| {} |	dict |
|[]	 |list |
|"string"  |	'str'或u'unicode' |
| 1234.56 |	int或float |
|true/false |	True/False |
| null |	None |

- json模块
  - Python对象到JSON格式的转换
```python
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
```
  - `dumps()`方法返回一个`str`，内容就是标准的`JSON`。
  - `dump()`方法可以直接把`JSON`写入一个`file-like Object`。
- 反序列化
```python
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{u'age': 20, u'score': 88, u'name': u'Bob'}
```   
- 反序列化得到的所有字符串对象默认都是`unicode`而**不是`str`**
- JSON标准规定JSON编码是`UTF-8`，所以我们总是能正确地在Python的`str`或`unicode`与`JSON`的字符串之间转换

### JSON进阶
- [对象序列化](https://docs.python.org/2/library/json.html#json.dumps)
- 把任意`class`的实例变为`dict`
```python
print(json.dumps(s, default=lambda obj: obj.__dict__))
```

- 通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，**用来存储实例变量**
- 如果我们要把JSON反序列化为一个`Student`对象实例，`loads()`方法首先转换出一个`dict对象`，然后，我们传入的`object_hook函数`负责把`dict`转换为`Student`实例

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
```

> json模块的`dumps()`和`loads()`函数是定义得非常好的接口的典范  
> 当默认的序列化或反序列机制不满足我们的要求时，我们又**可以传入更多的参数来定制序列化或反序列化的规则**，既做到了接口简单易用，又做到了充分的扩展性和灵活性