# 一种SPA（单页面应用）架构

## 概述
![spa前后端以及各自的主要组成](https://sfault-image.b0.upaiyun.com/313/912/31391284-56fe284a42a58_articlex)

## 前端架构
![前端架构图](https://segmentfault.com/image?src=https://cloud.githubusercontent.com/assets/6436132/3597146/1cdbb8c0-0cce-11e4-84fb-af528f3e3226.jpg&objectId=1190000000607661&token=d7fb0e7fd0cc2fe71fef0fb719083afd)

- 前端中大致分为**四种类型**的模块
1. `components`：前端UI组件
2. `services`：前端数据缓存和操作层
3. `databus`：封装一系列`Ajax操作`，和后端进行数据交互的**部件**
4. `common/utils`：以上组件的共用部件，可复用的函数、数据等

### components
指的是页面上的一个**可复用UI交互单元**
- 组件有自己的结构（`html`），外观（`css`），交互逻辑（`js`）
- **demo**
![博客评论功能](https://segmentfault.com/image?src=https://cloud.githubusercontent.com/assets/6436132/3597177/75747f1c-0cce-11e4-91be-1d329f4cb77a.jpg&objectId=1190000000607661&token=bd2fb5c0efd09fe010c3a9a6fa795d8b)

> **Notes**
> - 每个`component`可以想象成一个工程，甚至可以有自己的README、测试等

### components tree
-  类似`DOM tree`,`component`可以组成`components tree`
   1. 一个`component`可以依赖另外一个`component`，这时候它们是**父子关系**；
   2. component之间也可以互相组合，它们就是**兄弟关系**

### components之间的通信
- 最佳的方式就是使用**事件机制**
- 所有组件之间可以通过一个叫`eventbus`通用组件进行信息的交互

- **案例**： 怎么可以做到鼠标放到评论和回复的用户头像上显示名片呢？
1. `user-info-card`可以在`eventbus`监听一个`user-info-card:show`的事件。

```javascript
// user-info-card:

var eventbus = require("eventbus")
eventbus.on("user-info-card:show", function(user) {
    // 显示用户名片
})

```

2. 而当鼠标放到comment和reply组件的头像上的时候，组件可以使用`eventbus`触发`user-info-card:show`事件

```javascript
//comment or reply:

var eventbus = require("eventbus")
$avatar.on("mouseover", function(event) {
    eventbus.emit("user-info-card:show", userData)
})
```

- `components`之间用事件进行通信的**优势**
  1. 组件之间没有强的依赖，组件之间**被解耦**。
  2. 组件之间可以**单独开发**、**单独测试**。数据和事件都可以简单的进行伪造进行测试（`mocking`）

### services
- `component`的渲染和显示依赖于数据（`model`）,`services`是对前端数据（也就是`model`）的缓存和操作
- `services`除了用于缓存数据以外，还提供一系列对数据的一些操作接口。可以提供给`components`进行操作。这样的好处在于保持了数据的一直性

### databus
- `services`中缓存的数据是从哪里来的呢?
   - 是把各种和后端的API进行交互的接口封装到一个叫`databus`的模块当中，这里的`databus`相当于是“对后端数据进行原子操作的集合”

- **Demo**： `comment service`需要从后端进行拉取数据，它会这样做
```javascript
var databus = require("databus")
var comments = null
databus.getAllComments(function(cmts) { // 调用databus方法进行数据拉取
    comments = cmts
})
```
   - `databus`中则封装了一层`Ajax`

```javascript
databus.getAllCommetns = function(callback) {
    utils.ajax({
        url: "/comments",
        method: "GET",
        success: callback
    })
}
```
- 不同的`services`之间可能会用到同样的接口对后端进行操作，把操作封装起来可以提高接口的复用

> **总结**
> - `databus`封装了提供给`services`和`component`和后端`API`进行交互的接口

### common/utils
这两个模块都可以被其他组件所依赖

- `common`
   - 组件之间的共用数据和一些程序参数可以缓存在这里。

- `utils`
   - 封装了一些可复用的函数，例如`ajax`等。

### eventbus
所有组件（特别是`components`之间）的通过事件机制进行数据、消息通信的接口。
- 可以简单地使用[EventEmitter](https://github.com/asyncly/EventEmitter2)这个库来实现。

## 后端架构
- 传统的**网页页面**一般都是由后端进行页面的渲染
- **SPA**架构中，**后端只渲染一个页面**
   - 后端只是相当于一个`Web Service`，前端使用`Ajax`调用其接口进行数据的调取和操作，使用数据进行页面的渲染
- 后端大概分为三层
  1. `CGI`
     - 设置不同的路由规则，接受前端来的请求，处理数据，返回结果。
  2. `business`
      - 这一层封装了对数据库的一些操作，`business`可以被`CGI`所调用。
  3. `database`
       - 数据库，进行数据的持久化。

**好处**
> - 后端不仅仅能处理Web端的页面的请求，而且处理提供移动端、桌面端的请求或者作为第三方开放接口来使用。大大提高后端处理请求的灵活性

![后端架构图](https://segmentfault.com/image?src=https://cloud.githubusercontent.com/assets/6436132/3597195/9be8b2f8-0cce-11e4-83f5-5a7baf960de5.jpg&objectId=1190000000607661&token=777e4977834daad885c553bbc92eb15c)

- `CGI`可以接收到前端发送的请求
```javascript
var commentsBusiness = require("./businesses/comments")
app.get("/comments", function(req, res) {
    // 此处调用comments的business数据库操作
    commentsBusiness.getAllComments(function(comments) {
        // 返回数据结果
        res.json(comments)
    })
})
```

> **Notes**
> -  **好处**
> - 后端不仅仅能处理`Web端`的页面的请求，而且处理提供移动端、桌面端的请求或者作为第三方开放接口来使用。大大提高后端处理请求的灵活性


## 总结一下整个前后端的交互流程
1. 前端向服务端请求**第一个**页面，后端渲染返回。
2. 前端加载各个`component`，`components`从`services`拿数据，`services`通过`databus`发送**`Ajax`请求**向后端取数据。
3. 后端的`CGI`接收到前端`databus`发送过来的请求，处理数据，调用`business`操作数据库，返回结果。
4. 前端接收到后端返回的结果，把数据缓存到`service`，`component`拿到数据进行前端组件的渲染、显示。


## 工作流
- 工作流的**优势**： 一个好的工作流可以让开发事半功倍

1. 进行产品功能、原型设计。
2. 后端数据库设计。
3. 根据产品确定前后端的`API`（or `RESTful API`），以文档方式纪录。
4. 前后端就可以针对`API`文档同时进行开发。
5. 前后端最后进行连接测试。

> **前后端分离开发**
> - 建议都可以采用TDD（测试驱动开发）的方式来单独测试、**单独开发**
> 提高产品的可靠性、稳定性

## 参考
- [spa单页面设计架构](https://segmentfault.com/a/1190000000607661#articleHeader0)