# Python 自动补全

## vim python自动补全插件：`pydiction`

- 可以实现下面python代码的自动补全：
  1. 简单python关键词补全
  2. python 函数补全带括号
  3. python 模块补全
  4. python 模块内函数，变量补全
  5. from module import sub-module 补全

- [pydiction插件地址](https://github.com/rkulla/pydiction)  

### 安装配置

```bash
$ wget https://github.com/rkulla/pydiction/archive/master.zip
$ unzip -q master
$ mv pydiction-master pydiction
$ mkdir -p ~/.vim/tools/pydiction
$ cp -r pydiction/after ~/.vim
$ cp pydiction/complete-dict ~/.vim/tools/pydiction
```

- 文件结构为
```bash
$ tree ~/.vim
/root/.vim
├── after
│   └── ftplugin
│       └── python_pydiction.vim
└── tools
    └── pydiction
        └── complete-dict
```

- 修改`~/.vimrc`,增加如下内容
```bash
filetype plugin on
let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'
```

- 用`vim`编辑一个`py`文件,`import os`,这时候应该出现提示,证明成功
   ![vim配置成功](https://blog.linuxeye.com/wp-content/uploads/2013/05/python_vim.jpg)

## python交互模式下Tab自动补齐
- 创建`~/.pythonstartup`文件如下

```python
#!/usr/bin/env python
import sys
import readline
import rlcompleter
import atexit
import os
# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
 
del os, histfile, readline, rlcompleter
```

- 重新登陆`shell`，输入`python`命令进入交互模式，就可以用`Tab键`进行补全   
