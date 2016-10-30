# jQuery架构

- 一个优秀的`Javascript`框架
  - 轻量级的`js`库 ，它兼容`CSS3`，还兼容各种浏览器
     - `jQuery2.0`及后续版本将不再支持`IE6/7/8`浏览器
- `jQuery`使用户能更方便地处理`HTML`（标准通用标记语言下的一个应用）、`events`、*实现动画效果*，
并且**方便地为网站提供`AJAX`交互**

- 有许多成熟的插件可供选择


## jQuery设计理念

### 核心理念
- `The Write Less,Do More`（**写更少，做更多**)
  - 简洁的`API`、
  - 优雅的链式、
  - 强大的选择器、
  - 强大的查询与便捷的操作

## jQuery整体架构

- 最新版的`jQuery`的核心模块
	- // 核心方法
	- // 回调系统
	- // 异步队列
	- // 数据缓存
	- // 队列操作
	- // 选择器引
	- // 属性操作
	- // 节点遍历
	- // 文档处理
	- // 样式操作
	- // 属性操作
	- // 事件体系
	- // AJAX交互
	- // 动画引擎

```javascript
(function(global, factory) {
    factory(global);
}(typeof window !== "undefined" ? window : this, function(window, noGlobal) {
    var jQuery = function( selector, context ) {
		return new jQuery.fn.init( selector, context );
	};
	jQuery.fn = jQuery.prototype = {};
	// 核心方法
	// 回调系统
	// 异步队列
	// 数据缓存
	// 队列操作
	// 选择器引
	// 属性操作
	// 节点遍历
	// 文档处理
	// 样式操作
	// 属性操作
	// 事件体系
	// AJAX交互
	// 动画引擎
	return jQuery;
}));
```

### jQuery的模块依赖网

![jquery的模块依赖网](http://img.mukewang.com/53fa8fec0001754806930473.jpg)

- `jQuery`一共`13`个模块，从2.1版开始jQuery支持通过`AMD`模块划分
   - **1.0版本**只有`CSS选择符`、`事件处理`和`AJAX交互`3大块

- `jQuery`抽出了所有可复用的特性，分离出单一模块，通过组合的用法，
不管在设计思路与实现手法上`jQuery`都是非常高明的。


### 五大块

- 选择器、
- DOM操作、
- 事件、
- AJAX
- 动画

> **Notes**
> - 为什么`jQuery`需要有13个模块呢？
>    - jQuery的设计中最喜欢的做的一件事，就是抽出共同的特性使之“模块化”，当然也是更贴近`S.O.L.I.D`五大原则的`单一职责SRP`了，
>        - 遵守单一职责的好处是可以让我们很容易地来维护这个对象
>    - 通过`解耦`可以让每个职责更加有弹性地变化

## jQuery接口的设计原理

- 业务逻辑是复杂多变的
- `jQuery`的高层`API`数量**非常多**，而且也**非常的细致**，
   - 这样做可以更友好的便于开发者的操作，不需要必须在一个接口上重载太多的动作。

### 针对业务层的Ajax的处理【例子】

- **门面接口**

```javascript
.ajaxComplete()
.ajaxError()
.ajaxSend()
.ajaxStart()
.ajaxStop()
.ajaxSuccess()
```

- 底层接口
```
jQuery.ajax()
jQuery.ajaxSetup()
```

- 快捷方法：

```javascript
jQuery.get()
jQuery.getJSON()
jQuery.getScript()
jQuery.post()
```