# 导出和导入容器

## 导出容器

- 导出本地某个`容器`，可以使用 `docker export` 命令

```bash
$ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                    PORTS               NAMES
7691a814370e        ubuntu:14.04        "/bin/bash"         36 hours ago        Exited (0) 21 hours ago                       test
$ sudo docker export 7691a814370e > ubuntu.tar
```
> **Notes**
> - 这样将导出`容器快照`到*本地文件*


## 导入容器快照

- 使用 `docker import` 从`容器快照`文件中再导入为 `镜像`

```bash
$ cat ubuntu.tar | sudo docker import - test/ubuntu:v1.0
$ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              VIRTUAL SIZE
test/ubuntu         v1.0                9d37a6082e97        About a minute ago   171.3 MB
```

- 也可以通过指定 `URL` 或者`某个目录`来*导入*

```bash
$ sudo docker import http://example.com/exampleimage.tgz example/imagerepo
```

## `docker load` 和`docker import`的区别
- 使用 `docker load` 来导入**镜像存储文件**到`本地镜像库`
- 使用 `docker import` 来导入一个**容器快照**到`本地镜像库`

> **区别**
> - `容器快照文件`将**丢弃**所有的历史记录和`元数据`信息（即仅保存`容器`当时的`快照状态`）
> - 而`镜像存储文件`将保存**完整记录，体积也要大**
> - 从`容器快照文件`导入时**可以重新**指定标签等`元数据`信息

