# 计算管理(Nova)

## 概述
`Nova`是一套控制器,为单个用户或是使用群组启动`虚拟机实例`
- Openstack 整个生命周期中的所有行为都由`Nova`处理
    - 创建
    - 销毁
    - 挂起
    - 迁移

- `Nova`自身不提供任何虚拟化能力    


## 逻辑架构
 逻辑架构中的绝大数组件可分为两种类型的`Python`编写`守护进程`

![nova逻辑架构](http://c204396.r96.cf1.rackcdn.com/nova-cactus-logical.gif)

1. 接收个协调`API`调用的`WSGI`应用 
     - `nova-api`
2. 执行部署任务的 `Worker守护进程`
     - `nova-compute`
     - `nova-network`
     - `nova-scheduler`

## 物理架构

**无共享**、**基于消息**的架构，非常灵活

- 可将每个`nova-service`安装在单独的服务器
   - 安装`nova`的多种可能性,可多节点部署
- 部署`openstack`过程中唯一的联合依赖性是`Dashboard`必须安装在`nova-api`服务器

- `nova`的几种部署架构
   1. 单节点  
    - 只为尝试`nova`或是*开发目的*
   2. 双节点
    - `云控制器节点`运行除了`nova-compute`之外的所有`Nova`服务
    - `compute节点(计算节点)` 运行`nova-compute`
    - 用于对概念和开发环境的证明
   
   3. 多节点
   - 在双节点的基础上增加更多的`计算节点(compute node)`
   - 更复杂的多节点部署中，增加`卷控制器`和`网络控制器`
   - `消息队列`中大量复制引发性能问题，可以通过增加更多的`Messaging服务器`来解决
   > 只需要`node.conf`中的配置执行的`RabbitMQ服务器`，并且这些服务器能够向它发送消息

## 对主流的Hypervisor的支持架构

![异构Hypervisor支持架构](http://img.blog.csdn.net/20150118201314859)

## 支持的Hyperisor
- `Nova`支持多种`Hyperisor`,但是在一个集群（`cluster`）上的所有`compute`节点只能配置一种相同的`Hyperisor`
- `Nova`支持的`Hyperisor`
   1. KVM : 基于内核的虚拟机
   2. LXC
   3. QEMU
   4. UML
   5. VMware ESX/ESXi
   6. Xen
   7. Hyper-V
   8. Docker
   9. PowerVM
   10. Baremetal

## 与VMware的对接

-------------------------

## Nova关键组件

### API服务(nova-api)
- 一个用`python` 编写的`WEB服务器`，实现了`Restful API`到内部请求消息的转换
- `nova-api`支持两类`API`
   1. `Nova`自定义的`API`  
    > `V2`是主流支持的版本
   2. 兼容`EC1-API`接口，【未来有可能被移除】
    