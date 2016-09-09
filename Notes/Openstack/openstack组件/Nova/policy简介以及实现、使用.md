# Policy
- 首先还是先来了解一下什么是`policy`，它是用来做什么的?
- openstack的用户管理
  - `Users`
  - `Tenants`
  -  `Roles`

- `policy`就是用来控制某一个`User`在某个`Tenant`中的`权限`的
  - 这个`User`能执行什么操作，不能执行什么操作，就是通过`policy`机制来实现的
  - `policy`就是一个`json文件`

- 角色(`role`)
   - 是权限的集合，可以将`role`赋予某`个user`，使这个`user`拥有相应的权限，方便用户权限管理
   