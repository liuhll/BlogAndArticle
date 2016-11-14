# Javascript模块化编程（一）：模块的写法

**模块化编程的理想化状态：**
开发者只需要实现核心的业务逻辑，其他都可以加载别人已经写好的模块

- 模块
   - 实现特定功能的一组方法

## 原始写法

- 只要把不同的函数（以及记录状态的变量）简单地放在一起，就算是一个**模块**
```javascript
　function m1(){
　　　　//...
　　}
　　function m2(){
　　　　//...
　　}
```
> **缺点**
> - "污染"了全局变量，
> - 无法保证不与其他模块发生变量名冲突，
> - 而且模块成员之间看不出直接关系。

- 非常不推荐使用这样的写法

## 对象写法
- 可以把模块写成一个对象，所有的模块成员都放到这个对象里面

```javascript
var module1 = new Object({
　　　　_count : 0,
　　　　m1 : function (){
　　　　　　//...
　　　　},
　　　　m2 : function (){
　　　　　　//...
　　　　}
　　});
```

> **Notes**
> - 函数`m1()`和`m2()`，都封装在`module1`对象里。
> - 使用的时候，就是调用这个对象的属性。

> **例如**
> - `　module1.m1();`

> **缺点**
> - 这样的写法会暴露所有模块成员，
> - 内部状态可以被外部改写
>    - `module1._count = 5;`


## 立即执行函数写法
- `立即执行函数`（Immediately-Invoked Function Expression，IIFE）
  - 可以**达到不暴露私有成员的目的**

```javascript
　　var module1 = (function(){
　　　　var _count = 0;
　　　　var m1 = function(){
　　　　　　//...
　　　　};
　　　　var m2 = function(){
　　　　　　//...
　　　　};
　　　　return {
　　　　　　m1 : m1,
　　　　　　m2 : m2
　　　　};
　　})();
```  

> **Notes**
> - 外部代码无法读取内部的`_count`变量
>    - 　`console.info(module1._count); //undefined`

> - `立即执行函数写法`是 Javascript模块的基本写法
>    - 其他(如下面所述的写法)其实是再对这种写法进行加工

## 放大模式
- `放大模式`（`augmentation`）使用场景
   - 一个模块很大，必须分成几个部分，
   - 或者一个模块需要继承另一个模块

```javascript
　　var module1 = (function (mod){
　　　　mod.m3 = function () {
　　　　　　//...
　　　　};
　　　　return mod;
　　})(module1);
```
> **Notes**
> - 上面的代码为`module1模块`添加了一个`新方法m3()`，然后返回新的`module1`模块
> - 其他：如:给`jquery`扩充插件


## 宽放大模式（Loose augmentation）
- 与`放大模式`相比，`宽放大模式`就是`立即执行函数`的参数可以是`空对象`

- 采用这样写的原因  
  - 模块的各个部分通常都是从网上获取的，有时无法知道哪个部分会先加载

```javascript
　var module1 = ( function (mod){
　　　　//...
　　　　return mod;
　　})(window.module1 || {});
```

## 输入全局变量

- **独立性**是模块的重要特点，`模块内部`最好不与程序的其他部分直接交互

- 为了在模块内部调用全局变量，必须显式地将其他变量输入模块

```javascript
　　var module1 = (function ($, YAHOO) {
　　　　//...
　　})(jQuery, YAHOO);
```
> **Notes**
> - 上面的module1模块需要使用jQuery库和YUI库，就把这两个库（其实是两个模块）当作参数输入module1。
> **好处**
> - 这样做除了保证模块的独立性，
> - 还使得模块之间的依赖关系变得明显