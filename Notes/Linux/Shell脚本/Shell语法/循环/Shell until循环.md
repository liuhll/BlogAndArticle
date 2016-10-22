# Shell until循环

- `until循环`执行一系列命令直至条件为 `true` 时停止。
    - `until循环`与 `while循环`在处理方式上刚好相反。
- 一般`while循环`优于`until循环`，但在某些时候，也只是**极少数情况**下，`until循环`更加有用

- `until循环`格式

```bash
until command
do
   Statement(s) to be executed until command is true
done

```

> **Notes**
> - `command` 一般为条件表达式，如果返回值为 `false`，则继续执行循环体内的语句，否则跳出循环


- **demo** : 使用 `until` 命令输出 `0 ~ 9` 的数字

```bash
#!/bin/bash
a=0
until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```