# 数据卷容器

如果有一些**持续更新的数据需要在容器之间共享**，最好创建`数据卷容器`

## 什么是数据卷容器？
- **数据卷容器**，其实就是一个*正常的容器*，专门用来提供`数据卷`供其它容器挂载的


## 如何使用数据卷容器？
1. 首先，创建一个名为 `dbdata` 的`数据卷容器`
```bash
$ sudo docker run -d -v /dbdata --name dbdata training/postgres echo Data-only container for postgres
```

2. 然后，在**其他容器**中使用 `--volumes-from` 来挂载`dbdata` 容器中的`数据卷`
```bash
$ sudo docker run -d --volumes-from dbdata --name db1 training/postgres
$ sudo docker run -d --volumes-from dbdata --name db2 training/postgres
```

> **Notes**  
> - 可以使用**超过一个**的 `--volumes-from` 参数来指定从**多个容器**挂载*不同的`数据卷`*。 
> - 也可以从其他已经挂载了`数据卷`的`容器`来**级联挂载`数据卷`**。  
>    ```bash
>     $ sudo docker run -d --name db3 --volumes-from db1 training/postgres
>    ```
> - 使用 `--volumes-from` 参数所挂载数据卷的容器自己并**不需要保持在运行状态**
> - 如果删除了挂载的容器（包括 `dbdata`、`db1` 和 `db2`），数据卷并**不会**被自动删除。
>      - 如果要删除一个数据卷，必须在删除最后一个还挂载着它的`容器`时使用 `docker rm -v` 命令来指定同时**删除关联的`容器`**