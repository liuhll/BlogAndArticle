# Shell数组：shell数组的定义、数组长度

- `bash`支持**一维数组**（*不支持多维数组*），并且*没有限定数组的大小*
- 数组元素的`下标`(`索引`)由`0`开始编号
- 取数组中的元素要利用`下标`，`下标`可以是**整数**或**算术表达式**，其值应**大于或等于`0`**

## 定义数组

用`圆括号` `()`来表示数组，数组元素用`空格`符号分割开

- 语法
   1. 第一种
        ```bash
        array_name=(value0 value1 value2 value3)
        ```
   2. 第二种 
   ```bash
        array_name=(
        value0
        value1
        value2
        value3
        )
   ```
   3. 单独定义数组的各个分量
  
    ```bash
        array_name[0]=value0
        array_name[1]=value1
        array_name[2]=value2
        array_name[10]=value10
    ```

    > **Notes**
    > - 可以**不使用连续的下标**，而且`下标`的范围**没有限制** 

## 读取数组

- 读取`数组元素值`的一般格式

    ```bash
    value_n=${array_name[2]}
    ``` 

- 使用`@` 或 `*` 可以获取数组中的**所有元素**
    ```bash
    ${array_name[*]}
    ${array_name[@]}
    ```


- [数组例子](../Shell.Demo/array.demo.sh)    

## 获取数组的长度

- *获取数组长度的方法*与*获取字符串长度*的方法**相同**

```bash
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}
```
