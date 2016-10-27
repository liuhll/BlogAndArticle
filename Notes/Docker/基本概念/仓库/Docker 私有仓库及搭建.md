# Docker 私有仓库

- 私人或企业内部使用的docker仓库
- `docker-registry` 是官方提供的工具，可以**用于构建私有的镜像仓库**

## 安装运行 docker-registry

###  安装`docker-registry`的方法

1. **容器运行**
2. **本地安装**


### 使用docker运行`docker-registry`
- 安装了 `Docker` 后，可以通过获取官方 `registry` 镜像来运行

```bash
$ sudo docker run -d -p 5000:5000 registry
```


- 可以通过指定参数来配置**私有仓库位置**
   ```bash
   $ sudo docker run \
         -e SETTINGS_FLAVOR=s3 \
         -e AWS_BUCKET=acme-docker \
         -e STORAGE_PATH=/registry \
         -e AWS_KEY=AKIAHSHB43HS3J92MXZ \
         -e AWS_SECRET=xdDowwlK7TJajV1Y7EoOZrmuPEJlHYcNP2k4j49T \
         -e SEARCH_BACKEND=sqlalchemy \
         -p 5000:5000 \
         registry
   ```

- 指定**本地路径**（如 `/home/user/registry-conf` ）下的*配置文件*
```bash
$ sudo docker run -d -p 5000:5000 -v /home/user/registry-conf:/registry-conf -e DOCKER_REGISTRY_CONFIG=/registry-conf/config.yml registry
```  

- 仓库会被创建在容器的 `/tmp/registry` 下
- 可以通过 `-v` 参数来将镜像文件存放在**本地的指定路径**
   -  面的例子将上传的镜像放到 `/opt/data/registry` 目录
   
    ```bash
    $ sudo docker run -d -p 5000:5000 -v /opt/data/registry:/tmp/registry registry
    ```

### 本地安装

- 对于 `Ubuntu` 或 `CentOS` 等发行版，可以直接通过**源安装**

- `CentOS`

    ```bash
    $ sudo yum install -y python-devel libevent-devel python-pip gcc xz-devel
    $ sudo python-pip install docker-registry
    ```    

- `Ubuntu`
    
    ```bash
    $ sudo apt-get install -y build-essential python-dev libevent-dev python-pip liblzma-dev
    $ sudo pip install docker-registry
    ```    

- *源码*[docker-registry](https://github.com/docker/docker-registry) 进行安装 
   1. 安装源码包 
    ```bash
    $ sudo apt-get install build-essential python-dev libevent-dev python-pip libssl-dev liblzma-dev libffi-dev
    $ git clone https://github.com/docker/docker-registry.git
    $ cd docker-registry
    $ sudo python setup.py install
    ```
    2. 修改配置文件
       - 主要修改 `dev` 模板段的 `storage_path` 到本地的存储仓库的路径
    ```bash
    $ cp config/config_sample.yml config/config.yml #备份一份，然后修改配置文件
    ```
    3. 启动 `Web` 服务
    
    ```bash
    $ sudo gunicorn -c contrib/gunicorn.py docker_registry.wsgi:application
    ```
    > 或者

    ```bash
    $ sudo gunicorn --access-logfile - --error-logfile - -k gevent -b 0.0.0.0:5000 -w 4 --max-requests 100 docker_registry.wsgi:application
    ```
    > **Notes**
    > - 使用 `curl` 访问本地的 `5000端口`，看到输出 `docker-registry` 的版本信息说明运行成功
    > - `config/config_sample.yml` 文件是示例配置文件

## 在私有仓库上传、下载、搜索镜像

创建好**私有仓库**之后，就可以使用 `docker tag` 来标记一个镜像，然后推送它到仓库，别的机器上就可以下载下来了  

> 私有仓库地址为 `192.168.7.26:5000`  

### `docker tag` 命令

```bash
docker tag IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
```

- `docker tag` 将 `ba58` 这个镜像标记为 `192.168.7.26:5000/test`

```bash
$ sudo docker tag ba58 192.168.7.26:5000/test
root ~ # docker images
REPOSITORY                        TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
ubuntu                            14.04               ba5877dc9bec        6 weeks ago         192.7 MB
ubuntu                            latest              ba5877dc9bec        6 weeks ago         192.7 MB
192.168.7.26:5000/test            latest              ba5877dc9bec        6 weeks ago         192.7 MB
```
- 使用 `docker push` 上传标记的镜像

```bash
$ sudo docker push 192.168.7.26:5000/test
The push refers to a repository [192.168.7.26:5000/test] (len: 1)
....
```
> **Notes**
> - `push`时，发生`tls oversized record received with length 20527`
>     - [参考官网 `Insecure Registry`](https://docs.docker.com/registry/insecure/)
>     - 因为**验证**的原因，简单地处理方式只需在执行`push`命令的机器上执行`service docker stop`停止`docker`服务，
>     - 然后执行`/usr/bin/docker daemon --insecure-registry=192.168.1.104:5000`，
>     - 重新启动，然后就能重新`push`成功了
- 用 `curl` 查看仓库中的镜像。

```bash
$ curl http://192.168.7.26:5000/v1/search
{"num_results": 7, "query": "", "results": [{"description": "", "name": "library/miaxis_j2ee"}, {"description": "", "name": "library/tomcat"}, {"description": "", "name": "library/ubuntu"}, {"description": "", "name": "library/ubuntu_office"}, {"description": "", "name": "library/desktop_ubu"}, {"description": "", "name": "dockerfile/ubuntu"}, {"description": "", "name": "library/test"}]}
```

> **Notes**
> - 看到 `{"description": "", "name": "library/test"}`，表明镜像已经被成功上传
> - 可以到另外一台机器去下载这个镜像

## 批量镜像
- 使用 这个[脚本](https://raw.githubusercontent.com/yeasy/docker_practice/master/_local/push_images.sh) 批量上传本地的镜像到注册服务器中