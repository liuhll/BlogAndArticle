# 理解Python WSGI

> 参考资料
> - [理解Python WSGI](http://www.letiantian.me/2015-09-10-understand-python-wsgi/)
> - [官网](http://wsgi.tutorial.codepoint.net/)

## 什么是`WSGI`
- 全称：`Web Server Gateway Interface`
- 这是一个规范，描述了`web server`如何与`web application`交互、`web application`如何处理请求

> **Notes**
> - WSGI既要实现`web server`，也要实现`web application`

- 实现了`WSGI`的模块/库
  - `wsgiref`(python内置)
  - `werkzeug.serving`
  - `twisted.web`

- 运行在`WSGI`之上的`web`框架
   1. `Bottle`
   2. `Flask`
   3. `Django`

   > 参考
   > - [Frameworks that run on WSGI¶](http://wsgi.readthedocs.io/en/latest/frameworks.html) 


- `WSGI server`  
所做的工作仅仅是将从客户端收到的请求传递给`WSGI application`，然后将`WSGI application`的返回值作为响应传给客户端。
- `WSGI applications`  
可以是栈式的，这个栈的中间部分叫做`中间件`，两端是必须要实现的`application`和`server`   

## WSGI教程

### WSGI application接口

- `WSGI application`接口应该实现为一个**可调用对象**
   - 例如`函数`、`方法`、`类`、含`__call__方法`的实例。
- 这个**可调用对象**可以接收`2`个参数
  1. 一个字典，该字典可以包含了客户端请求的信息以及其他信息，可以认为是**请求上下文**，一般叫做`environment`（编码中多简写为`environ`、`env`）；
  2. 一个用于发送`HTTP`响应状态（`HTTP status` ）、响应头（`HTTP headers`）的**回调函数**

- **可调用对象**的返回值是`响应正文`（`response body`），`响应正文`是可迭代的、并包含了多个字符串  

> WSGI Application的结构
```python
def application (environ, start_response):

    response_body = 'Request method: %s' % environ['REQUEST_METHOD']

    # HTTP响应状态
    status = '200 OK'

    # HTTP响应头，注意格式
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    # 将响应状态和响应头交给WSGI server
    start_response(status, response_headers)

    # 返回响应正文
    return [response_body]
```

### Environment
- 

### 可迭代的响应

- 如果把上面的可调用对象`application`的返回值：
```python
return [response_body]
```
改成：

```python
return response_body
```
> **Notes** 
> - 导致`WSGI`程序的响应变慢
> - 原因
>    - 是字符串`response_body`也是可迭代的，它的每一次迭代只能得到1 byte的数据量，这也意味着每一次只向客户端发送1 byte的数据，直到发送完毕为止。
> - 推荐使用`return [response_body]`

## 解析GET请求

## 解析POST请求

## Python WSGI入门

### Web server
`WSGI server`就是一个`web server`
- 处理请求逻辑如下：
```python
iterable = app(environ, start_response)
for data in iterable:
   # send data to client
```
- `app`即`WSGI application`，`environ`即上文中的`environment`
- 可调用对象`app`返回一个可迭代的值，`WSGI server`获得这个值后将数据发送给客户端

### Web framework/app
- `WSGI application`

### 中间件（`Middleware`）
- 中间件位于`WSGI server`和`WSGI application`之间

> 一个示例

```python
# ! /usr/bin/env python
# -*- coding: utf-8 -*- 

from wsgiref.simple_server import make_server

def application(environ, start_response):

    response_body = 'hello world!'

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

# 中间件
class Upperware:
   def __init__(self, app):
      self.wrapped_app = app

   # 实现专有函数__call__(),进行回调   
   def __call__(self, environ, start_response):
      for data in self.wrapped_app(environ, start_response):
        yield data.upper()

wrapped_app = Upperware(application)

httpd = make_server('localhost', 8051, wrapped_app)

httpd.serve_forever()

print 'end'
```
