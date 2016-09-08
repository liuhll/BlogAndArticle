# struct
- Python没有专门处理字节的数据类型
- `str`既是字符串，又可以表示字节，
   - 字节数组＝`str`

- Python提供了一个`struct模块`来解决`str`和其他二进制数据类型的转换


- `struct`的`pack函数`把任意数据类型变成字符串
```python
>>> import struct
>>> struct.pack('>I', 10240099)
'\x00\x9c@c'
```   
- `pack`的第一个参数是处理指令
  - `>I` : `>`表示字节顺序是`big-endian`，也就是网络序，`I`表示4字节无符号整数

- `unpack`把`str`变成相应的数据类型  
```python
>>> struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
(4042322160, 32896)
```
- `>IH`的说明，后面的`str`依次
   - `I`：4字节无符号整数
   - `H`：2字节无符号整数。
> Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用`struct`就方便   
