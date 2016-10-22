# Shell文件包含
- 像其他语言一样，`Shell` 也可以**包含外部脚本**，将外部脚本的内容合并到当前脚本

- `Shell` 中包含脚本可以使用

```bash
. filename
```
> 或者

```bash
source filename
```

> **Notes** 
> - 两种方式的**效果相同**，简单起见，一般使用点号(`.`)，但是注意点号(`.`)和文件名中间**有一空格**

- Demo
   - [main.sh](../Shell.Demo/main.sh)
   - [subscript.sh](../Shell.Demo/subscript.sh)

- 执行脚本   
```bash
$chomd +x main.sh
./main.sh
http://see.xidian.edu.cn/cpp/view/2738.html
$
```
> **Notes**
> - 被包含脚本**不需要有执行权限**
