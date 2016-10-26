# 终止容器

- 可以使用 `docker stop` 来终止一个运行中的`容器`。

- 此外，当`Docker容器`中指定的**应用终结**时，`容器`也**自动终止**。

> **例子**
> - 例如对于启动了一个终端的`容器`，用户通过 `exit` 命令或`Ctrl+d` 来*退出终端*时，所创建的`容器`立刻终止。

- 终止状态的容器可以用 `docker ps -a` 命令看到

```bash
sudo docker ps -a
CONTAINER ID        IMAGE                    COMMAND                CREATED             STATUS                          PORTS               NAMES
ba267838cc1b        ubuntu:14.04             "/bin/bash"            30 minutes ago      Exited (0) About a minute ago                       trusting_newton
98e5efa7d997        training/webapp:latest   "python app.py"        About an hour ago   Exited (0) 34 minutes ago                           backstabbing_pike

```

- 处于**终止状态**的`容器`，可以通过 `docker start` 命令来重新启动

- `docker restart` 命令会将一个**运行态**的`容器`终止，然后再**重新启动**它

