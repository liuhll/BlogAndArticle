# Linux网络通信工具

## ping 命令
`ping` 命令会向网络上的主机发送应答请求，根据响应信息可以**判断远程主机是否可用**

## ftp 工具
`ftp` 是 **File Transfer Protocol** 的缩写，称为`文件传输协议`
- 通过 `ftp` 工具，能够将文件**上传**到远程服务器，
- 也可以从远程服务器**下载**文件

- `ftp` 工具有自己的命令,可以：  
   - 连接并登录远程主机；
   - 查看目录，遍历目录下的文件；
   - 上传或下载文件，包括文本文件、二进制文件等

- **用法**
```
$ ftp hostname or ip-address
```
> **接下来**  
> 会提示你输入用户名和密码，验证成功后会进入主目录，然后就可以使用 ftp 工具的命令进行操作了

| ftp命令 |	说明 |
|:--------|:-------|
| put filename |	将本地文件上传到远程主机。 |
| get filename |	将远程文件下载到本地。 |
| mput file list |	将多个本地文件上传到远程主机。|
| mget file list |	将多个远程文件下载到本地。 |
| prompt off |	关闭提示。默认情况下，使用 `mput` 或 `mget` 命令会不断提示你确认文件的上传或下载。 |
| prompt on |	打开提示。 |
| dir |	列出远程主机当前目录下的所有文件。 |
| cd dirname |	改变远程主机目录。 |
| lcd dirname |	改变本地目录。 |
| quit |	退出登录。 |

> **注意：**  
> 所有的上传和下载都是针对本地主机和远程主机的**当前目录**，如果你希望上传指定目录下的文件，首先要 `cd`到该目录，然后才能上传

## telnet工具
`Telnet`工具可以让我们**连接并登录**到远程计算机

----------------
- ssh

## finger工具

`finger` 可以让我们查看**本地主机**或**远程主机**上的*用户信息*

- 有些系统为了安全会禁用 `finger` 命令

- 查看本机在线用户
```
$ finger
Login     Name       Tty      Idle  Login Time   Office
amrood               pts/0          Jun 25 08:03 (62.61.164.115)
```

- 查看本机指定用户的信息
```
$ finger amrood
Login: amrood                           Name: (null)
Directory: /home/amrood                 Shell: /bin/bash
On since Thu Jun 25 08:03 (MST) on pts/0 from 62.61.164.115
No mail.
No Plan.
```

- 查看远程主机上的在线用户：
```
$ finger @avtar.com
Login     Name       Tty      Idle  Login Time   Office
amrood               pts/0          Jun 25 08:03 (62.61.164.115)
```

- 查看远程主机上某个用户的信息：
```
$ finger amrood@avtar.com
Login: amrood                           Name: (null)
Directory: /home/amrood                 Shell: /bin/bash
On since Thu Jun 25 08:03 (MST) on pts/0 from 62.61.164.115
No mail.
No Plan.
```