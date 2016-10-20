# Shell变量：Shell变量的定义、删除变量、只读变量、变量类型

## 定义变量
- `Shell`支持`自定义变量`

- 定义变量时，变量名不加美元符号（`$`)

```sh
variableName="value"
```
> **Notes**  
> `变量名`和`等号`之间**不能**有空格

- 变量名的命名
  - 首个字符必须为字母（`a-z`，`A-Z`）。
  - **中间不能有空格**，可以使用下划线（`_`）。
  - 不能使用标点符号。
  - 不能使用`bash`里的关键字（可用`help命令`查看保留关键字）。


## 使用变量
- 使用一个定义过的变量，只要在变量名前面加美元符号（`$`）即可

```bash
your_name="mozhiyan"
echo $your_name
echo ${your_name}
```  

- `变量名`外面的花括号是可选的，**加不加都行**，**加花括号是为了帮助解释器识别变量的边界**

```bash
for skill in Ada Coffe Action Java 
do
    echo "I am good at ${skill}Script"
done
```
> **注释**  
> 不给`skill`变量加花括号，写成`echo "I am good at $skillScript`，解释器就会把`$skillScript`当成一个变量（其值为空），代码执行结果就不是我们期望的样子了

> **Notes**  
> - 推荐给**所有变量加上`花括号`**，这是个好的编程习惯

## 重新定义变量

```bash
myUrl="http://see.xidian.edu.cn/cpp/linux/"
echo ${myUrl}
myUrl="http://see.xidian.edu.cn/cpp/shell/"
echo ${myUrl}
```

> **Notes**  
> - 第二次赋值的时候**不能写** `$myUrl="http://see.xidian.edu.cn/cpp/shell/`，使用变量的时候才加美元符（`$`）

## 只读变量
- 使用 `readonly` 命令可以将变量定义为只读变量，**只读变量的值不能被改变**

```bash
#!/bin/bash
myUrl="http://see.xidian.edu.cn/cpp/shell/"
readonly myUrl
myUrl="http://see.xidian.edu.cn/cpp/danpianji/"
```
> **输出**  
>  `/bin/sh: NAME: This variable is read only.`

## 删除变量

- 使用 `unset` 命令可以删除变量
```bash
unset variable_name
```

> **Notes**  
> - 变量被删除后**不能**再次使用；
> - `unset` 命令**不能**删除只读变量

```bash
#!/bin/sh
myUrl="http://see.xidian.edu.cn/cpp/u/xitong/"
unset myUrl
echo $myUrl
```
> 上面脚本没有任何输出

## 变量类型

- 运行`shell`时，会同时存在**三种变量**

1. **局部变量**
    - `局部变量`在脚本或命令中定义，仅在当前`shell`实例中有效，其他`shell`启动的程序**不能**访问`局部变量`
2. **环境变量**
    - 所有的程序，包括`shell`启动的程序，都能访问`环境变量`，有些程序需要环境变量来保证其正常运行。
    - 必要的时候shell脚本也可以定义`环境变量`

3. **shell变量**
    - `shell变量`是由`shell`程序设置的`特殊变量`。
    - `shell变量`中有一部分是`环境变量`，有一部分是`局部变量`，这些变量保证了`shell`的正常运行

