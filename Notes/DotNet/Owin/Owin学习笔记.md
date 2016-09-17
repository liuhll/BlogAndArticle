# OWIN

- [OWIN官网](http://owin.org/)

- [Open Web Interface for .NET (OWIN)](https://docs.asp.net/en/latest/fundamentals/owin.html)

## 什么是owin？
`OWIN`全称`Open Web Interface for .NET`,在 .NET Web 服务器和 .NET Web 应用之间定义了一套标准的接口， 其目的是为了实现`服务器`与`应用`之间的**解耦**， 鼓励为 `.NET Web` 应用开发简单模块
- `OWIN`是一个**开源开放**的标准

### 服务器 (Server)
- **HTTP 服务器**直接与**客户端**交互， 并用 `OWIN`语义处理请求, 服务器需要一个`适配层`将**客户请求**转换成`OWIN`语义
- 支持`OWIN`的服务器有`Katana`和`Nowin`

### Web 框架 (Web Framework)
- 构建在`OWIN`之上的**自包含的独立组件**， 向`Web应用`提供可用的**对象模型**或者**接口**
- `Web框架`可能需要一个`适配层`来转换`OWIN语义`
-  支持`OWIN`的 `Web框架`
   - `Nancy`
   - `SignalR`
   - `WebApi`
   - `FubuMVC`
   - `Simple.Web`
   - `DuoVia.Http`

### Web 应用 (Web Application) 
- 一个特定的`Web应用`， 通常构建在`Web框架`之上， 使用`OWIN`兼容的服务器运行

### 中间件 (Middleware)
- 特定的目的的**服务器和应用之间的`可插拔组件`**， 可以监视、 路由、 修改请求与响应

### 宿主 (Host)
- 应用与服务器所在的`进程`， 主要**负责应用的启动**

## 为什么使用 OWIN?
`OWIN`定义了`.NET Web服务器`与 `.NET Web应用`之间的标准接口， 将应用与服务器**解耦**， 使得便携式 `.NET Web应用`以及跨平台的愿望成为现实， 标准的`OWIN`应用可以在任何`OWIN`兼容的服务器上运行， **不再依赖与 `Windows` 和 `IIS` **

