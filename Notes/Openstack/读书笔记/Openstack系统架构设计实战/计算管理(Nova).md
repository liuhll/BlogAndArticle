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

- 启动`Nova`
   1. 读取配置文件，读取配置参数，并且根据配置完成初始化消息队列[用于后续与别的组件进行内部消息交互]
   2. 根据配置文件中的配置项启动[`WSGI服务器`](http://pep-3333-wsgi.readthedocs.io/en/latest/#) 
      - 配置文件中的每一个`API`对应一个服务器
      - 根据系统的`CPU核心数n`，每个`WSGI服务器`都会有`n个worker`协程去处理请求

- nova-api端口号
   - EC2的API对应的端口号 `8773`
   - 自定义的API对应的端口号`8774`

- `node-api`利用`WSGI框架`,实现`url`到`action`的映射
    - `action`是对应模块里面的具体实现的函数

### 消息队列【AMQP】
- `AMQP`[Advanced Message Queuing Protocol]: 是一个提供**统一消息服务**的`应用层`标准**高级消息队协议**
  - 应用层协议的一个**开放标准**
  - 为**面向消息的中间件**而设计
  - 基于此协议的**客户端中间件**可以*传递消息*，并不受`客户端`/`中间件`不同产品、不同开发语言等条件的限制

- 典型的`AMQP`的产品
   - RabbitMQ
   - Qpid
- openstack采用消息队列作为**组件间**通信的`中间件`

- 模型概念主要由连个组件
    - Exchange  ----  `X`  ----- 交换器
    - Queue     ---- 队列
   
   ![AMQP消息模型示意](http://img2016.itdadao.com/d/file/tech/2016/07/20/cd22947062016501815.png)

   > **Notes**  
   > - `交换器` ：**交换消息的实体**，起到消息路由、过滤的作用
   > - `队列` ：**接受消息的实体**,本质上是一个缓存消息的队列
   > - `绑定器(Bind)`:将`交换器`的和`队列`连接起来，并且封装消息的路由信息

- 一个客户发送消息，哪些`Client`可以收到消息，其**核心**在于`交换器`，`RoutingKey`，`队列`的关系

- openstack使用的交换器类型
    1. Fanout
    2. Direct
    3. Topic

- [RabbitMQ 使用参考](https://www.zouyesheng.com/rabbitmq.html#toc21)    


### nova-compute
- 负责管理虚拟机
   - 单独运行于承载分配虚拟机的主机之上
- `nova-compute`通过消息队列获取任务然后执行

- 典型的业务流程
   - `nova-compute`从消息队列中获取分发自己的消息
       - 消息队列的消息体里定义了一系列的`key/values`值对，需要对消息体进行解析
       - key是`method`,key对应的value指明了nova-compute需要完成的任务

- [OpenStack建立实例完整过程源码详细分析](http://blog.csdn.net/gaoxingnengjisuan/article/details/9130213)

- `nova-compute`从消息队列中获取的任务主要有以下几个:
  - 运行实例
  - 终止实例
  - 重启实例
  - 添加卷
  - 去除卷
  - 获得控制输出
  - 迁移实例
  - 诊断实例
  - 搁置


  
## nova-cell
- `G`版本开始引入

- Cell有自己的DB和AMQP，并且是树状结构，Cell之间使用AMQP通信
- 顶层的Cell称为`API Cell`，有自己的`nova-api`
- 子Cell无`nova-api`服务，子Cell定时上报资源给父Cell，接受父Cell的调度
- nova-cell架构
  ![nova-cell架构图](http://img.blog.csdn.net/20131030175522375?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZ2FveGluZ25lbmdqaXN1YW4=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
