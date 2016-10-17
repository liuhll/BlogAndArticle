# Linux系统日志及日志分析


`Linux系统`拥有非常**灵活**和**强大**的日志功能，可以保存几乎所有的操作记录，并可以从中检索出我们需要的信息

## 日志守护进程
- 默认的日志守护进程为 `syslog`
   - 位于 `/etc/syslog` 或 `/etc/syslogd`，
   - 默认配置文件为 `/etc/syslog.conf`

- 任何希望生成日志的程序都可以向 `syslog` 发送信息

- Linux系统内核和许多程序会产生各种`错误信息`、`警告信息`和`其他的提示信息`，这些信息对管理员了解系统的运行状态是非常有用的，所以应该把它们写到`日志文件`中去

- `syslog`可以根据日志的`类别`和`优先级`将日志保存到**不同**的文件中
> **例如：**  
> - 为了方便查阅，可以把`内核信息`与`其他信息`分开，单独保存到一个独立的`日志文件`中

- **默认配置**下，`日志文件`通常都保存在`/var/log`目录下

## 日志类型
- 下面是常见的日志类型

| 类型 |	说明 |
|:-----|:------|
| auth |	用户认证时产生的日志，如`login`命令、`su`命令。 |
| authpriv |	与 `auth` 类似，但是只能被特定用户查看。 |
| console |	针对系统控制台的消息。 |
| cron |	系统定期执行计划任务时产生的日志。 |
| daemon |	某些守护进程产生的日志。 |
|ftp	| `FTP`服务。 |
| kern |	系统内核消息。 |
| local0.local7 |	由自定义程序使用。 |
| lpr |	与打印机活动有关。 |
| mail |	邮件日志。 |
| mark |	产生时间戳。系统每隔一段时间向日志文件中输出当前时间，每行的格式类似于 `May 26 11:17:09 rs2 -- MARK --`，可以由此推断系统发生故障的大概时间。 |
| news |	网络新闻传输协议(`nntp`)产生的消息。 |
| ntp |	 网络时间协议(`ntp`)产生的消息。 |
| user |	用户进程。 |
| uucp |	`UUCP`子系统。 |


## 日志优先级

- 常见的日志优先级

| 优先级 |	说明 |
|:------|:-----|
| emerg |	**紧急情况**，系统**不可用**（例如系统崩溃），一般会通知所有用户。 |
| alert	| 需要立即修复，例如系统数据库损坏。 |
| crit |	**危险情况**，例如硬盘错误，可能会阻碍程序的部分功能。 |
| err |	一般错误消息。 |
| warning |	警告。 |
| notice |	不是错误，但是可能需要处理。 |
| info |	通用性消息，一般用来提供有用信息。 |
| debug |	调试程序产生的信息。 |
| none |	没有优先级，不记录任何日志消息。 |

## 常见日志文件

- 所有的系统应用都会在 `/var/log` 目录下创建`日志文件`，或创建子目录再创建`日志文件`


| 文件/目录 |	说明 |
|:---------|:------|
| /var/log/boot.log |	开启或重启日志。 |
| /var/log/cron |	计划任务日志 |
| /var/log/maillog |	邮件日志。 |
| /var/log/messages |	该`日志文件`是许多进程日志文件的**汇总**，从该文件可以看出任何入侵企图或成功的入侵。 |
| /var/log/httpd 目录 |	`Apache HTTP` 服务日志。 |
| /var/log/samba 目录 |	`samba` 软件日志 |


## /etc/syslog.conf 文件
`/etc/syslog.conf` 是 `syslog` 的配置文件，会根据`日志类型`和`优先级`来决定将日志保存到何处

- 典型的 `syslog.conf` 文件格式

```
*.err;kern.debug;auth.notice /dev/console
daemon,auth.notice           /var/log/messages
lpr.info                     /var/log/lpr.log
mail.*                       /var/log/mail.log
ftp.*                        /var/log/ftp.log
auth.*                       @see.xidian.edu.cn
auth.*                       root,amrood
netinfo.err                  /var/log/netinfo.log
install.*                    /var/log/install.log
*.emerg                      *
*.alert                      |program_name
mark.*                       /dev/console
```
> **说明**
>   - **第一列**为`日志类型`和`日志优先级`的组合，每个*类型*和*优先级的组合*称为一个`选择器`；
>   - **后面一列**为保存`日志的文件`、`服务器`，或输出日志的`终端`

