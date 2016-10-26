# 删除Docker容器

- 使用 `docker rm` 来删除一个处于*终止状态*的`容器`

```bash
$ sudo docker rm  trusting_newton
trusting_newton
```
> **Notes**
> - 如果要删除一个**运行中**的`容器`，可以添加 `-f` 参数。
>    - `Docker` 会发送 `SIGKILL` 信号给`容器`。

## 清理所有处于终止状态的容器
-  `docker ps -a` 命令可以查看所有已经创建的包括终止状态的容器，如果数量太多要一个个删除可能会很麻烦，
- 用 `docker rm $(docker ps -a -q)` 可以**全部清理掉**

> **Notes**
> - 这个命令其实会试图删除所有的包括还在**运行中**的`容器`
> - 但是, `docker rm` 默认并**不会删除**运行中的`容器`


