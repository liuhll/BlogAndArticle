# Docker Hub

目前 `Docker` 官方维护了一个公共仓库 `Docker Hub`，其中已经包括了超过 `15,000` 的镜像。
- 大部分需求，都可以通过在 `Docker Hub` 中直接下载镜像来实现。

## 登录

- 可以通过执行 `docker login` 命令来输入`用户名`、`密码`和`邮箱`来完成`注册`和`登录`。
-  注册成功后，本地用户目录的 `.dockercfg` 中将**保存用户的认证信息**。


## 基本操作

- 用户**无需登录**即可通过 `docker search` 命令来查找官方仓库中的镜像，
- 利用 `docker pull` 命令来将它下载到本地。

- 例如以 `centos` 为关键词进行搜索：

```bash
$ sudo docker search centos
NAME                                            DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
centos                                          The official build of CentOS.                   465       [OK]
tianon/centos                                   CentOS 5 and 6, created using rinse instea...   28
blalor/centos                                   Bare-bones base CentOS 6.5 image                6                    [OK]
saltstack/centos-6-minimal                                                                      6                    [OK]
tutum/centos-6.4                                DEPRECATED. Use tutum/centos:6.4 instead. ...   5                    [OK]
...
```

- 可以看到返回了很多**包含关键字**的`镜像`，
   - 其中包括*镜像名字*、*描述*、*星级*（*表示该镜像的受欢迎程度*）、*是否官方创建*、*是否自动创建*。
   - **官方的镜像**说明是官方项目组创建和维护的，`automated` 资源允许用户验证镜像的来源和内容。

- 根据是否是官方提供，可将镜像资源分为**两类**。
  1. 一种是类似 `centos` 这样的**基础镜像**，被称为`基础镜像`或`根镜像`。
        - 这些基础镜像是由 `Docker` 公司*创建*、*验证*、*支持*、*提供*。
        - 这样的`镜像`往往使用**单个单词作为名字**。 
  2. 还有一种类型，比如 `tianon/centos` 镜像，它是由 `Docker` 的用户创建并维护的，往往带`有用户名`称前缀。
        - 可以通过前缀 `user_name/` 来指定使用某个用户提供的镜像，
        > - 比如 `tianon` 用户。

- 在查找的时候通过 `-s N` 参数可以指定仅显示评价为`N星`以上的`镜像`。

> - 下载官方 `centos` 镜像到本地。

```bash
$ sudo docker pull centos
Pulling repository centos
0b443ba03958: Download complete
539c0211cd76: Download complete
511136ea3c5a: Download complete
7064731afe90: Download complete
```
- 用户也可以在**登录**后通过 `docker push` 命令来将镜像推送到 `Docker Hub`。

## 自动创建

`自动创建`（`Automated Builds`）功能对于需要经常升级镜像内程序来说，十分方便。 有时候，用户创建了镜像，安装了某个软件，如果软件发布新版本则需要手动更新镜像。。

- `自动创建`允许用户通过 `Docker Hub` 指定跟踪一个`目标网站`（目前支持 `GitHub` 或 `BitBucket`）上的项目，一旦项目发生新的提交，则自动执行创建。

- 要配置`自动创建`，包括如下的步骤：

   1. 创建并登录 `Docker Hub`，以及**目标网站**；
   2. 在目标网站中连接帐户到 `Docker Hub`；
   3. 在 `Docker Hub` 中 配置一个**自动创建**；
   4. 选取一个目标网站中的项目（需要含 `Dockerfile`）和`分支`；
   5. 指定 `Dockerfile` 的位置，并**提交创建**。
   6. 之后，可以 在`Docker Hub` 的 自动创建页面 中跟踪每次创建的状态。