# .net Core 入门体验

[通过几个Hello World感受.NET Core全新的开发体验](http://www.cnblogs.com/artech/p/net-core-hello-world.html)
## 核心特性
- `COM`
   -  `Cross-Platform`
   - `Open-Source`
   - `Modularization`

## 开发环境
- 运行环境.NET Core SDK
  - 跨平台: `Windows`、`Linux`、`Mac`

- IDE
   - visual Studio Core
   - visual Studio 2015

- CLI
  - dotnet 
     1. `new`
     2. `restore`
     3. `build`
     4. `run`
     5. `publish`
  - `yo aspnet`



## project.json
项目自身的设置, 整个文件由四个节点组成。
- `version`定义目标项目的**版本**
- `buildOptions`用来定义目标项目**编译选项**
- `dependencies`在用来存放针对`NuGet包`的依赖 
- `frameworks`节点:创建的项目可以针对**一个或者多个**`Framework`（可以同时在`.NET Framework`和`.NET Core`上运行），支持的`Framework`定义在`frameworks`节点

## 程序集引用
针对NuGet的依赖主要有两种类型,执行`dotnet restore`命令获取并在本地安装所有需要的`NuGet包`
1. 一种是针对**所有`Framework`的**，它们会直接定义在`dependencies节点`下
2. 则是针对**某个具体`Framework`**的，定义的定义为当前`Framework`节点下的`dependencies`子节点

## ASP.NET Core应用
ASP.NET Core应用的寄宿依赖于一个`WebHost`对象，后者则通过对应的工厂`WebHostBuilder`创建，为此我们将针对`WebHost`的创建定义在作为入口点的`Main方法`中。
- ASP.NET Core的**核心管道**定义在NuGet包`Microsoft.AspNetCore.Hosting`
- 以`Self-Host`的方式寄宿`ASP.NET Core`应用还需要一个`Server`
   - 定义在`Microsoft.AspNetCore.Server.Kestrel`这个NuGet包中的`KestrelServer`

ASP.NET Core应用的背后是一个由`Server`和`Middleware`构成的**管道**

### Server
- `Server`实现针对请求的`监听`、`接收`和`响应`
- `WebHostBuilder`的`UseKestrel`方法为管道注册了必不可少`Server`


### Middleware
- 注册的`Middleware`则负责对请求**进行处理**
- `Middleware`的注册在实现在由`UseStartup`方法注册的启动类型中
  - 在Configure方法中调用`ApplicationBuilder`的扩展方法`Run`注册了唯一的`Middleware`

### 自行指定监听地址
- 默认的监听地址`http://localhost:5000/`
- 自行指定这个监听地址，该地址可以通过调用`WebHostBuilder`的扩展方法`UseUrls`来指定


## ASP.NET Core MVC应用
建立在`ASP.NET Core`的所有的开发框架都是**通过注册到管道中的某一个或者多个`Middleware`实现的**

- 针对MVC的`Middleware`实现了`路由`、`Controller的激活`、`Action方法的执行`以及`View`的呈现
- 相关的类型通过`Microsoft.AspNetCore.Mvc`这个NuGet包承载

----------------
- ASP.NET Core MVC相关`Middleware`的注册同样实现在`Startup`类型的`Configure`方法中
- 调用`ApplicationBuilder`的扩展方法`UseMvc`注册了这个`Middleware`
   - 这个`Middleware`需要使用到**相关的服务**，所以我们在另一个名为`ConfigureServices`的方法中通过调用`ServiceCollection`的扩展方法`AddMvc`注册了这些服务

- 使用到了`Razor引擎`，我们同样需要将相关的NuGet包`Microsoft.AspNetCore.Razor.Tools`按照如下的方式添加到`project.json`文件中  
  ```
  "buildOptions": {  
        "preserveCompilationContext": true
      },
       "dependencies": {
        "Microsoft.AspNetCore.Mvc":"1.0.0",
        "Microsoft.AspNetCore.Razor.Tools": {
         "version": "1.0.0-preview2-final",
         "type": "build"
       }
  ```
- `View`的定位依赖于一个根路径，所以我们需要按照如下的方式调用`WebHostBuilder`的`UseContentRoot`方法将当前目录设置为此根目录  
```csharp
     public class Program
        {
           public static void Main(string[] args)
           {
               new WebHostBuilder()
               .UseKestrel()
               .UseStartup<Startup>()
               .UseContentRoot(Directory.GetCurrentDirectory())
               .UseUrls("http://localhost:8888/", "http://localhost:9999/")
               .Build()
               .Run();
           }
       }
```