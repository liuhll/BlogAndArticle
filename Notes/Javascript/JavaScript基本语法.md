# Javascript 基本语法
## 基本语法
- `JavaScript`的语法和`Java`语言类似，每个语句以;结束，**语句块**用`{...}`。
- JavaScript并不强制要求在每个语句的结尾加`;`，
浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上`;`。


## 数据类型
### Number

```javascript
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
```
- `NaN`这个特殊的`Number`与所有其他值都不相等，包括它自己
   - 唯一能判断NaN的方法是通过`isNaN()`函数
### 字符串
- 字符串是以单引号`'`或双引号`"`括起来的任意文本
- 字符串内部既包含'又包含"怎么办？
   - 可以用转义字符`\`来标识
   ```javascript
   'I\'m \"OK\"!';
   ```
   > 转义字符`\`可以转义很多字符，比如`\n`表示`换行`，`\t`表示`制表符`，字符`\`本身也要转义，所以`\\`表示的字符就是`\`
- `ASCII字符`可以以`\x##`形式的`十六进制`表示
- 用`\u####`表示一个`Unicode字符`
- 多行字符串
  - S6标准新增了一种多行字符串的表示方法，用｀... ｀表示

####  模板字符串
- 把多个字符串连接起来，可以用`+`号连接
- ES6新增了一种模板字符串，表示方法和上面的多行字符串一样，但是它会自动替换字符串中的变量
```javascript
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```
#### 操作字符串
- s.length
- 获取字符串某个指定位置的字符
   - `s[i];` #索引号从0开始
   > 字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果
- toUpperCase
- toLowerCase
- indexOf
- substring
    ```javascript
    var s = 'hello, world'
    s.substring(0, 5); // 从索引0开始到5（不包括5），返回'hello'
    s.substring(7); // 从索引7开始到结束，返回'world'
    ```
### 布尔值
- 一个布尔值只有`true`、`false`两种值
- `&&`  、  `||`  、 `!`

### null和undefined
- `null`表示“空”
- `undefined`表示值未定义
- 大多数情况下，我们都应该用`null`。`undefined`仅仅在判断函数参数是否传递的情况下有用

### 数组
```Javascript
[1, 2, 3.14, 'Hello', null, true];
```
- `数组`是一组按顺序排列的`集合`，
- `集合`的每个值称为`元素`
- `JavaScript`的数组可以**包括任意数据类型**
   - `Array`可以包含任意数据类型，并通过索引来访问每个元素
- 数组用`[]`表示，元素之间用`,`分隔
- 直接给`Array`的`length`赋一个新的值会导致`Array大小`的变化
    ```javascript
    var arr = [1, 2, 3];
    arr.length; // 3
    arr.length = 6;
    arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
    arr.length = 2;
    arr; // arr变为[1, 2]
    ```
- `Array`可以通过索引把对应的元素修改为新的值，因此，
   - 对`Array`的索引进行赋值会直接修改这个`Array`
   - 如果通过索引赋值时，索引超过了范围，同样会引起`Array`大小的变化
> 大多数其他编程语言不允许直接改变数组的大小，越界访问索引会报错。  
> 然而，JavaScript的`Array`却不会有任何错误
> **不建议**直接修改Array的大小，访问索引时要确保索引不会越界

#### 操作数组
- indexOf
  - Array也可以通过`indexOf()`来搜索一个指定的元素的位置
- slice
  - **截取`Array`的部分元素**，然后返回一个新的Array

- `push`和`pop`
   - `push()`向`Array`的末尾添加若干元素
   - `pop()`则把`Array`的最后一个元素删除掉
- `unshift`和`shift`
   - `Array`的头部添加若干元素，使用`unshift()`方法，
   - `shift()`方法则把`Array`的第一个元素删掉
- sort
- reverse
  - 反转
- splice
  - 可以从指定的索引开始**删除若干元素**，然后**再从该位置添加若干元素**
  ```javascript
    var arr = ['Microsoft', 'Apple', 'Yahoo', 'AOL', 'Excite', 'Oracle'];
    // 从索引2开始删除3个元素,然后再添加两个元素:
    arr.splice(2, 3, 'Google', 'Facebook'); // 返回删除的元素 ['Yahoo', 'AOL', 'Excite']
    arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
    // 只删除,不添加:
    arr.splice(2, 2); // ['Google', 'Facebook']
    arr; // ['Microsoft', 'Apple', 'Oracle']
    // 只添加,不删除:
    arr.splice(2, 0, 'Google', 'Facebook'); // 返回[],因为没有删除任何元素
    arr; // ['Microsoft', 'Apple', 'Google', 'Facebook', 'Oracle']
  ```   
