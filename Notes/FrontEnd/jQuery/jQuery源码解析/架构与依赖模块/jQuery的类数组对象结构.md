# jQuery的类数组对象结构

- `jQuery`为什么能像数组一样操作，通过对象`get方法`或者直接通过`下标0索引`就能转成`DOM对象`?

## 原因分析

1. `jQuery`的入口都是统一的`$`,`9`种方法的重载

```javascript
1. jQuery([selector,[context]])
2. jQuery(element)
3. jQuery(elementArray)
4. jQuery(object)
5. jQuery(jQuery object)
6. jQuery(html,[ownerDocument])
7. jQuery(html,[attributes])
8. jQuery()
9. jQuery(callback)
```

- 9种用法整体来说可以分**三大块**
   - 选择器、
   - `dom`的处理、
   - `dom`加载

   > `jQuery`就是为了获取`DOM`、操作`DOM`而存在的

- `jQuery`内部就采用了一种叫`类数组对象`的方式作为**存储结构**
    - 所以我们即可以像对象一样处理`jQuery`操作，也能像**数组**一样可以使用`push`、`pop`、`shift`、`unshift`、`sort`、`each`、`map`等**类数组**的方法操作`jQuery对象`了   

## jQuery对象可用数组下标索引的原理

- 通过$(".Class")构建的对象结构  
![jquery对象结构](http://img.mukewang.com/53fad4240001c7b805050236.jpg)

> **Notes**  
> - 通过`对象键值对`的**关系**保存着属性，`原型`保存着方法


- 模拟代码段

```javascript
var aQuery = function(selector) {
    //强制为对象
	if (!(this instanceof aQuery)) {
		return new aQuery(selector);
	}
	var elem = document.getElementById(/[^#].*/.exec(selector)[0]);
	this.length = 1;
	this[0] = elem;
	this.context = document;
	this.selector = selector;
	this.get = function(num) {
		return this[num];
	}
	return this;
}
```
