1. 虚拟环境搭建

![](http://oy2qbfbi8.bkt.clouddn.com/18-1-25/41245664.jpg)


2. Django的MTV（MVC）


为什么需要T（模版）？

这里的模版其实就是MVC中的视图。

视图，其实就是HTTP报文的响应体，大多时候是HTML格式的文本，也可以是JSON，普通文本，甚至图片，Excel等等。

视图的本质其实就是字符串。的确可以将HTML内容放在字符串中，写在代码里，但这样会让代码充斥大量字符串，会使得阅读困难，维护也不方便。所以才将HTML内容抽取出来，做成模版，便于管理和维护。这其实也是在抽象，在分层，在解耦。









