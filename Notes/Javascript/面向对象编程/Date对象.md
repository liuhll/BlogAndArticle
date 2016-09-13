# Date
`Js`中，使用`Date`对象用来表示日期和时间
- 获取系统当前时间
- **当前时间**是**浏览器**从**本机操作系统获取的**时间
- `JavaScript`的月份范围用整数表示是`0~11`
  - 非常坑爹

```javascript
var now = new Date();
now; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
now.getFullYear(); // 2015, 年份
now.getMonth(); // 5, 月份，注意月份范围是0~11，5表示六月
now.getDate(); // 24, 表示24号
now.getDay(); // 3, 表示星期三
now.getHours(); // 19, 24小时制
now.getMinutes(); // 49, 分钟
now.getSeconds(); // 22, 秒
now.getMilliseconds(); // 875, 毫秒数
now.getTime(); // 1435146562875, 以number形式表示的时间戳
```


## 创建一个指定的日期时间对象
1. 通过构造函数
```javascript
var d = new Date(2015, 5, 19, 20, 15, 30, 123);
d; // Fri Jun 19 2015 20:15:30 GMT+0800 (CST)
```
2. 创建一个指定日期和时间的方法是解析一个符合`ISO 8601格式`的**字符串**
```javascript
var d = Date.parse('2015-06-24T19:49:22.875+08:00');
d; // 1435146562875
```
- 返回的不是`Date`对象，而是一个时间戳

3. 时间戳转`Date`对象

```javascript
var d = new Date(1435146562875);
d; // Wed Jun 24 2015 19:49:22 GMT+0800 (CST)
```

## 时区
- `Date对象`表示的时间**总是按浏览器所在时区显示的**
- `JavaScript`中如何进行时区转换呢？

- 时间戳?
  - `时间戳`是一个自增的整数，它表示从1970年1月1日零时整的GMT时区开始的那一刻，到现在的毫秒数
  - `时间戳`可以精确地表示一个时刻，并且**与时区无关**