# base64
- `Base64`是一种用**64个字符**来表示**任意二进制数据**的方法
- Python内置的`base64`可以直接进行base64的编解码

```python
>>> import base64
>>> base64.b64encode('binary\x00string')
'YmluYXJ5AHN0cmluZw=='
>>> base64.b64decode('YmluYXJ5AHN0cmluZw==')
'binary\x00string'
```


## url safe的base64编码
- 标准的`Base64`编码后可能出现字符`+`和`/`，在URL中就不能直接作为参数
   - 把字符`+`和`/`分别变成`-`和`_`


```python
>>> base64.b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd++//'
>>> base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
'i\xb7\x1d\xfb\xef\xff'
```   
- `=`在`url`中有歧义
```python
>>> base64.b64decode('YWJjZA==')
'abcd'
>>> base64.b64decode('YWJjZA')
Traceback (most recent call last):
  ...
TypeError: Incorrect padding
>>> safe_b64decode('YWJjZA')
'abcd'
```

## base64编码的用途
- Base64是一种通过查表的编码方法，**不能用于加密**，即使使用自定义的编码表也不行。
- Base64适用于**小段内容的编码**，
   - 比如`数字证书签名`、`Cookie`的内容等。
   - 常用于在`URL`、`Cookie`、网页中`传输少量二进制数据`