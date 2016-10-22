# Shell for循环

- Shell支持`for循环`

- `for循环`的一般格式

```bash
for 变量 in 列表
do
    command1
    command2
    ...
    commandN
done
```

> **Nots**  
> - 列表是**一组值**（`数字`、`字符串`等）组成的**序列**，每个值`通过空格`分隔
> - 每循环一次，就将列表中的下一个值赋给变量
> - `in` 列表是**可选的**，如果不用它，`for` 循环使用命令行的位置参数

- 例子1
```bash
for loop in 1 2 3 4 5 #in列表使用空格分割的
do
    echo "The value is: $loop"
done

# 输出
#The value is: 1
#The value is: 2
#The value is: 3
#The value is: 4
#The value is: 5
```

- 例子2

```bash
for str in 'This is a string'
do
    echo $str
done

#输出
#This is a string

for str in "This is a string"
do
    echo $str
done

#输出
#This
#is 
#a
#string
```

- 显示主目录下以 `.bash` 开头的文件

```bash
#!/bin/bash
for FILE in $HOME/.bash*
do
   echo $FILE
done

#输出
#/root/.bash_history
#/root/.bash_logout
#/root/.bash_profile
#/root/.bashrc
```