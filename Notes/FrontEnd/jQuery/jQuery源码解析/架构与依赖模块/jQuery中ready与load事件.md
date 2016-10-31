# jQuery文档加载事件

- `jQuery`有`3`种针对文档加载的方法

```javascript
$(document).ready(function() {
    // ...代码...
})
//document ready 简写
$(function() {
    // ...代码...
})
$(document).load(function() {
    // ...代码...
})
```

## `ready`和`load`的区别
- `ready`与`load`谁先执行?
   - `ready`先执行，`load`后执行

- `DOM`文档加载的步骤
    1. 解析HTML结构。
    2. 加载外部脚本和样式表文件。
    3. 解析并执行脚本代码。
    4. 构造HTML DOM模型。//ready
    5. 加载图片等外部文件。
    6. 页面加载完毕。//load   

> **总结**
> - `ready`与`load`的区别就在于**资源文件的加载**，`ready`构建了基本的`DOM`结构，所以对于代码来说应该越快加载越好。    
>     - 我们**应该越早处理DOM越好**，我们不需要等到图片资源都加载后才去处理框架的加载，图片资源过多`load事件`就会迟迟不会触发

- `jQuery`是处理文档加载时机

```javascript
jQuery.ready.promise = function( obj ) {
    if ( !readyList ) {
        readyList = jQuery.Deferred();
        if ( document.readyState === "complete" ) {
            // Handle it asynchronously to allow scripts the opportunity to delay ready
            setTimeout( jQuery.ready );
        } else {
            document.addEventListener( "DOMContentLoaded", completed, false );
            window.addEventListener( "load", completed, false );
        }
    }
    return readyList.promise( obj );
};
```

> **jQuery兼容的具体策略**
> - 针对高级的浏览器，很乐意用`DOMContentLoaded事件`了，省时省力

- 旧的IE如何处理呢？

```javascript
// Ensure firing before onload, maybe late but safe also for iframes
document.attachEvent( "onreadystatechange", completed );
// A fallback to window.onload, that will always work
window.attachEvent( "onload", completed );
// If IE and not a frame
// continually check to see if the document is ready
var top = false;
try {
    top = window.frameElement == null && document.documentElement;
} catch(e) {}
if ( top && top.doScroll ) {
    (function doScrollCheck() {
        if ( !jQuery.isReady ) {
            try {
                // Use the trick by Diego Perini
                // http://javascript.nwbox.com/IEContentLoaded/
                top.doScroll("left");
            } catch(e) {
                return setTimeout( doScrollCheck, 50 );
            }
            // detach all dom ready events
            detach();

            // and execute any waiting functions
            jQuery.ready();
        }
    })();
}
```

> **Notes**
> - 如果浏览器存在`document.onreadystatechange` 事件，当该事件触发时，如果 `document.readyState=complete` 的时候，可视为 `DOM` 树已经载入
> - 总的来说当页面 `DOM` 未加载完成时，调用 `doScroll` 方法时，会产生异常。那么我们反过来用，如果不异常，那么就是页面**DOM加载完毕**了 