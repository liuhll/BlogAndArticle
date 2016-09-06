# Nova组件

> [OpenStack Nova组件](http://www.aboutyun.com/thread-6733-1-1.html)

- 一套虚拟化管理程序，还可以**管理网络**和**存储**
  - Essex版本后，Nova开始做减法
  > 和网络相关的内容，包括安全组，交给Quantum负责，存储相关的交给Cinder负责。调度有关的内容，会交给新的项目Marconi。
- `Nova`是OpenStack云中的计算组织控制器
- 支持OpenStack云中`实例（instances）(虚拟机)`生命周期的所有活动都由Nova处理
- Nova成为一个负责管理`计算资源`、`网络`、`认证`、所需可扩展性的平台
- Nova自身**并没有提供任何虚拟化能力**，相反它使用`libvirt API`来与被支持的`Hypervisors`交互

## 功能和特点
1. 实例生命周期管理
2. 管理计算资源
3. 网络和认证管理
4. `REST`风格的`API`
5. 异步的**一致性**通信
6. `Hypervisor`透明：支持`Xen`,`XenServer/XCP`,`KVM`, `UML`, `VMware` `vSphere` and `Hyper-V`
   - Nova对各种Hyperv的支持
   - `KVM`和`XEN`，基本是最好的。
   - 微软的`Hyper-V`算是很不错


## 主要组件
- API Server (nova-api)
- Message Queue (rabbit-mq server)
- Compute Workers (nova-compute)
- Network Controller (nova-network)
- Volume Worker (nova-volume)
- Scheduler (nova-scheduler)  
![Nova逻辑图](../images/nova-01.png)

### API Serve ---- nova-api
- 对外**提供一个与云基础设施交互的接口**，也是外部可用于管理基础设施的唯一组件
- `API Server`通过消息队列（`Message Queue`）轮流与云基础设施的相关组件通信

### Message Queue ---- Rabbit MQ Server
- OpenStack 节点之间通过`消息队列(MQ)`使用`AMQP（Advanced Message Queue Protocol）`完成通信
- `Nova` 通过**异步调用** *请求响应*，使用回调函数在收到响应时触发
- 像是网络上的一个`hub`，
nova各个组件之间的通信几乎都是靠它进行的，当前的Queue是用`RabbitMQ`实现的，它和database一起为各个守护进程之间传递消息

### Compute Worker ---- nova-compute
- 管理实例生命周期
- 通过`Message Queue`接收实例生命周期管理的请求，并承担操作工作
- 生产环境的云部署中有一些`compute workers`
- 实例部署在哪个可用的`compute worker`上取决于**调度算法**

### Network Controller ---- nova-network
- 处理主机地网络配置
   - `IP`地址分配、
   - 为项目配置`VLAN`、
   - 实现`安全组`、
   - 配置`计算节点网络`

### Volume Workers ---- nova-volume   
- 管理基于`LVM（ Logical Volume Manager ）`的实例卷,有卷的相关功能
  1. 新建卷
  2. 删除卷
  3. 为实例附加卷
  4. 为实例分离卷
- `卷`为实例提供一个持久化存储
- 当一个卷从实例分离或者实例终止（这个卷附加在该终止的实例上）时，这个卷保留着存储在其上的数据。当把这个卷重附加载相同实例或者附加到不同实例上时，这些数据依旧能被访问
   > 一个实例的重要数据几乎总是要写在卷上，这样可以确保能在以后访问

### Scheduler ---- nova-scheduler
- 调度器`Scheduler`
- 作为一个称为`nova-schedule`**守护进程**运行，通过恰当的**调度算法**从**可用资源池**获得一个**计算服务**
- Scheduler会根据诸如`负载`、`内存`、`可用域的物理距离`、`CPU构架`等作出**调度决定**
- nova scheduler实现了一个**可插入式的结构**
- 基本的调度算法
   - 随机算法：计算主机在所有可用域内随机选择
   - 可用域算法：跟随机算法相仿，但是计算主机在指定的可用域内随机选择。
   - 简单算法：这种方法选择负载最小的主机运行实例。负载信息可通过负载均衡器获得。


> `nova`的各个组件是以**数据库**和**队列**为中心进行通信的
