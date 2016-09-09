# openstack Token 及 endpoints

## Token
- 什么是`token`？
   - 拿到了用户的`token`就相当于取得了进入`openstack`这个大工厂大门的钥匙，有了这个钥匙，才能进入这个工厂大显身手
- 如何拿到`Token`？
  - 必须知道用户的相关信息，其中`用户名`和`密码`是**必须的**
  - 如果还想取得更多的信息，*例如用户对各种服务包括`glance`, `keystond`的访问`endpoint`,* 还需要提供用户的`tenant`信息
  - Token = User + Password + Tenant
  > - 对于**终端用户**来说，因为`用户名`，`密码`以及`tenant`名更为直观，所以很少会直接用`token`进行操作
  > - 对于**自动化测试**来说，因为要直接和相关`api`打交道，取得`token`就相当有必要
- 如果在请求`token`的时候同时提供了`tenant`信息，**则可以额外获取用户相关的`endpoints`信息**
- 用户每次发出一次请求，就会生成一个`token`,
  同时会在`glance`数据库的`token`表内生成一个记录。每个`token`的有效时间**缺省为24个小时**

- 取得用户`token`的命令
 1. 命令行
```
      # curl -X POSThttp://localhost:5000/v2.0/tokens -d '{"auth":{"passwordCredentials":{"username":"username", "password":"password"}}}' -H"Content-type: application/json"
```  

> - 其中`localhost:5000`是`openstack keystone`服务的`endpoint`, 如果没有特殊的设置，`5000`就是`keystone`服务进程的端口号
> -  `/v2.0/token` 是openstack api里定义的取得`token`的`URI`， 请求方式为`POST`

  2. 编程实现取得用户token
  ```python
import httplib2
import json
http_obj =httplib2.Http()
headers = {}
body = {
    "auth": {
            "passwordCredentials":{
                "username":'username',
                "password":'password',
            },
            "tenantName":'tenantname',
        },
    }
req_url ="http://localhost:5000/v2.0/tokens"
method ="POST"
headers['Content-Type']= 'application/json'
headers['Accept']= 'application/json'
resp, token =http_obj.request(req_url, method,
                               headers=headers,body=json.dumps(body))
print resp
print token
  ```