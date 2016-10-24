# Shell case esac语句

`case ... esac` 与其他语言中的 `switch ... case` 语句类似，是一种`多分枝选择结构`

- `case` 语句匹配**一个值**或**一个模式**，如果匹配成功，*执行相匹配的命令*

- `case语句`格式

```bash
case 值 in
模式1)
    command1
    command2
    command3
    ;;
模式2）
    command1
    command2
    command3
    ;;
*)
    command1
    command2
    command3
    ;;
esac
```

> **Notes**  
> - `取值`后面必须为关键字 `in，**每一模式必须以`右括号`结束**
> - `取值`可以为`变量`或`常数`
> - 匹配发现`取值`符合某一`模式`后，其间所有命令开始执行直至 `;;`
>     - `;;` 与其他语言中的 `break` 类似，意思是跳到整个 `case` 语句的最后
> - `取值`将检测匹配的每一个`模式`。一旦**模式匹配**，则执行完匹配模式相应命令后不再继续其他模式
> - 如果**无一匹配模式**，使用星号 `*` 捕获该值，再执行后面的命令

- [`case...esac`例子](../../Shell.Demo/case.expression.sh)

- 例子2

```bash
#!/bin/bash
option="${1}"
case ${option} in
   -f) FILE="${2}"
      echo "File name is $FILE"
      ;;
   -d) DIR="${2}"
      echo "Dir name is $DIR"
      ;;
   *) 
      echo "`basename ${0}`:usage: [-f file] | [-d directory]"
      exit 1 # Command to come out of the program with status 1
      ;;
esac
```

> **运行结果**
```bash
$./test.sh
test.sh: usage: [ -f filename ] | [ -d directory ]
$ ./test.sh -f index.htm
$ vi test.sh
$ ./test.sh -f index.htm
File name is index.htm
$ ./test.sh -d unix
Dir name is unix
$
```