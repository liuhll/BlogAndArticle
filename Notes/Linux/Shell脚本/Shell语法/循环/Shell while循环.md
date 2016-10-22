# Shell while循环

- `while循环`用于不断执行一系列命令，也用于从输入文件中读取数据
  - **命令**通常为测试条件

- 语法
```bash
while command
do
   Statement(s) to be executed if command is true
done
```  

> **Notes**
> - 命令执行完毕，控制返回循环顶部，从头开始**直至测试条件为假**

- demo
```bash
COUNTER=0
while [ $COUNTER -lt 5 ]
do
    COUNTER='expr $COUNTER+1'
    echo $COUNTER
done

#输出
#1
#2
#3
#4
#5
```

- demo2
   - `while循环`可用于读取键盘信息

    ```bash
    echo 'type <CTRL-D> to terminate'
    echo -n 'enter your most liked film: '
    while read FILM
    do
        echo "Yeah! great film the $FILM"
    done

    # 输出
    #type <CTRL-D> to terminate
    #enter your most liked film: Sound of Music
    #Yeah! great film the Sound of Music
    ``` 