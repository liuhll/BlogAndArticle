# Http报头Accept与Content-Type的区别

- [参考](http://blog.csdn.net/muzizongheng/article/details/46795243)

## `Accept`属于**请求头**， `Content-Type`属于**实体头**。 
- `Http`报头分为通用报头，请求报头，响应报头和实体报头。 

- 请求方的`http`报头结构：
```
通用报头|请求报头|实体报头 
```
- 响应方的`http`报头结构：

```
通用报头|响应报头|实体报头
```

## `Accept`代表发送端（客户端）希望接受的数据类型。 
- 比如：`Accept：text/xml;` 
- 代表客户端希望接受的数据类型是`xml`类型

## `Content-Type`代表发送端（客户端|服务器）发送的实体数据的数据类型。 
- `Content-Type`，内容类型，一般是指网页中存在的Content-Type，用于定义网络文件的类型和网页的编码，决定浏览器将以什么形式、什么编码读取这个文件，这就是经常看到一些Asp网页点击的结果却是下载到的一个文件或一张图片的原因
- 比如：`Content-Type：text/html;` 
- 代表发送端发送的数据格式是`html`。

## Demo
- 二者合起来， 
```
Accept:text/xml； 
Content-Type:text/html 
```
>  **Notes**
> - 即代表希望接受的数据类型是`xml`格式，本次请求发送的数据的数据格式是`html`。