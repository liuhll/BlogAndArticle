# 几种常见的Shell

`Shell`是一种`脚本语言`，那么，就必须有`解释器`来执行这些脚本

- `Unix/Linux`上常见的`Shell` `脚本解释器`有`bash`、`sh`、`csh`、`ksh`等，习惯上把它们称作一种`Shell`
   - 常说有多少种`Shell`，其实说的是`Shell脚本解释器`

 ## bash
- `bash`是`Linux`标准**默认**的`shell`
- `BourneAgain Shell`的缩写
- 作者
   - Brian Fox和Chet Ramey

> **特色**  
> - 可以使用类似`DOS`下面的`doskey`的功能，用`方向键`查阅和快速输入并修改命令。
> - **自动**通过查找匹配的方式给出以某字符串开头的命令。
> - 包含了自身的帮助功能，你只要在提示符下面键入`help`就可以得到相关的帮助。


## sh
`Bourne Shell`的缩写，`sh` 是`Unix` 标准默认的`shell`

- 作者
   - Steve Bourne

## ash
- 作者
   - Kenneth Almquist
- Linux中*占用系统资源最少*的一个小`shell`，它只包含`24`个内部命令，
- 因而使用起来很不方便   

## csh
- 作者
   - `William Joy`为代表的共计*47位作者*编成
- 共有`52个`内部命令
- 该`shell`其实是指向`/bin/tcsh`这样的一个`shell`，也就是说，`csh`其实就是`tcsh`   

## ksh
- `ksh` 是`Korn shell`的缩写
- 作者
   - `Eric Gisin`编写

- `42`条内部命令  
- 该`shell`最大的优点
    - 几乎和商业发行版的`ksh`完全兼容，这样就可以在不用花钱购买商业版本的情况下尝试商业版本的性能了 

>  **Notes**   
> - `bash`是 `Bourne Again Shell` 的缩写，是`linux`标准的默认`shell` ，它基于`Bourne shell`，吸收了`C shell`和`Korn shell`的一些特性。
> - `bash`**完全兼容**`sh`，也就是说，用`sh`写的脚本可以不加修改的在`bash`中执行  