- 对配置文件的几点说明：
   - `日志类型`和`优先级`由点号(`.`)分开，
     > **例如** `kern.debug` 表示由内核产生的调试信息。
   - `kern.debug` 的优先级大于 `debug`。
   - 星号(`*`)表示所有，例如 `*.debug` 表示所有类型的调试信息，`kern.* `表示由内核产生的所有消息。
   - 可以使用逗号(`,`)分隔多个`日志类型`，使用分号(`;`)分隔`多个选择器`

- 对日志的操作包括：
   - **将日志输出到文件**，例如 `/var/log/maillog` 或 `/dev/console`。
   - **将消息发送给用户，多个用户用逗号(`,`)分隔**，例如 `root`, `amrood`。
   - **通过管道将消息发送给用户程序，注意程序要放在管道符(`|`)后面。**
   - **将消息发送给其他主机上的 `syslog` 进程，这时 `/etc/syslog.conf` 文件后面一列为以`@`开头的主机名** ,例如`@see.xidian.edu.cn`。

## logger 命令
- `logger` 是`Shell`命令，
   - 可以通过该命令使用 `syslog` 的系统日志模块，
   - 还可以从命令行直接向系统日志文件写入一行信息。

- `logger`命令的语法
```
logger [-i] [-f filename] [-p priority] [-t tag] [message...]
```
- 选项


| 选项 |	说明 |
|:-----|:-----|
| -f filename |	将 `filename` 文件的内容作为日志。 |
| -i |	每行都记录 `logger` 进程的`ID`。 |
| -p priority |	指定`优先级`；`优先级`必须是形如 `facility.priority` 的完整的选择器，默认优先级为 `user.notice`。 |
| -t tag |	使用指定的标签标记每一个记录行。 |
| message |	要**写入的日志内容**，多条日志以空格为分隔；如果没有指定日志内容，并且 `-f filename` 选项为空，那么会把标准输入作为日志内容。 |

- 例如，将`ping`命令的结果写入日志：

```
$ ping 192.168.0.1 | logger -it logger_test -p local3.notice&
$ tail -f /var/log/userlog
Oct 6 12:48:43 kevein logger_test[22484]: PING 192.168.0.1 (192.168.0.1) 56(84) bytes of data.
Oct 6 12:48:43 kevein logger_test[22484]: 64 bytes from 192.168.0.1: icmp_seq=1 ttl=253 time=49.7 ms
Oct 6 12:48:44 kevein logger_test[22484]: 64 bytes from 192.168.0.1: icmp_seq=2 ttl=253 time=68.4 ms
```
> **Notes**  
> `ping`命令的结果成功输出到 `/var/log/userlog` 文件。
> - `-i`：在每行都记录进程ID；
> -  `-t logger_test`：每行记录都加上`logger_test`这个标签；
> - `-p local3.notice`：设置`日志类型`和`优先级`。

## 日志转储

**日志转储**也叫`日志回卷`或`日志轮转`。
- Linux中的日志通常增长很快，会占用**大量硬盘空间**，需要在日志文件达到指定大小时分开存储。

- `syslog` 只负责接收日志并保存到相应的文件，但**不会**对日志文件进行管理，因此经常会造成*日志文件过大*，尤其是`WEB服务器`，轻易就能超过`1G`，给*检索带来困难*

- **大多数Linux发行版**使用 `logrotate` 或 `newsyslog` 对日志进行管理
    - `logrotate` 程序不但可以压缩日志文件，减少存储空间，还可以将日志发送到指定 `E-mail`，方便管理员及时查看日志

> **例如**  
> 规定邮件日志 `/var/log/maillog` 超过`1G`时转储，每周一次，那么每隔一周 `logrotate` 进程就会检查 `/var/log/maillog` 文件的大小    
> - 如果没有超过*1G*，不进行任何操作。
> - 如果在*1G~2G*之间，就会创建新文件 `/var/log/maillog.1`，并将多出的1G日志转移到该文件，以给 `/var/log/maillog` 文件瘦身。
> - 如果在*2G~3G*之间，会继续创建新文件 `/var/log/maillog.2`，并将 `/var/log/maillog.1` 的内容转移到该文件，将 `/var/log/maillog` 的内容转移到 `/var/log/maillog.1`，以保持 `/var/log/maillog` 文件不超过`1G`。


- `logrotate` 的主要配置文件是 `/etc/logrotate.conf`，
    - `/etc/logrotate.d` 目录是对 `/etc/logrotate.conf` 的补充，或者说为了不使 `/etc/logrotate.conf` 过大而设置

> **Notes**  
> - 建议将 `/etc/logrotate.conf` 作为**默认配置文件**，
> - 第三方程序在 `/etc/logrotate.d` 目录下**自定义配置文件**。    

- `logrotate` 也可以作为命令直接运行来修改配置文件。
