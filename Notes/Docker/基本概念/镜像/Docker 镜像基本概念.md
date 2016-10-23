# Docker 镜像

## 基本概念

- `Docker镜像`(`Image`): 一个**只读的模板**

> **例子**  
> 一个镜像可以包含一个完整的 ubuntu 操作系统环境，里面仅安装了 Apache 或用户需要的其它应用程序

- `Docker` 提供了一个很简单的机制来创建镜像或者更新现有的镜像
- 用户甚至可以直接从其他人那里**下载一个已经做好的镜像来直接使用**


### Docker的作用
- `镜像`可以用来创建 `Docker容器`


## 获取镜像

可以使用 `docker pull` 命令来从仓库获取所需要的镜像。

- 从 `Docker Hub` 仓库下载一个 `Ubuntu 12.04` 操作系统的镜像
```bash
$ sudo docker pull ubuntu:12.04
```
> **Notes**  
> - 该命令实际上相当于 `$ sudo docker pull registry.hub.docker.com/ubuntu:12.04` 命令，即从注册服务器 `registry.hub.docker.com` 中的 `ubuntu` 仓库来下载**标记**为 `12.04` 的镜像

- 从其他仓库下载
  - 需要指定完整的仓库注册服务器地址
  ```bash
  $ sudo docker pull dl.dockerpool.com:5000/ubuntu:12.04
  ```

- 完成后，即可随时使用该镜像  

## 列出镜像
- 使用 `docker images` 显示**本地已有的镜像**

```bash
$ sudo docker images
REPOSITORY       TAG      IMAGE ID      CREATED      VIRTUAL SIZE
ubuntu           12.04    74fe38d11401  4 weeks ago  209.6 MB
ubuntu           precise  74fe38d11401  4 weeks ago  209.6 MB
ubuntu           trusty   99ec81b80c55  4 weeks ago  266 MB
```

> **Notes**  
> 几个字段信息
> - 来自于哪个仓库，比如 ubuntu
> - 镜像的`标记`，比如 `14.04`
> - 它的 `ID` 号（**唯一**）
> - 创建时间
> - 镜像大小 

- 镜像的 `ID`**唯一标识了镜像**

- `TAG` 信息用来标记来自**同一个仓库的不同镜像**
   
>  **Notes**
> - `ubuntu仓库`中有多个镜像，通过 `TAG `信息来**区分发行版本**
> - 如果不指定具体的标记，则默认使用 `latest` 标记信息

------------------------------------

