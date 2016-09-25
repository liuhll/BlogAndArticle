# 中间件 middleware

## 什么是中间件
**中间件**是用于组成应用程序管道来处理请求和响应的`组件`。`管道`内的每一个组件都可以选择是否将请求交给下一个组件、并在管道中调用下一个组件之前和之后执行某些操作。`请求委托`被用来建立`请求管道`，`请求委托`处理每一个 HTTP 请求。

- 请求委托通过使用 `IApplicationBuilder` 类型的 `Run`、`Map` 以及 `Use 扩展方法`来配置，并在`Startup` 类中传给 `Configure` 方法
- 每个单独的`请求委托`都可以被指定为一个**内嵌匿名方法**，或其定义在一个可重用的类中
   - 可重用的类被称作 `中间件` 或 `中间件组件`
   - 每个位于请求管道内的`中间件组件`负责调用管道中`下一个组件`，或`适时短路调用链`

## 用 IApplicationBuilder 创建中间件管道
ASP.NET 请求管道由一系列的请求委托所构成，它们一个接着一个被调用
![中间件](../images/中间件.png)

- 每个委托在下一个委托**之前**和**之后**都有机会执行操作
- 任何委托都能选择停止传递到下一个委托，转而自己处理该请求
  - 请求管道的短路
  - 一种有意义的设计，因为它可以避免不必要的工作
- 将多个请求委托彼此链接在一起；`next` 参数表示管道内下一个委托。通过 **不** 调用 `next` 参数，你可以**中断（短路）管道** 

```csharp
public void ConfigureLogInline(IApplicationBuilder app, ILoggerFactory loggerfactory)
{
    loggerfactory.AddConsole(minLevel: LogLevel.Information);
    var logger = loggerfactory.CreateLogger(_environment);
    app.Use(async (context, next) =>//手工高亮
    {
        logger.LogInformation("Handling request.");
        await next.Invoke();//手工高亮
        logger.LogInformation("Finished handling request.");
    });

    app.Run(async context =>
    {
        await context.Response.WriteAsync("Hello from " + _environment);//手工高亮
    });
}
```


## Run，Map 与 Use
你可以使用 `Run`、`Map` 和 `Use` 配置 **HTTP 管道**
- `Run` 方法将会短路管道（因为它不会调用 `next`请求委托）,`Run` 应该**只能在你的管道尾部被调用**
  - `Run` 是一种惯例，有些中间件组件可能会暴露他们自己的 `Run[Middleware]` 方法，而这些方法只能在管道末尾处运行

- 约定了 `Map*`扩展被用于**分支管道**
   - `Map 扩展方法`用于匹配基于请求路径的请求委托
   - `Map` 只接受路径，并配置单独的中间件管道的功能

## 内置中间件
| 中间件	   | 描述   |
|:-----------|---------|
|[份验证（Authentication）](https://docs.asp.net/en/latest/security/authentication/index.html)|	提供身份验证支持。|
|[跨域资源共享（CORS）](https://docs.asp.net/en/latest/security/cors.html)|	配置跨域资源共享。CORS 全称为 Cross-Origin Resource Sharing。|
|[路由（Routing）](https://docs.asp.net/en/latest/fundamentals/routing.html)|	定义和约定请求路由。|
|[会话（Session）](https://docs.asp.net/en/latest/fundamentals/app-state.html#id12)|	提供对管理用户会话（session）的支持。|
|[静态文件](https://docs.asp.net/en/latest/fundamentals/static-files.html)	|提供对静态文件服务于目录浏览的支持。|

## 编写中间件
对于更复杂的请求处理功能，ASP.NET 团队推荐在他们自己的类中实现中间件，并暴露 `IApplicationBuilder` 扩展方法，这样就能通过`Configure`方法来被调用
- [CodeLabs 中间件教程](https://github.com/Microsoft-Build-2016/CodeLabs-WebDev/tree/master/Module2-AspNetCore)