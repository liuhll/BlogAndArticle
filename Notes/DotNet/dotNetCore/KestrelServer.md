# KestrelServer
[ASP.NET Cor默认跨平台的服务器——KestrelServer](http://www.cnblogs.com/artech/p/KestrelServer.html)
- **跨平台**是ASP.NET Core一个显著的特性，而`KestrelServer`是目前微软推出了唯一一个能够真正跨平台的`Server`
- `KestrelServer`利用一个名为`KestrelEngine`的网络引擎实现对请求的`监听`、`接收`和`响应`
- `KestrelEngine`是在一个名为`libuv`的跨平台网络库上开发

## libuv
- `libev`
  - `Libev`不支持`Windows`，有人在`libev`之上创建了一个抽象层以屏蔽平台之间的差异，这个抽象层就是`libuv`

## KestrelServer  
1. 实现接口`IServer`定义的`Features`属性之外，
2. `KestrelServer`还具有一个类型为`KestrelServerOptions`的只读属性`Options`。这个属性表示对`KestrelServer`所作的相关设置，我们在调用构造函数时通过输入参数`options`所代表的`IOptions<KestrelServerOptions>`对象对这个属性进行初始化。
3. 构造函数还具有另两个额外的参数，它们的类型分别是`IApplicationLifetime`和`ILoggerFactory`，
   - 后者用于创建记录日志的`Logger`
   - 前者与应用的生命周期管理有关

通过调用`WebHostBuilder`的扩展方法`UseKestrel`方法来完成对`KestrelServer`的注册   
- `UseKestrel`方法具有两个重载，其中一个具有同一个类型为`Action<KestrelServerOptions>`的参数，我们可以利用这个参数直接完成对`KestrelServerOptions`的设置

## KestrelServerOptions
`Server`是影响整个`Web应用`响应能力和吞吐量最大的因素之一,对于`KestrelServer`来说，在`构造函数`中作为参数指定的`KestrelServerOptions对象`代表针对它所做的设置

```csharp
 public class KestrelServerOptions
    {   
        //省略其他成员
        public int          MaxPooledHeaders { get; set; }
        public int          MaxPooledStreams { get; set; }
        public bool         NoDelay { get; set; }
        public TimeSpan     ShutdownTimeout { get; set; }
        public int          ThreadCount { get; set; }
    }
```
`KestrelServerOptions`注册的`KetrelServer`在管道中会以依赖注入的方式被创建,采用构造器注入的方式提供其构造函数的参数`options`

1. 可以将`KestrelServer`的相关配置定义在如下一个`JSON文件`()

```json
 { 
        "noDelay"         : false, 
        "shutdownTimeout" : "00:00:10", 
        "threadCount"     : 10 
 } 
```

2. 只需要在启动类型（`Startup`）类的`ConfigureServces`方法中按照如下的方式利用`ConfigurationBuilder`加载这个配置文件并生成相应的`Configuration`对象，最后按照`Options`模型的编程方式完成`KestrelServerOptions`类型和该对象的映射即可

```csharp
 public class Startup
    {
        //其他成员
        public void ConfigureServices(IServiceCollection services)
        {
            IConfiguration configuration = new ConfigurationBuilder()
                .AddJsonFile("KestrelServerOptions.json")
                .Build();
            services.Configure<KestrelServerOptions>(configuration);
       }
   }
```

## ApplicationLifetime
所有实现了`IApplicationLifetime接口`的所有类型及其对应对象统称为`ApplicationLifetime`
- `IApplicationLifetime接口`具有三个CancellationToken类型的属性`ApplicationStarted`、`ApplicationStopping`和`ApplicationStopped`

- 如果试图关闭应用，`StopApplication`方法应该被调用以发出应用正在被关闭的通知。对于`KestrelServer`来说，如果请求处理线程中发生未被处理异常，它会调用这个方法。
- 一个ASP.NET Core应用**利用管道处理请求**，
  - 所以管道的生命周期等同于应用自身的生命周期。
  当我们调用`Run`方法开启`WebHost`时，请求处理管道被构建出来。  
- 如果管道在处理请求时发生未被处理的异常，管道的`Sever`会调用`ApplicationLifeTime`对象的`StopApplication`方法向`WebHost`发送关闭应用的通知以便后者执行一些回收释放工作。

## 监听地址
- 默认的监听地址
  ```
   http://localhost:5000
  ```
### `ServerAddressesFeature`特性  
`Server`的接口`IServer`中定义了一个类型为`IFeatureCollection` 的只读属性`Features`，它表示用于描述当前`Server`的特性集合，`ServerAddressesFeature`作为一个重要的特性，就包含在这个集合之中
- `ServerAddressesFeature`对象是对所有实现了`IServerAddressesFeature`接口的所有类型及其对应对象的统称
   - 该接口具有一个唯一的只读属性返回`Server`的**监听地址列表**

```csharp
    public interface IServerAddressesFeature
    {
        ICollection<string> Addresses { get; }
    }
     
    public class ServerAddressesFeature : IServerAddressesFeature
    {
        public ICollection<string> Addresses { get; }
    }
```   
- 如果没有一个合法的监听地址被添加到这个 `ServerAddressesFeature`对象的地址列表中，`WebHost`会将显式指定的地址（一个或者多个）添加到该列表中

- 针对监听地址的显式设置，最直接的编程方式还是调用`WebHostBuilder`的扩展方法`UseUrls`