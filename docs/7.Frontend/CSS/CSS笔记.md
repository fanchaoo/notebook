
# CSS

## 目录

* 选择器
* 属性
	* 样式
		* 字体和文本相关属性
		* 背景相关属性
	* 布局
		* 盒模型，块元素和行内元素，标准文档流
		* 浮动
		* 定位

## 注意

* 分门别类地去记忆属性，要知道属性的**默认值**和**继承性**

* 要知道每个属性都是用来做什么的，随着属性值的不同，要能在脑海里有一个动态的绘制过程，要知道某些属性能用来做哪些常见布局或常见效果

* 数字类型的属性，要考虑属性值能不能是负值

* 综合类的属性，要考虑多个属性值哪些是必填项，有没有顺序要求，比如border: red solid 10px


## 常用属性默认值

width,height,left,right,top.bottom: auto

margin,padding: 0


## 百分比

width,height是相对于父元素的width和height
margin,padding是相对于父元素的width，而不是对应的margin,padding

## 一些概念

CSS规定的并不是属性，而是行为（behavior），DOM里的每个元素都可以看成是一个独立的物体，按照CSS规定的方式运动，最后稳定下来的结果就是最终布局的结果


# 标准流与盒模型

界面上的每个元素，都是一个矩形盒子。整个网页，其实就是盒子套盒子，大盒套小盒。

网页的布局，其实就是摆放一个个矩形盒子，把这些盒子摆放在合适的位置。竖着摆放，默认标准流就行；横着摆放，就用浮动；任意摆放，就用定位。

reset.css：https://meyerweb.com/eric/tools/css/reset/

注意事项：

* 什么时候设置padding，什么时候设置margin

* 什么时候设置父元素的padding，什么时候设置子元素的margin


## border

border可以设为none


## padding

盒子的可见区域 = conent + padding + border

当宽高为非auto时，padding会影响可视区域的大小

背景色会填充到padding里

子元素默认占用父元素的content区域，不占用padding区域

当某元素设置了固定宽度时，添加padding会是元素可见框变大；默认情况下，width为auto，这时候设置padding，会向里挤子元素


## margin

margin是指当前盒子与其它盒子之间的距离（和父盒子，和兄弟盒子）

margin不会影响盒子可视区域的大小（当margin为非负数的时候），但是会影响盒子占地大小，并且会影响自身盒子或其它盒子在界面中的位置

默认设置左边距和上边距，会影响自身盒子的位置；设置右边距和下边距，会影响其他盒子的位置

当margin为负数时，会使自身盒子或其它盒子向反方向移动

可以给左边距和右边距设置margin: auto，auto的意思是能设多大设多大。在标准流中，可以使一个盒子居左，或居右，或居中。给上下margin设置auto没有效果

当盒子间距离大于margin的值时，margin会不起作用

**相邻**兄弟元素之间，垂直方向的margin会重叠，最终会取最大值

在标准流中，如果父子元素的垂直方向外边界重叠了，则子元素的外边距会设置给父元素，可以通过`box.before{content:"";display:table;}`来解决父子边界重叠问题

水平方向的margin不会重叠

当设置了固定宽高时，padding就不能随意设置了，因为会撑开可视框；当宽高为auto时，可以设置padding，让元素自动调整宽高


## 行内元素

行内元素不支持设置宽高（标准流中）

行内元素可以设置左右内边距

行内元素可以设置上下内边距，只不过不会影响其它盒子的位置，而且可能会覆盖其它盒子

行内元素可以设置左右边框

行内元素可以设置上下边框，只不过不会影响其它盒子的位置，而且可能会覆盖其它盒子

行内元素支持左右外边距

行内元素不支持上下外边距


## 标准文档流

块元素：

* 块元素在文档流中会独占一行，自上向下排列
* 块元素在文档流中默认宽度是auto，展示的效果就是占父元素的100%
* 当元素的width为auto时，此时设置padding不会影响可视区域的大小，而是会自动缩减宽度以适应padding
* 块元素在文档流中的高度，默认被内容（即子元素）撑开

行内元素：

* 行内元素在文档流中只占自身大小，自左向右排列，如果一行容不下，则换行展示，继续自左向右排列
* 行内元素在文档流中，宽高默认都被内容撑开
* 行内元素在文档流中，如果书写标签的时候元素之间有换行等空白字符，则会在元素之间产生一个空格
* 可以通过`font-size: 0`来清除行内元素直接的空格


## display属性

inline（默认）：设置为行内元素

block：设置为块级元素

inline-block：设置为行内块元素，既可以设置宽高，又不独占一行

none：隐藏该元素，并且不占据页面位置，但是标签还在页面内


## visibilitys属性

visible（默认）：展示该元素

hidden：隐藏该元素，但是仍然占据界面位置


## overflow

visible（默认）：展示溢出元素