- concat
  - `concat()`方法把当前的`Array`和另一个`Array`连接起来，并返回一个`新的Array`
  - `concat()`方法可以接收任意个元素和`Array`，并且自动把`Array`拆开，然后全部添加到新的`Array`里
- join
  - 把当前`Array`的每个元素都**用指定的字符串连接起来**，然后返回连接后的`字符串`

#### 创建数组
  - 1. `Array()`
  - 2. `[]`
  > 出于代码的可读性考虑，强烈建议直接使用`[]`
- 数组的元素可以通过`索引`来访问
  - 索引的起始值为`0`

#### 多维数组


### 对象
- `对象`是一组由`键-值`组成的**无序**`集合`
```javascript
var person = {
    name: 'Bob',
    age: 20,
    tags: ['js', 'web', 'mobile'],
    city: 'Beijing',
    hasCar: true,
    zipcode: null
};
```
- JavaScript用一个`{...}`表示一个对象，键值对以`xxx: xxx`形式申明，用`,`隔开
  - 最后一个键值对不需要在末尾加`,`，如果加了`，`有的浏览器（如低版本的IE）将报错

- `键`都是**字符串类型**，`值`可以是**任意数据类型**
  - `键`又称为`对象的属性`
- 获取一个`对象的属性`
  - `对象变量.属性名`
  - `对象变量['属性名']`
- JavaScript的对象是`动态类型`，你可以自由地给一个对象添加或删除属性
```javascript
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错
```
- 我们要检测xiaoming是否拥有某一属性，可以用`in操作符`
```javascript
'name' in xiaoming; // true
'grade' in xiaoming; // false
```
- 如果`in`判断一个属性存在，这个属性不一定是`obj`的，它可能是`obj`继承得到
- 要判断一个属性是否是`obj`自身拥有的，**而不是继承得到的**，可以用`hasOwnProperty()`方法
```javascript
var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
```
## 变量
- 变量在JavaScript中就是用一个`变量名`表示
- 变量名是`大小写英文`、`数字`、`$`和`_`的组合，**且不能用数字开头**。
- 变量名也**不能是`JavaScript`的关键字**
- 申明一个变量用`var语句`
   - 只能用`var`**申明一次**
- 使用等号`=`对变量进行赋值
   - **把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量**
   - 动态语言

## strict模式
- 设计之初，不强制要求用`var`申明变量
- 如果一个变量没有通过var申明就被使用，那么该变量就自动被申明为**全局变量**
－**同一个页面**的不同的JavaScript文件中，如果都不用`var`申明，恰好都使用了变量`i`，将造成变量`i`互相影响，产生难以调试的错误结果
```javascript
i = 10; // i现在是全局变量
```
- `strict`模式
  - 在`strict模式`下运行的JavaScript代码，强制通过`var`申明变量，未使用`var`申明变量就使用的，将导致运行错误
```javascript
'use strict';
```

## 比较运算符
### 相等运算符
- `JavaScript`在设计时，有两种比较运算符
  1. `==`
  > **会自动转换数据类型再比较**，很多时候，会得到非常诡异的结果
  2. `===`
  > **不会自动转换数据类型**，如果数据类型不一致，返回`false`，如果一致，再比较


## 条件判断

- `if () { ... } else { ... }`来进行条件判断
- 多行条件判断
  - 通常把`else if`连写在一起，来增加可读性
  > 请注意，`if...else...`语句的执行特点是二选一，在多个`if...else...`语句中，如果某个条件成立，则后续就不再继续判断了

## 循环
- 循环有两种
1. `for循环`，通过`初始条件`、`结束条件`和`递增条件`来循环执行语句块
  - `for循环`最常用的地方是利用索引来遍历数组
  - `for循环`的3个条件都是可以省略的，如果没有退出循环的判断条件，就必须使用break语句退出循环，否则就是`死循环`
  - `for ... in`
2. while
   - `while`循环只有一个判断条件，条件满足，就不断循环，条件不满足时则退出循环
   - `do ... while`
   - 循环体**会至少执行1次**，而`for`和`while`循环则可能一次都不执行
  > 务必小心编写初始条件和判断条件，尤其是**边界值**。特别注意i < 100和i <= 100是不同的判断逻辑 
