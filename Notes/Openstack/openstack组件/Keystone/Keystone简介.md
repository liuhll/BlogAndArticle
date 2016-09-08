# Keystone
## 简介
- `Keystone（OpenStack Identity Service）`是OpenStack框架中，负责**身份验证**、**服务规则**和**服务令牌**的功能， 
- 它实现了OpenStack的`Identity API`。
- `Keystone`类似一个**服务总线**， 或者说是整个Openstack框架的注册表，
- 其他服务通过`keystone`来注册其服务的`Endpoint`（服务访问的`URL`），任何服务之间相互的调用， 需要经过`Keystone`的**身份验证**， 来获得目标服务的`Endpoint`来找到目标服务

## Keystone基本概念
### User
- 代表可以通过`keystone`进行访问的**人**或**程序**
- User如何通过验证?
   - Users通过**认证信息**（*credentials*，如*密码*、*API Keys*等）进行验证

### Tenant
- 各个服务中的一些**可以访问的资源集合**
   - 在Nova中一个`tenant`可以是一些机器
   - 在S`wift`和`Glance`中一个`tenant`可以是一些镜像存储
   - 在Quantum中一个`tenant`可以是一些网络资源 
- `Users`默认的**总是绑定到某些`tenant`上** 

### Role 
- 代表一组用户可以访问的**资源权限**
- `Users`可以被添加到任意一个**全局的Role** 或 **租户内的Role**
   - 全局的Role
   > 用户的`role`权限作用于所有的租户，即可以对所有的租户执行role规定的权限
   - 租户内的Role   
   > 用户仅能在**当前租户**内执行`role`规定的权限  

### Service
- `Service`即服务，如`Nova`、`Glance`、`Swift`
- 一个服务可以确认当前用户是否具有访问其资源的权限
   - 根据`User`,`Tenant`,`Role`   
- 通常使用一些不同的**名称**表示不同的服务   
- `Role`实际上也是可以绑定到某个`service`的

### Endpoint
- 它是一个服务暴露出来的访问点
- 需要访问一个服务，则必须知道他的`endpoint`
- **endpoint template**
  - 提供了所有存在的服务`endpoints`信息
  - 包含一个`URLs`列表
  - 列表中的每个`URL`都对应一个**服务实例**的访问地址，并且具有`public`、`private`和`admin`这**三种权限**
     1. `public url`可以被全局访问
     2. `private url`只能被局域网访问
     3. `admin url`被从常规的访问中分离
