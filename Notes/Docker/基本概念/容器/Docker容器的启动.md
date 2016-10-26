# Docker容器的启动

## 启动 `Docker容器`的方式
1. 基于镜像新建一个容器并启动

2. 是将在`终止状态`（`stopped`）的`容器`**重新启动**

> **Notes** 
> - 因为 Docker 的容器实在**太轻量级**了，很多时候用户都是随时*删除*和*新创建*`容器`


## 新建并启动

- 命令
```bash
docker run
```

- 下面的命令输出一个 `Hello World`，之后**终止容器**
   ```bash
   $ sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
   Hello world
   ```

- 启动一个 `bash` 终端，允许用户**进行交互**

    ```bash
    $ sudo docker run -t -i ubuntu:14.04 /bin/bash
    root@af8bae53bdd3:/#
    root@af8bae53bdd3:/# pwd
    /
    ```   

> **Notes**
> - `-t` 选项让`Docker`分配一个`伪终端`（`pseudo-tty`）并**绑定**到容器的`标准输入`上， 
> - `-i` 则让`容器`的标准输入**保持打开**
> - 在**交互模式**下，用户可以通过所创建的`终端`来输入命令

- 利用 `docker run` 来创建容器时，`Docker` 在后台运行的**标准操作**包括
   1. 查本地**是否存在**指定的`镜像`，**不存在**就从`公有仓库`下载
   2. 利用镜像**创建并启动一个`容器`**
   3. 分配一个`文件系统`，并在**只读的镜像层**外面挂载一层**可读写层**
   4. 从`宿主主机`配置的`网桥接口`中桥接一个`虚拟接口`到`容器`中去
   5. 从地址池配置一个 `ip` 地址给`容器`
   6. 执行用户指定的`应用程序`
   7. 执行完毕后`容器`*被终止*


## 启动已终止容器

- 可以利用 `docker start` 命令，直接**将一个已经终止的容器启动运行**。

- `容器`的**核心**为所执行的应用程序，所需要的`资源`都是**应用程序运行所必需**的。
   - 除此之外，并**没有**其它的`资源`。
   - 可以在*伪终端*中利用 `ps` 或 `top` 来查看进程信息。


## 守护态运行【后台(background)运行】

**更多的时候**，需要让 `Docker`在后台运行而**不是**直接把执行命令的结果输出在当前`宿主机`下

- 可以通过添加 `-d`参数来实现

- **Demo**
   1. 不使用 `-d` 参数运行容器
   ```bash
   $ sudo docker run ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
     hello world
     hello world
     hello world
     hello world
   ```
   > **Notes**
   > - `容器`会把输出的结果(`STDOUT`)打印到`宿主机`上面

  2. 使用了 `-d` 参数运行容器 
   ```bash
   $ sudo docker run -d ubuntu:14.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
     77b2dc01fe0f3f1265df143181e7b9af5e05279a884f4776ee75350ea9d8017a
   ``` 
   > **Notes**
   > - `容器`会在后台运行并**不会**把输出的结果(`STDOUT`)打印到`宿主机`上面
   > - 输出结果可以用`docker logs` 查看
   > - `容器`是否会长久运行，是和`docker run`指定的命令有关，和 `-d` 参数**无关**
   > - 使用 `-d` 参数启动后会返回一个**唯一**的 `id`，也可以通过 `docker ps` 命令来查看`容器`信息
    
    ```bash
    $ sudo docker ps
      CONTAINER ID  IMAGE         COMMAND               CREATED        STATUS       PORTS NAMES
      77b2dc01fe0f  ubuntu:14.04  /bin/sh -c 'while tr  2 minutes ago  Up 1 minute        agitated_wright
    ```
- 要获取容器的输出信息，可以通过 `docker logs` 命令    

```bash
$ sudo docker logs [container ID or NAMES]
hello world
hello world
hello world
```