# Shell输入输出重定向

- Unix 命令默认从**标准输入设备**(`stdin`)获取输入，将结果输出到**标准输出设备**(`stdout`)显示
    - **标准输入设备**就是*键盘*，
    - **标准输出设备**就是*终端*，即*显示器*

## 输出重定向

- **命令的输出**不仅可以是显示器，还可以很容易的转移向到文件，这被称为`输出重定向`

- 命令输出重定向的语法

```bash
$ command > file # 出到显示器的内容就可以被重定向到文件
```

> **Notes**  
> - 在显示器上不会看到任何输出

```bash
$ who > users # 在显示器上不会看到任何输出
```
> **Notes**  
> - `输出重定向`  `>` 会覆盖文件内容
> - 果不希望文件内容被覆盖，可以使用 `>>` 追加到文件末尾


## 输入重定向

- 和`输出重定向`一样，Unix 命令也可以从文件获取输入

- 语法
    ```bash
    command < file
    ```
    > **Notes**  
    > - 本来需要从键盘获取输入的命令会转移到文件读取内容
    > - 输出重定向是大于号(`>`)，输入重定向是小于号(`<`)

- 计算 `users 文件`中的行数    

```bash
$ wc -l users
2 users
$

$ wc -l < users #将输入重定向到 users 文件
2
$
```
> **Notes**  
> - 上面两个例子的结果不同：
>      - 第一个例子，会输出文件名；
>      - 第二个不会，因为它仅仅知道从标准输入读取内容


## 重定向深入讲解
- 三个文件
   1. `标准输入文件`(`stdin`)：`stdin`的文件描述符为`0`，Unix程序默认从`stdin`**读取数据**。
   2. `标准输出文件`(`stdout`)：`stdout` 的文件描述符为`1`，Unix程序默认向`stdout`**输出数据**。
   3. `标准错误文件`(`stderr`)：`stderr`的文件描述符为`2`，Unix程序会向`stderr`流中**写入错误信息**。
 
- 默认情况下，
   - `command > file` 将 `stdout` 重定向到 `file`
   - `command < file` 将`stdin` 重定向到 `file` 

- 如果希望 `stderr` 重定向到 `file`，可以这样写：

``` bash
$ command 2 > file
```
- 如果希望 `stderr` 追加到 `file` 文件末尾

```bash
$ command 2 >> file
```

> **Notes**
> - `2` 表示`标准错误文件`(`stderr`)

- 希望将 `stdout` 和 `stderr` 合并后重定向到 `file`

```bash
$ command > file 2>&1
```
> 或者

```bash
$ command >> file 2>&1
```

-  希望对 `stdin` 和 `stdout` 都重定向 
    ```bash
    $ command < file1 >file2
    ```
    > **Notes**
    > - `command` 命令将`stdin` 重定向到 `file1`，将 `stdout` 重定向到 `file2`

## 全部可用的重定向命令列表

| 命令 |	说明 |
|:-----|:-----|
| command > file |	将输出重定向到 file。 |
| command < file |	将输入重定向到 file。 |
| command >> file |	将输出以追加的方式重定向到 file。 |
| n > file |	将文件描述符为 `n` 的文件重定向到 file。 |
| n >> file |	将文件描述符为 `n` 的文件以追加的方式重定向到 file。 |
| n >& m |	将输出文件 `m` 和 `n` 合并。 |
| n <& m |	将输入文件 `m` 和 `n` 合并。 |
| << tag |	将开始标记 `tag` 和结束标记 `tag` 之间的内容作为输入。 |


## Here Document
- 可翻译为`嵌入文档`
- `Here Document` 是 Shell 中的一种**特殊的重定向方式**
   - 它的作用是将两个 `delimiter` 之间的内容(`document`) 作为输入传递给 `command`
```bash
command << delimiter
    document
delimiter
```

> **Notes**
> - 结尾的`delimiter` 一定要**顶格写**，前面**不能有任何字符**，后面也**不能有任何字符**，包括`空格`和`tab` 缩进。
> - 开始的`delimiter`前后的空格会被忽略掉

```bash
$ wc -l << EOF
    This is a simple lookup program
    for good (and bad) restaurants
    in Cape Town.
EOF
3
$
```

- 将 Here Document 用在脚本中

```bash
#!/bin/bash
cat << EOF
This is a simple lookup program
for good (and bad) restaurants
in Cape Town.
EOF

#输出
#This is a simple lookup program
#for good (and bad) restaurants
#in Cape Town.
```

## /dev/null 文件
- 如果希望执行某个命令，但又**不希望在屏幕上显示输出结果**，那么可以将输出重定向到 `/dev/null`
   - 类似于`windows`系统下的垃圾箱

```bash
$ command > /dev/null
```

> **Notes**
> - `/dev/null` 是一个**特殊的文件**，
>      - 写入到它的内容都会被丢弃；
>      - 如果尝试从该文件读取内容，那么什么也读不到。
> - 但是 `/dev/null` 文件非常有用，将命令的输出重定向到它，会起到**禁止输出**的效果

- 如果希望屏蔽 `stdout` 和 `stderr`

```bash
$ command > /dev/null 2>&1
```