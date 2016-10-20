# Shell字符串

- `字符串`是`shell`编程中**最常用** **最有用的** `数据类型`
   - 除了`数字`和`字符串`，也没啥其它类型好用了

- `字符串`可以**用单引号**，也可以**用双引号**，也可以**不用引号**

## 单引号

```bash
str='this is a string'
```

>`单引号字符串`的限制 
> - **单引号**里的任何字符都**会原样输出**，`单引号字符串`中的变量**是无效的**；
> - **单引号字串**中**不能**出现`单引号`（**对单引号使用转义符后也不行**）。

## 双引号

```bash
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
echo ${str}
echo -e ${str}

#输出
#Hello, I know your are "qinjx"! \n #没有换行
#Hello, I know your are "qinjx"! #换行了


```

> **优点**  
> - `双引号`里可以*有变量*
> - `双引号`里可以出现*转义字符*

## 拼接字符串

```bash
your_name="qinjx"
greeting="hello, "$your_name""
greeting_1="hello, ${your_name}"
echo $greeting $greeting_1
```

## 获取字符串长度
- 语法
```bash
${#var_name} #输出该变量的字符串长度
```

```bash
string="abcd"
echo ${#string} #输出 4
```

## 提取子字符串

- 语法

```bash
${var_name:start_index:end_index} #得到子串
```
> **Notes**  
> - 可以将得到子串赋值给另一个变量，或是直接输出
> - `start_index`和`end_index`指的是字符串的索引，索引从`0`开始

```bash
string="alibaba is a great company"
echo ${string:1:4} #输出liba
```

## 查找子字符串
-----------

## 参考资料
- [linux shell 字符串操作详解](http://justcoding.iteye.com/blog/1963463)
- [Bash Shell字符串操作小结](https://www.centos.bz/2013/08/bash-shell-string-operate-summary/)

