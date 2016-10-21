# echo 命令

`echo`是`Shell`的一个**内部指令**，用于在屏幕上*打印出指定的`字符串`*

- 命令格式
```bash
echo arg
```
> **Notes**
> - 使用`echo`实现更复杂的输出格式控制


## 显示转义字符

```bash
echo "\"It is a test\""
#输出
#"It is a test"

echo \"It is a test\"
#输出
#"It is a test"

echo "It is a test"
#输出
#It is a test
```

## 显示变量

```bash
name="OK"
echo "$name It is a test"
#输出
#OK It is a test
```

> **Notes**  
> - `双引号`可以省略
> - `单引号`不行，`单引号`里的任何字符都会原样输出，`单引号`字符串中的`变量`是无效的,转义符也无效

- 如果`变量`与`其它字符`相连的话，需要使用大括号（`{ }`）

```bash
mouth=8
echo "${mouth}-1-2009"
#输出
#8-1-2009
```

## 显示换行

```bash
echo -e "OK!\n"
echo "It is a test"
#输出
#OK!
#It is a test
```

## 显示不换行

```bash
echo "OK!\c"
echo "It is a test"
#输出：
#OK!It is a test
```

## 显示结果重定向至文件

```bash
echo "It is a test" > myfile
```
> **Notes**
> - 使用`输出重定向` `>` 将打印到屏幕上的字符串输出的制定的文件中

## 原样输出字符串
- 若需要*原样输出字符串*（`不进行转义`），请使用`单引号`

```bash
echo '$name\"'
# 输出
# name\"
```
> **Notes**
> - `双引号`**可有可无**，`单引号`主要用在**原样输出**中。

## 显示命令执行结果
在`shell`脚本中,使用"``"来执行某个命令，并可以将其执行的结果赋值给某个变量或是直接打印到屏幕

```bash
echo `date`
#输出
#2016年10月21日 星期五 16时45分45秒 CST
# 结果将显示当前日期
```








