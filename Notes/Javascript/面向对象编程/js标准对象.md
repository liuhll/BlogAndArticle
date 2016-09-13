# 标准对象
在`js`世界中，一切都是`对象`,某些对象还是和其他对象**不太一样**
- 用`typeof`操作符**获取对象的类型**，它总是**返回一个字符串**

```javascript
typeof 123; // 'number'
typeof NaN; // 'number'
typeof 'str'; // 'string'
typeof true; // 'boolean'
typeof undefined; // 'undefined'
typeof Math.abs; // 'function'
typeof null; // 'object'
typeof []; // 'object'
typeof {}; // 'object'
```
- `number`、`string`、`boolean`、`function`和`undefined`**有别于其他类型**
> 特别注意:  
>- `null`的类型是`object`，
>- `Array`的类型也是`object`
>- 用`typeof`将无法区分出`null`、`Array`和通常意义上的`object`——`{}` 

## 包装对象
- `number`、`boolean`和`string`都有**包装对象**
- 包装对象用`new`创建
- 包装对象看上去和原来的值一模一样，显示出来也是一模一样，**但他们的类型已经变为`object`了**
- 包装对象和原始值用`===`比较会返回`false`
   - **不要使用包装对象**,尤其是针对`string`类型



```javascript
var n = new Number(123); // 123,生成了新的包装类型
var b = new Boolean(true); // true,生成了新的包装类型
var s = new String('str'); // 'str',生成了新的包装类型
```
- 在使用`Number`、`Boolean`和`String`时，没有写`new`会发生什么情况？
   - `Number()`、`Boolean()`和`String()`被当做**普通函数**
   - 任何类型的数据转换为`number`、`boolean`和`string`类型
   >  **注意:** 不是其包装类型

## 要遵守的几条规则
- **不要**使用`new Number()`、`new Boolean()`、`new String()`创建包装对象   
- 用`parseInt()`或`parseFloat()`来转换任意类型到`number`
- 用`String()`来转换任意类型到`string`，或者直接调用某个对象的`toString()`方法；
- 通常不必把任意类型转换为`boolean`再判断，因为可以直接写`if (myVar) {...}`；
- `typeof操作符`可以判断出`number`、`boolean`、`string`、`function`和`undefined`；
- 判断`Array`要使用`Array.isArray(arr)`；
- 判断`null`请使用`myVar === null`；
- 判断**某个全局变量是否存在**用`typeof window.myVar === 'undefined'`；
- **函数内部判断某个变量是否存在**用`typeof myVar === 'undefined'`。

> 注意：  
>- `number`对象直接调用`toString()`报`SyntaxError`
>- `null`和`undefined`没有`toString()`

```javascript
123.toString(); // SyntaxError
123..toString(); // '123', 注意是两个点！
(123).toString(); // '123'
```