# Nova关键组件

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


## nova-conductor
从`G`版本开始增加了`nova-conductor`,所有的`nova-compute`原先需要和数据库交互的部分，*都不得直接访问数据库*,而是通过`nova-conductor`获得

- `nova-conductor`相当于`Nova`组件操作数据库的一个中间件

- 引入`nova-conductor`的原因
   1. 数据库安全
   2. `nova-compute`与数据库的解耦更有利于`node-compute` 的后续升级

- `nova-conductor`也承接了一部分的`TaskAPI`任务
    - `TaskAPI任务`主要包含了一些比较耗时的任务（比如创建`虚拟机`）

## nova-scheduler
`Nova`组件实现任务分派的模块，决定如何派遣`compute`和`volume`的请求

- `Scheduler`映射`nova-api`调用到合适的`Openstack Component`,根据指定的算法从可用的资源中获取`Compute`服务器
- 决定`调度器算法`的因素
   - 负载
   - 内存
   - 可用`zone`的物理距离
   - `CPU`体系结构

- 目前`Scheduler`可用的`调度算法` 
  - `Chance`
  - `AZ`
  - `Simple`
  - `滤波器调度器`  

## nova-volume

- 用来管理`块存储设备`,提供附加的块存储挂接给虚拟机
- 目前已经完全被`Cinder`所替代
- 在提供弹性能力的本质上，`nova-volume`和`Cinder`是一样的
   - `Cinder`只是对`nova-volume`的进一步封装，包括对异构设备的支持、水平扩展能力的支持等

- `nova-volume`管理的块设备基于`Linux`的`LVM`(`Logical Volume Manager`),使用`iSCSI`进行挂接

## nova-network
`nova-network`是`Nova`里负责虚拟机网络的组件
- openstack发展了`Neutron`来替代`nova-network`

### 关键概念
1. `fixed_ip`
   - 内网中虚拟机所使用的内部`IP地址`,从虚拟机创建其到虚拟机终止位置，都需要有一个固定的`fixed_ip`来对应这个虚拟机
      - 一个虚拟机必须要有`fixed_ip`
   - 集群的网络类型决定了虚拟机获取`fixed_ip`的方式，具体使用何种方式是在系统中预先配置好的
      - `nova-controller.conf`有一个选项`network_manager`来指定某个具体的方式

2. `floating_ip`        
    - `外网IP`，可以动态指派给虚拟机，也可以随时收回
    - `floating_ip`是可选的
        - 用户需要这台虚拟机可供外网访问时，才需要指派`floating_ip`
    - `floating_ip`不是在虚拟机的虚拟网卡上，而是在`nova-network`的外围的网络接口上分配
    - `nova-network`会根据用户配置指令做`NAT`,将用户的`fixed_ip`映射到外网的`floating_ip` 

### 网络类型
`Nova`支持三种类型的网络:`Flat`、`Flat DHCP`、`VLAN` 
- 在一个云系统中，这三种类型的网络可以同时存在
- 用户不能为给定的项目选择网络类型
   - 一个给定的`compute`部署中，只能配置一种网络类型

1. Flat模式

2. Flat DHCP

3. VLAN         