# Web Api指南

## 什么是 Web API
- 可以对接各种`客户端`（**浏览器**，**移动设备**），构建`http服务`的框架

## 为什么要用 Web API
- 可以构建**面向各种客户端的`服务`**
- 与`WCF REST Service`不同在于，`Web API`利用`Http协议`的各个方面来表达服务

## 何时使用Web Api？
1. 需要`Web Service`但是**不需要`SOAP`**
2. 需要在已有的`WCF服务`基础上建立`non-soap-based` `http服务`
3. 只想发布一些**简单的**`Http服务`，不想使用相对复杂的`WCF配置`
4. 发布的服务可能会被带宽受限的设备访问
5. 希望使用`开源框架`，关键时候可以自己调试或者自定义一下框架


## 功能简介
1. 支持基于`Http verb `(`GET`, `POST`, `PUT`, `DELETE`)的`CRUD` (**create, retrieve, update, delete**)操作
    通过不同的`http动作`表达不同的含义，这样就不需要暴露多个`API`来支持这些基本操作。

2. 请求的回复通过`Http Status Code`表达不同含义，并且客户端可以通过`Accept header`来与服务器**协商格式**
   - 例如你希望服务器返回`JSON格式`还是`XML格式`。

3. 请求的回复格式支持 `JSON`，`XML`，并且可以扩展添加其他格式。
4. 原生支持`OData`。

5. 支持`Self-host`或者`IIS host`。

6. 支持大多数`MVC`功能，例如`Routing`/`Controller`/`Action Result`/`Filter`/`Model Builder`/`IOC Container`/`Dependency Injection`

## Web API vs MVC
![WebApi vs MVC](../Images/mvc-vs-webapi.png)

1. `MVC`主要用来**构建网站**，既**关心数据**也**关心页面展示**，而`Web API`**只关注数据**
2. `Web API`支持`格式协商`，客户端可以通过`Accept header`**通知服务器期望的格式**
3. `Web API`支持`Self Host`，`MVC`目前**不支持**
4. `Web API`通过不同的`http verb`表达不同的动作(`CRUD`)，`MVC`则通过`Action`名字表达动作
5. `Web API`内建于`ASP.NET System.Web.Http`命名空间下，`MVC`位于`System.Web.Mvc`命名空间下，因此`model binding`/`filter`/`routing`等功能有所不同
6. `Web API`**非常适合构建移动客户端服务**

## Web API vs WCF
`Web Api`和 `WCF`如何取舍？
- 选择`WCF`
   1. 如果服务需要支持`One Way Messaging`/`Message Queue`/`Duplex Communication`，选择`WCF`
   2. 如果服务需要在`TCP`/`Named Pipes`/`UDP` (`wcf 4.5`)，选择`WCF`
- 选择 `WEB API`
   3. 如果服务需要在`http协议`上，并且希望利用`http协议`的各种功能，选择`Web API`
   4. 如果服务需要**被各种客户端**(特别是移动客户端)调用，选择`Web API`