hidden：截断，不展示溢出元素

auto：根据需要自动展示滚动条


## list-style

通过给ul设置`list-style: none`，可以清除列表默认的圆点


## 浏览器默认样式

浏览器会给一些元素加一些默认的margin或padding，一般开发都要先去掉浏览器默认样式

一些表单项（input，textarea）也会有些默认样式（padding，margin，border），一般也要先去掉

文本可以预设字体，字号，行高


# 浮动与盒模型

## float

不继承

none（默认）：不浮动

left：向左浮动

right：向右浮动


## 浮动元素的特性

脱离标准文档流，不再占用原来的位置，即它的位置会被其它元素占用

元素会尽量向左上或右上漂浮，直到遇到父元素content边缘，或其它浮动元素的margin

如果浮动元素上方是一个未浮动的块元素，则浮动元素不会漂浮到上方元素的位置，因为上面的块级元素已经独占了一行

连续的几个兄弟浮动元素，如果一行着不下，则会自动换行

浮动的元素，不会超过它上面浮动的兄弟元素，最多一边齐

浮动的元素，不会遮盖住父元素内或兄弟元素内的文字，文字会自动环绕到浮动元素周围

行内元素脱离文档流后，会变成块元素；脱离文档流后的块元素，宽高会由内容撑开

浮动会提升层级（提升半层），盒模型相关层，文字相关层


## 清除浮动

### clear属性

可以清除其它浮动的兄弟元素对当前元素的影响（即如果其它兄弟元素没有浮动，自己会在什么位置，这个位置就是清除浮动之后自己所在的位置）

none（默认值）：不清除

left：清除左侧浮动元素对自己的影响

right：清除右侧浮动元素对自己的影响

both：清除两侧对自己影响最大的元素对自己的影响

### 清除浮动方式

1.给父级加高度
	扩展性不好

2.开启BFC
	overflow:hidden
	定位
	浮动
	
	ie 6 7底下不支持BFC
	
3.br标签
	ie6 不支持
	违反了结构 行为 样式相分离的原则
	
4.空标签
	违反了结构 行为 样式相分离的原则
		ie6下元素的最小高度为19px
			可以尝试给元素的fontsize设为0---> 2px

5.伪元素 + 开启haslayout
	因为ie6 7 下不支持伪元素  
	所以要额外的去开启haslayout


## BFC

BFC全称Block Formatting Context，块格式化上下文，是元素的一个隐藏属性

元素开启BFC后的特点：

* 当前元素的外边距不会和子元素重叠（即子元素设置margin，自己不会跟着动）
* 当前元素不会被浮动元素覆盖
* 当期元素可以包含浮动的元素

如何开启BFC：

* 设置元素浮动（会导致宽度丢失，即不再是父元素的100%了，并导致下面元素上移）
* 设置元素绝对定位
* 设置元素为inline-block（导致宽度丢失）
* 设置overflow为非visible值，比如hidden，audo


## 高度塌陷

子元素脱离文档流后，便无法撑起父元素，可能会导致父元素的高度塌陷

如何解决高度塌陷：

* 通过给元素开启BFC，可以解决高度塌陷的问题
* 可以在元素内部末尾，加一个`clear: both`的空白div，通过清除浮动来撑开父元素
* 可以通过伪元素选择器`:after`清除浮动来撑开父元素
```
.clearfix:after{
	content: "";
	display: block;
	clear: both;
}
```

高度塌陷问题解决后，父元素的高度即为被子元素撑开的高度，而不是0


## 解决父子边界重叠和清除浮动

```
.clearfix:before,
.clearfix:after{
	content: "";
	display: table;
	clear: both;
}
```

## PS

