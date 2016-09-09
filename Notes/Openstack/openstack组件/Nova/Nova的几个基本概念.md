# Nova中的几个基本概念

## OpenStack API类型
- `nova-api` 起到了`Cloud Controller`的作用，主要为所有的`API`查询提供了一个接口
   - 引发多数业务流程的活动（如运行一个实例）
   - 并实施一些政策（主要是配额检查）

1. 程序内部的api主要是给本机程序内部使用   
   - `/nova/compute/api.py`
2. `RpcAPI`，就是通过高级消息队列的方式，实现不同主机的方法的远程调用
   - `/nova/compute/rpcapi.py`

3. 通过`web资源`的方式暴露给外界的`api`，将提供的服务暴露成`web资源`，可以方便外界的访问
   - `WSGI`


## server、manager、driver
### server
- `server`是一个**服务进程**，类似于Linux中的守护进程   
- 一个`server`对应一个`RpcAPI`,接收特定`topic`的消息
- 一个`server`具体有什么功能，由`manager`来决定

### manager
- `manager`顾名思义，一个服务请求的**管理者，处理者**，不做实际的工作

### driver
- `driver`就相当于一个`workers`，**实际的工作都由它来完成**
- 一个`manager`可以对应有多个`driver`
- `driver`可以理解为一个**适配器**

## 组件之间（比如`Scheduler`和`Nova`）到底是如何传递消息的?
###  nova-schedule 
- 接受一个消息队列的**虚拟实例请求**，通过算法决定该请求应该在那台主机上运行
### nova-compute
- 非常重要的守护进程，负责创建和终止虚拟机实例，即管理着虚拟机实例的生命周期

### rpc_dispatcher



