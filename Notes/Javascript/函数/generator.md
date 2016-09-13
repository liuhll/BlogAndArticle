# 生成器----genrator
- `generator`（生成器）是**ES6标准**引入的新的数据类型
- 一个`generator`看上去像一个**函数**，但可以返回多次

> 函数在执行过程中，如果没有遇到`return语句`（*函数末尾如果没有`return`，就是隐含的`return undefined;`*），控制权无法交回被调用的代码。

- `generator`和`函数`不同的是:
   - `generator`由`function*`定义（注意多出的`*`号），并且，除了`return`语句，还可以用`yield`**返回多次**
   
- 返回多次有啥用？

```javascript
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 1;
    while (n < max) {
        yield a;
        t = a + b;
        a = b;
        b = t;
        n ++;
    }
    return a;
}
```   

- 直接调用一个`generator`和调用函数不一样，`fib(5)`仅仅是创建了一个`generator对象`，还没有去执行它
```javascript
var f = fib(5);
```

## 调用generator对象有两个方法
1. 不断地调用`generator`对象的`next()`方法
```javascript
var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: true}
```
- 每次遇到`yield x`;就返回一个对象`{value: x, done: true/false}`，然后**暂停**
- `done`表示这个`generator`是否已经执行结束了
   - 如果`done`为`true`，则`value`就是`return`的返回值

2. 直接用`for ... of`循环迭代`generator`对象
   - 这种方式不需要我们自己判断`done`
```javascript
for (var x of fib(5)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3
}
```      

## 有什么用？
1. `generator`可以在执行过程中多次返回，所以它看上去就**像一个可以记住执行状态的函数**，利用这一点，写一个`generator`就可以实现需要用面向对象才能实现的功能

2. generator还有另一个巨大的好处，就是把`异步回调代码`变成**“同步”代码**

```javascript
//暗黑时代
ajax('http://url-1', data1, function (err, result) {
    if (err) {
        return handle(err);
    }
    ajax('http://url-2', data2, function (err, result) {
        if (err) {
            return handle(err);
        }
        ajax('http://url-3', data3, function (err, result) {
            if (err) {
                return handle(err);
            }
            return success(result);
        });
    });
});


// generator
try {
    r1 = yield ajax('http://url-1', data1);
    r2 = yield ajax('http://url-2', data2);
    r3 = yield ajax('http://url-3', data3);
    success(r3);
}
catch (err) {
    handle(err);
}
```