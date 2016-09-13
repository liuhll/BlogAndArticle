# Json
- `JSON`是`JavaScript Object Notation`的缩写,它是一种**数据交换格式**

- `Json`是一种**超轻量级**的数据交换格式

## Json数据类型
- `number`：和JavaScript的`number`完全一致；
- `boolean`：就是JavaScript的`true`或`false`；
- `string`：就是JavaScript的`string`；
- `null`：就是JavaScript的`null`；
- `array`：就是JavaScript的`Array`表示方式——`[]`；
- `object`：就是JavaScript的`{ ... }`表示方式。

> `JSON`还定死了字符集必须是`UTF-8`，**表示多语言就没有问题了**

## Json格式
- JSON的字符串规定必须用双引号`""`，`Object`的`键`也必须用双引号`""`
- 几乎所有编程语言**都有解析JSON的库**

## 序列化
- JavaScript对象变成`JSON`
- 把这个**对象序列化**成一个`JSON`格式的**字符串**
- 能够通过网络传递给其他计算机
```javascript

JSON.stringify(obj);

//要输出得好看一些，可以加上参数，按缩进输出
JSON.stringify(xiaoming, null, '  ');
```
> **第二个参数**
> - 用于控制如何筛选对象的键值，如果我们只想输出指定的属性，可以传入`Array`
> - 还可以传入一个函数，这样**对象的每个键值对都会被函数先处理**

```javascript
function convert(key, value) {
    if (typeof value === 'string') {
        return value.toUpperCase();
    }
    return value;
}

JSON.stringify(xiaoming, convert, '  ');

{
  "name": "小明",
  "age": 14,
  "gender": true,
  "height": 1.65,
  "grade": null,
  "middle-school": "\"W3C\" MIDDLE SCHOOL",
  "skills": [
    "JAVASCRIPT",
    "JAVA",
    "PYTHON",
    "LISP"
  ]
}
```

## 反序列化
- `Json`格式的**字符串**`反序列化`为一个`对象`
- 到一个`JSON`格式的**字符串**，我们直接用`JSON.parse()`把它变成一个`JavaScript对象`
- `JSON.parse()`还可以接收一个函数，用来转换解析出的属性

```javascript
JSON.parse('{"name":"小明","age":14}', function (key, value) {
    // 把number * 2:
    if (key === 'name') {
        return value + '同学';
    }
    return value;
}); // Object {name: '小明同学', age: 14}
```
