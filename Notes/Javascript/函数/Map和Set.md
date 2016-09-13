# Map和Set
- 对象表示方式:`{}`
  - 视为其他语言中的`Map`或`Dictionary`的数据结构，即一组**键值对**
  - `键`必须是字符串
> 但实际上`Number`或者`其他数据类型`作为`键`也是**非常合理**的
- `ES6`规范引入了新的数据类型`Map`

## Map
- `Map`是一组**键值对**的结构，具有极快的查找速度
- 创建一个`Map`
  - 初始化Map需要一个**二维数组**，或者直接初始化一个`空Map`
  ```javascript
    var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
    m.get('Michael'); // 95
  ```
```javascript
    var m = new Map(); // 空Map
    m.set('Adam', 67); // 添加新的key-value
    m.set('Bob', 59);
    m.has('Adam'); // 是否存在key 'Adam': true
    m.get('Adam'); // 67
    m.delete('Adam'); // 删除key 'Adam'
    m.get('Adam'); // undefined
    
  ```


## Set
- 一组`key`的集合，但**不存储`value`**
- 在`Set`中，**没有重复的`key`**
- 重复元素在`Set`中自动被过滤
  - `add(key)`方法可以添加元素到`Set`中，可以重复添加，**但不会有效果**
  - `delete(key)`方法可以删除元素
> `Map`和`Set`是**ES6标准**新增的数据类型，请根据浏览器的支持情况决定是否要使用  