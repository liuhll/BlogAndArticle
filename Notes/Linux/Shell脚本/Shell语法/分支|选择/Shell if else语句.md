# Shell if else语句

- `if` 语句(`判断语句`)通过`关系运算符`判断`表达式`的`真|假`来决定执行**哪个分支**
- Shell 有三种 `if ... else` 语句
   1. `if ... fi` 语句；
   2. `if ... else ... fi` 语句；
   3. `if ... elif ... else ... fi` 语句。

##  if ... else 语句

- 语法：

```bash
if [ expression ]
then
   Statement(s) to be executed if expression is true
fi
```
> **Notes**  
> - `expression` 返回 `true`，`then` 后边的语句将会被执行；
> - 如果返回 `false`，不会执行任何语句
> - 最后**必须**以 `fi` 来结尾**闭合 `if`**，`fi` 就是 `if` **倒过来拼写**
> - `expression` 和方括号(`[ ]`)之间**必须有空格**，否则会*有语法错误*

- [`if`例子](../../Shell.Demo/if.expression.sh)

- `if ... else` 语句也可以写成一行，以命令的方式来运行

```bash
if test $[2*3] -eq $[1+5]; then echo 'The two numbers are equal!'; fi;
```

## if ... else ... fi 语句

- 语法

```bash
if [ expression ]
then
   Statement(s) to be executed if expression is true
else
   Statement(s) to be executed if expression is not true
fi
```

> **Notes**  
> -  `expression` 返回 `true`，那么 `then` 后边的语句将会被执行；
> - 否则，执行 `else` 后边的语句 

- [`if...else`例子](../../Shell.Demo/if.else.expression.sh)

##  if ... elif ... fi 语句
- 对`多个条件`进行判断
- 语法

```bash
if [ expression 1 ]
then
   Statement(s) to be executed if expression 1 is true
elif [ expression 2 ]
then
   Statement(s) to be executed if expression 2 is true
elif [ expression 3 ]
then
   Statement(s) to be executed if expression 3 is true
else
   Statement(s) to be executed if no expression is true
fi
```

> **Notes**  
> -  `expression` 的值为 `true`，就执行哪个`expression` 后面的语句；
> - 如果都为 `false`，那么**不执行任何语句**

- [if...elif...else例子](../../Shell.Demo/if.elif.expression.sh)

## `if...else`与`test`语句的结合使用

```bash
num1=$[2*3]
num2=$[1+5]
if test $[num1] -eq $[num2]
then
    echo 'The two numbers are equal!'
else
    echo 'The two numbers are not equal!'
fi
```
> **Notes**
> - `test` 命令用于检查某个条件是否成立，与方括号(`[ ]`)类似