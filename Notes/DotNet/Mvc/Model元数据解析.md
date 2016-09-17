# Model 元数据
- `Model` 总是体现为一个**数据对象**
- `Model元数据`是对数据类型的描述，它为**参数绑定**，**参数验证**，数据对象**在View上的呈现**提供相应的指导信息

## Model元数据层次化结构
- 用于描述`Model元数据`的是一个`ModelMetadata`对象
  - 描述目标数据类型本身的`ModelMetadata`
  - 描述其数据成员的`ModelMataData`
  - 前者是后者的**容器**`Container`
   
```csharp
public class ModelMetadata
{
    public virtual IEnumerable<ModelMetadata> Properties{get;}
}
```

### 与类型相关的只读属性
1. `ModelType`: `Model`自身的数据类型
2. `IsComplexType`: 是否是一个复杂类型
3. `IsNullableValueType`: 可空值类型
4. `Model`属性表示具体的数据对象

### 复杂类型还是简单类型？
- `IsComplexType`
- 是否支持源自字符串的类型转换
  - `基元类型（Primative Type）`和`可空值类型（Nullable Type）`是**简单类型**
  - `自定义数据类型`默认是`复杂类型`

### 模板方法
- 在调用这些方法将制定的数据呈现在`View`中的时候并不对最终呈现的`Html`作具体的控制，
而是**利用默认或者是制定的模板来决定最终呈现在浏览器中的`HTML`**
- 模板名称
  - `ModelMataData`的`TemplateHint`属性表示


### Model 元数据定制
- `Model元数据`决定了数据对象在`View`中的默认呈现方式
#### `UiHintAttribute`

#### HiddenInputAttribute 与 ScaffoldColumnAttribute