修改单位为像素：![](https://fanchaoo-notebook.oss-cn-beijing.aliyuncs.com/img/WX20190811-220213@2x.png)

查看矩形选框详情：快捷键F8


# 定位与盒模型

## position属性

通过定位可以将元素摆放在页面的任意位置

position属性默认不继承，有以下可选项：

* static（默认值）：未开启定位

* relative：开启相对定位

* absolute：开启绝对定位

* fixed：开启固定定位

position属性需要配合top，bottom，left，right属性使用


## 相对定位

* 当某元素开启相对定位后，如果不设置偏移量，则元素位置不会发生变化

* 相对定位，是指的相对于元素原来的位置（原来可能是在标准流中，也可能是浮动了），进行定位

* 开启相对定位的元素，不会脱离标准流，不会改变元素是块元素还是行内元素的性质

* 相对定位会使元素层级提高，可能会覆盖其它层级低的元素（相对定位提升一层，浮动提升半层）


## 绝对定位

* 当元素开启绝对定位后，如果不设置偏移量，则位置不会发生变化

* 绝对定位的元素，会脱离标准流；行内元素脱标后，会变成块元素；脱标后的块元素，宽高会由内容撑开

* 绝对定位的元素，会提高自己的层级，所以可能会覆盖其它层级低的元素

* 绝对定位，是以“离它最近的一个开启了定位（relative，absolute，fixed都可以）的祖先元素”为基准，开始定位

* 绝对定位，默认是以浏览器视窗口为基准定位，而不是以body和html为基准

* 绝对定位是相对于某祖先元素的“边框内边界”开始定位的，而浮动是相对于父元素content的内边界开始定位的


## 固定定位

固定定位也是一种绝对定位，区别在于：

* 固定定位的元素，永远相对于浏览器窗口定位

* 固定定位的元素，会固定在浏览器窗口某个位置，不会随滚动条滚动


## z-index（层级）

* z-index属性不继承

* 通过z-index属性，可以给**开启定位的元素**设置一个层级（正整数），值越大，层级越高

* 开启定位元素，在没有设置z-index的情况下，位置越往下，层级越高

* 父元素z-index再高，也不会盖住子元素


## opacity（不透明度）

* opacity取值范围为0-1，0表示完全透明，1表示完全不透明


# 字体和文本

## 如何出现...省略号

前提：宽度不能是被内容撑开的

```
.box{
	width: 100px;
	display: block;
	white-space: nowrap;
	text-overflow: ellipsis;
	overflow: hidden;
}
```
## 行高的继承

如果父元素line-heigth为百分比，则子元素继承下来的是父元素的font-size * 父元素的line-height

如果父元素line-heigth为正数因子，则子元素会继承下来line-height，然后再根据自己的font-size进行计算最终行高



# 背景

背景相关的属性，都不继承：![](https://fanchaoo-notebook.oss-cn-beijing.aliyuncs.com/img/20190818174501.png)

## background-color

默认值是transparent（透明的）

## background-image

* 背景图片，默认以“图片原始大小”，从元素的左上角（padding外边缘）开始repeat绘制，向外截止到border外边缘

* 背景图片和背景色可以同时设置，背景图片会在背景色上面展示

* 背景图片可以设置为**渐变**，比如线性渐变（linear-gradient）或径向渐变（radial-gradient）

## background-repeat

用于设置背景图片的重复性

可选项：

* repeat（默认值）：自左向右，自上向下重复

* no-repeat：不重复

* repeat-x：仅水平方向重复

* repeat-y：仅垂直方向重复


## background-position

设置背景图片的起始位置

https://www.w3school.com.cn/cssref/pr_background-position.asp

背景图片的位置可以设置为负值，常用于雪碧图背景图片（雪碧图只适用于背景图片，不适用于img标签）


## background-attachment

设置背景图像是否固定或者随着页面的其余部分滚动

* scroll（默认值）：背景图像会随着页面其余部分的滚动而移动。
* fixed：当页面的其余部分滚动时，背景图像不会移动。

当设置为fixed时，background-position是相对于浏览器窗口定位的，常用语body的固定大背景图

## background-size

设置背景图片的大小，通过像素或百分比（相对于盒子宽高）

`background-size: 100%`表示宽度100%，高度auto

`background-size: 100% 100%`表示宽高都为100%，可能会压缩图片大小

## background-origin

规定背景图片的定位区域：padding-box，border-box，content-box

## background-clip

规定背景的绘制区域：border-box，padding-box，content-box

## background

可以将所有背景相关属性简写为一个：`background: blue url(a.jpg) top left no-repeat fixed`

background的属性值，没有顺序要求，没有数量要求，不写的样式就是用默认值




# 实战

## 常用布局

![image.png](https://upload-images.jianshu.io/upload_images/1754553-b6645171d6f3addb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 圣杯布局

浮动，相对定位，margin为负值

* 伪等高布局

不设高度，padding-bottom正值，margin-bottom负值，相互抵消

margin只影响盒子边界，不影响盒子位置（不同于left，top）

## 禁止系统滚动条

```
html,body{
	height: 100%;
	overflow: hidden;
}
```



# CSS3

## text-shadow

默认值：none，不继承

文本阴影，可以设置阴影偏移的的xy坐标，阴影颜色，模糊程度

## box-shadow

默认值：none，不继承

盒子阴影，可以设置阴影偏移的xy坐标，阴影颜色，模糊程度，阴影大小，内阴影或外阴影

## resize

默认值：none，不继承

可以通过设置resize，使盒子可以被缩放

## box-sizing

默认值：content-box，不继承

当设置为border-box时，添加padding会向盒子内部挤内容


## border-radius

默认值：0，不继承

圆角边框，可以用来画圆或椭圆；

可以制作圆形头像：

```
.box{
	height: 200px;
	width: 200px;
	border-radius: 50%;
	background-image: url(wb.jpeg);
	background-repeat: no-repeat;
	background-size: 200px;
}
```





























