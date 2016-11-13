# 过滤器 `filter`

- `过滤器`可以使用一个管道字符（`|`）添加到**表达式**和**指令**中

## 几个应用filter的例子

```javascript
{{ 1234 | number:2 }}
//显示两位小数，结果 1,234.00

{{ 1234.56 | currency:"人民币￥":0}}
//转化为货币后输出(保留0位小数，四舍五入)，结果为
//人民币￥1,234.00

{{ list | json }}
//将对象转化为json文本输出，结果为
//[ { "name": "Harry" }, { "name": "Tom" }, { "name": "Jerry" } ]

<tr ng-repeat="x in list | orderBy:'name'">
//对显示的数据列表按照name进行排序
//结果为显示顺序Harry,Jerry,Tom
```

## AngularJS的常用用法

| Filter名称 |	示例用法 |	说明 |
|:----------|:----------|:------|
| filter |	- |	传入自定义的函数作为过滤器 |
| currency |	currency / currency:"人民币￥":0 |	转化为货币后输出。可选货币单位和保留小数位数。 |
| number |	number / number:2 |	将数字转化为文本，自动加逗号。可选设置小数位数。 |
| date |	data : format : timezone |	将时间转化到对应的格式和时区 |
| json |	json |	将对象转化为Json格式内容输出 |
| lowercase |	lowercase |	将文本转化为小写 |
| uppercase	 | uppercase |	将文本转化为大写 |
| limitTo |	limitTo : limit : begin |	截取array从begin位置开始的limit个元素 |
| orderBy |	orderBy : expression : reverse |	根据expression的条件对list进行排序，reverse可选，设置为true则反过来排 |

## 多个filter同时应用
- AngularJS支持多个`filter` 的使用

```javascript
{{ list | orderBy:'name' | json }}
//对list的内容进行排序后输出成json文本，结果为
//[ { "name": "Harry" }, { "name": "Jerry" }, { "name": "Tom" } ]
```

## 创建自己的过滤器
- 制作一个将文字全部翻转过来的过滤器

1. 定义自定义过滤器方法
```javascript
//app.js
App.filter("reverse", function(){
    return function(text){
        return text.split("").reverse().join("");
    }
});
```
2. 使用
```javascript
<div ng-controller="FirstCtrl">
    <h1>{{data.message | reverse}}</h1>
    <input type="text" ng-model="data.message">
</div>
```
3. 运行效果
![自定义过滤器](https://hairui219.gitbooks.io/learning_angular/content/zh/pic/0410_filter.png)


## 通过filter进行搜索
> 这个搜索功能并**不是非常常用**，因为搜索工作现在一般在服务端完成。
> - 如果数据量非常小（几百行以内），可以考虑使用本功能来筛选结果

```javascript
App.controller("FirstCtrl", function ($scope) {
    $scope.searchText = '';

    $scope.list = [
        {
            name: "Harry"
        },
        {
            name: "Tom"
        },
        {
            name: "Jerry"
        }
    ];
});
<div ng-controller="FirstCtrl">
    <input type="text" ng-model="searchText">
    <table>
        <tr ng-repeat="x in list | filter:searchText">
            <td>{{x.name}}</td>
        </tr>
    </table>
</div>
```

### 一些值得注意的用法

| 用法 |	效果 |
| searchText = "T" |	搜索所有字段 |
| searchText = {name:"T"} |	只搜索name字段包含T的项目 |
| searchText = {name:"T", last:"H"} |	搜索name字段包含T且last字段包含H的项目 |

```javascript
<div ng-controller="FirstCtrl">
    <input type="text" ng-model="searchText.name">
    <input type="text" ng-model="searchText.last">
    <table>
        <tr ng-repeat="x in list | filter:searchText">
            <td>{{x.name}}</td>
            <td>{{x.last}}</td>
        </tr>
    </table>
</div>
```