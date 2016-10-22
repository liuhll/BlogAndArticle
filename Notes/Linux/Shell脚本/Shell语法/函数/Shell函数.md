# Shell函数：Shell函数返回值、删除函数、在终端调用函数

- `函数`可以让我们将一个复杂功能划分成若干模块，让程序结构更加清晰，**代码重复利用率更高**

- `Shell` 也支持`函数`。`Shell函数`必须**先定义后使用**

## 函数的定义

1. 函数定义格式1

```bash
function_name () {
    list of commands
    [ return value ]
}

```

2. 可以在函数名前加上关键字 `function`

```bash
function function_name () {
    list of commands
    [ return value ]
}
```

## 函数返回值
- 函数`返回值`，可以显式增加`return语句`；
- 如果不加，会将**最后一条命令运行结果**作为`返回值`
- Shell 函数返回值只能是`整数`，一般用来**表示函数执行成功与否**，`0`表示成功，其他值表示失败 
- 如果 `return` 其他数据，比如一个`字符串`，往往会得到错误提示："numeric argument required"
- 如果一定要让函数返回`字符串`，那么可以先定义一个变量，用来接收函数的计算结果，脚本**在需要的时候访问这个变量来获得函数返回值**。

- Demo 
   - 带有`return语句`的函数

    ```bash
    #!/bin/bash
    funWithReturn(){
       echo "The function is to get the sum of two numbers..."
       echo -n "Input first number: "
       read aNum
       echo -n "Input another number: "
       read anotherNum
       echo "The two numbers are $aNum and $anotherNum !"
       return $(($aNum+$anotherNum))
    }
    funWithReturn
    # Capture value returnd by last command
    ret=$? #函数返回值在调用该函数后通过 $? 来获得 
    echo "The sum of two numbers is $ret !"
       
    ``` 
> **输出**  

```
The function is to get the sum of two numbers...
Input first number: 25
Input another number: 50
The two numbers are 25 and 50 !
The sum of two numbers is 75 !
```

- 函数嵌套的例子

```bash
#!/bin/bash
# Calling one function from another
number_one () {
   echo "Url_1 is http://see.xidian.edu.cn/cpp/shell/"
   number_two
}
number_two () {
   echo "Url_2 is http://see.xidian.edu.cn/cpp/u/xitong/"
}
number_one

# 输出
#Url_1 is http://see.xidian.edu.cn/cpp/shell/
#Url_2 is http://see.xidian.edu.cn/cpp/u/xitong/

```

## 输出函数
- 与删除变量一样，删除函数也可以使用 `unset` 命令，不过要加上 `.f` 选项

```bash
$ unset .f function_name
```

> **Notes**  
> - 如果希望直接从终端调用函数，可以将函数定义在`主目录`下的 `.profile` 文件，这样每次登录后，在命令提示符后面输入函数名字就可以立即调用