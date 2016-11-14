# Javascript模块化编程（二）：AMD规范

- 本文描述如何规范地使用模块

## 模块的规范

- 目前通行的Javascript模块规范共有两种：
  1. `CommonJS`
  2. [`AMD`](https://github.com/amdjs/amdjs-api/wiki/AMD-(%E4%B8%AD%E6%96%87%E7%89%88))

### CommonJS
- 模块化编程的重要性
   - **在服务器端**，一定要有模块，与操作系统和其他应用程序互动，否则根本没法编程
- `node.js`的模块系统，就是参照`CommonJS`规范实现的

- `require()`方法
   - 这是一种同步的加载模块的方式，不适用客户端模块的加载
   - 在CommonJS中，有一个全局性方法`require()`，用于加载模块

   ```javascript
   　var math = require('math');
   ```
   - 加载模块后，就可以调用模块提供的方法

   ```javascript
   var math = require('math');
　 math.add(2,3); // 5 
   ```

   
### 浏览器环境
- 浏览器模块与客户端模块的兼容
  - 一个模块不用修改，在服务器和浏览器都可以运行。
  - 由于一个重大的局限，使得`CommonJS`规范**不适用**于浏览器环境。


```javascript
　var math = require('math');
　math.add(2, 3);
```
> **说明**
> - 第二行math.add(2, 3)，在第一行require('math')之后运行，因此必须等math.js加载完成。
>   - 也就是说，如果加载时间很长，整个应用就会停在那里等。
> - 对于服务端
>    - 服务器端不是一个问题，因为所有的模块都存放在本地硬盘，可以同步加载完成，等待时间就是硬盘的读取时间
> - 对于浏览器
>    - ，因为模块都放在服务器端，等待时间取决于网速的快慢，可能要等很长时间，浏览器处于**假死**状态

> - 浏览器端的模块，不能采用`同步加载`（`synchronous`），只能采用`异步加载`（`asynchronous`）

## AMD
- `AMD`是`Asynchronous Module Definition`的缩写，意思就是`异步模块定义`

- 采用异步模块定义的好处
  - 模块的加载**不影响**它后面语句的运行
  - 所有依赖这个模块的语句，都定义在一个回调函数中，等到加载完成之后，这个`回调函数`才会运行
  - 浏览器**不会**发生假死 
      - `AMD`比较适合**浏览器环境**

- AMD也采用`require()`语句加载模块
   - 但是不同于CommonJS，它要求两个参数

```javascript
require([module], callback);
```

> **Notes**
> - 第一个参数`[module]`，是一个数组，里面的成员就是要加载的模块；
> - 第二个参数`callback`，则是加载成功之后的回调函数

```javascript
　　require(['math'], function (math) {
　　　　math.add(2, 3);
　　});
```

> 实现AMD规范的js库
> - 主要有两个Javascript库实现了AMD规范：`require.js`和`curl.js`



