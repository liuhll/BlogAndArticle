# Shell break和continue命令 ---- 跳出循环

- 在`循环`过程中，有时候需要在**未达到循环结束条件时强制跳出循环**
- 像大多数编程语言一样，`Shell`也使用 `break` 和 `continue` 来跳出循环。

## break命令

- `break`命令允许跳出**所有循环**
   - 终止执行后面的**所有循环**

- [break跳出循环例子](../../Shell.Demo/break_loop.sh)   

- **嵌套循环**中，`break` 命令后面还可以跟一个整数，表示跳出`第几层循环`

```bash
break n #表示跳出第 n 层循环
```

- Demo

```bash
#!/bin/bash
for var1 in 1 2 3
do
   for var2 in 0 5
   do
      if [ $var1 -eq 2 -a $var2 -eq 0 ]
      then
         break 2
      else
         echo "$var1 $var2"
      fi
   done
done

# break 2 表示直接跳出外层循环
# 输出
#1 0
#1 5
```

## continue命令
- `continue`命令与`break`命令类似，
   - 只有一点差别，**它不会跳出所有循环，仅仅跳出当前循环**。

```bash
#!/bin/bash
while :
do
    echo -n "Input a number between 1 to 5: "
    read aNum
    case $aNum in
        1|2|3|4|5) echo "Your number is $aNum!"
        ;;
        *) echo "You do not select a number between 1 to 5!"
            continue
            echo "Game is over!"
        ;;
    esac
done

#运行代码发现，当输入大于5的数字时，该例中的循环不会结束
# echo "Game is over!" 永远不会被执行
```

- `continue` 后面也可以跟一个数字，表示跳出`第几层循环`

```bash
continue n
```
- Demo

```bash
#!/bin/bash
NUMS="1 2 3 4 5 6 7"
for NUM in $NUMS
do
   Q=`expr $NUM % 2`
   if [ $Q -eq 0 ]
   then
      echo "Number is an even number!!"
      continue
   fi
   echo "Found odd number"
done

#输出
#Found odd number
#Number is an even number!!
#Found odd number
#Number is an even number!!
#Found odd number
#Number is an even number!!
#Found odd number
```