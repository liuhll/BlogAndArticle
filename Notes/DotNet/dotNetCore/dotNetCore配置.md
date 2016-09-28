# 配置

支持多种配置选项。应用程序配置数据内建支持读取 `JSON`、`XML` 和 `INI` 格式的配置文件和环境变量


## 获取和设置配置
- 以前的 ASP.NET 版本的配置文件
  - 依赖于 `System.Configuration` 和 `XML` 配置文件[`Web.config`]

- `dotNetCore`新的配置模型 
  - 精简高效的通过检索多样化提供程序的获取**基于键/值对配置**的能力 
  > **建议**  
  > 在应用程序的 `Startup` 类中只实例化一个 `Configuration`实例。然后使用**选择模式**来访问各自的设置

- `Configuration类`
  - 一个提供了**读写名/值对能力**的 `Providers` 集合
  - **至少需要配置一个提供程序**，使得 `Configuration` 能正常工作   

一般**不会**把配置值存储在一个有层次的结构中，尤其是使用外部文件（如 JSON、XML、INI）时。在此情况下，可以使用以 `:` 符号分隔（**从层次结构的根开始**）的键来取回配置值


## 内建提供程序
配置框架已内建支持 `JSON`、`XML` 和 `INI` 配置文件，内存配置（直接通过代码设置值），从**环境变量**和**命令行参数**中拉取配置
- 开发者并**不受限于**必须使用单个配置提供程序
- 可以把多个配置提供程序组合在一起

### 指定环境的配置文件

```csharp
public Startup(IHostingEnvironment env)
{
    var builder = new ConfigurationBuilder()
        .SetBasePath(env.ContentRootPath)
        .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
        .AddJsonFile($"appsettings.{env.EnvironmentName}.json", optional: true); //手动高亮

    if (env.IsDevelopment())
    {
        // For more details on using the user secret store see http://go.microsoft.com/fwlink/?LinkID=532709
        builder.AddUserSecrets();
    }

    builder.AddEnvironmentVariables();
    Configuration = builder.Build();
}
```
- `IHostingEnvironment` 服务用于**获取当前环境**
- 在 `Development` 环境中，上例高亮行代码将寻找名为 `appsettings.Development.json` 的配置文件，并用其中的值覆盖当前存在的其它值
- ASP.NET 团队建议最后指定环境变量，如此一来本地环境可以覆盖任何部署在配置文件中的设置

## 选项和配置对象
### 选择模式（options pattern）
- 可将`任何类`或 `POCO（Plain Old CLR Object）`转换为**设置类**
- 推荐把你创建的配置根据应用程序的功能**分解为多个配置对象**，从而实现 `ISP`和` SoC`原则

配置选项使用 `Configure<TOption>` 扩展方法。你可以通过**委托**或**绑定配置选项**的方式来进行配置 

```csharp
public void ConfigureServices(IServiceCollection services)
{
    // Setup options with DI
    services.AddOptions();                          //手动高亮

    // Configure MyOptions using config by installing Microsoft.Extensions.Options.ConfigurationExtensions
    services.Configure<MyOptions>(Configuration);

    // Configure MyOptions using code
    services.Configure<MyOptions>(myOptions =>      //手动高亮
    {
        myOptions.Option1 = "value1_from_action";   //手动高亮
    });                                             //手动高亮

    // Configure MySubOptions using a sub-section of the appsettings.json file
    services.Configure<MySubOptions>(Configuration.GetSection("subsection"));//手动高亮

    // Add framework services.
    services.AddMvc();
}
```

通过绑定选项来配置选项类型的每一个属性，**实际上是绑定到每一个配置键**
   - `MyOptions.Option1` 属性绑定到键 `Option1`，那么就会从 `appsettings.json` 中读取 `option1` 属性

调用`Configure<TOption>` 将一个 `IConfigureOptions<TOption>` 服务加入**服务容器**，是为了之后应用程序或框架能通过 `IOptions<TOption>` 服务来获取配置选项
- 想从其他途径（比如之前从数据库）获取配置，你可使用 `ConfigureOptions<TOptions>` 扩展方法直接指定经过定制的 `IConfigureOptions<TOption>` 服务

## 自定义提供程序
从 `ConfigurationProvider` 继承并使用来自你配置提供程序的配置来填充 `Data` 属性即可