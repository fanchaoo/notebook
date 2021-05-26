1. 关系型数据库，其实就是，在“普通的表格”的基础上，将“表格之间的关系”也存储了起来。


2. 常用数据类型：数字，布尔，字符串，日期。


3. MySQL和MongoDB简单对比

MySQL：数据库-->表-->数据行

MongoDB：数据库-->集合-->文档

MongoDB stores documents in collections. Collections are analogous to tables in relational databases.

4. `distinct`的意义是：消除重复行。所以它控制着它后面的多个字段。


5. select 字段1, 字段2 from 表名 where 条件

select后面的字段，是在决定“查询哪些列”。

where后面的条件，是在决定“查询哪些行”。

6. where后面的“运算符”和“关键字”

* `null`判断：`is null`，`is not null`

* 比较运算符：>, >=, <, <=, =, !=

* 连续范围查询：between 值1 and 值2

* `in`查询：`in (值1, 值2)`，`not in (值1, 值2)`

`not in`查询时，如果这个字段有null值，虽然null确实不在`not in`后面的列表里，但是“字段为null的这一行记录不会被查询出来”。

* 逻辑运算：and, or, not

* 字符串模糊查询：like(`%`匹配多个字符，`_`匹配单个字符)

7. 聚合函数

* count

`count(*)`，统计行数；

`count(1)`：统计行数；

`count(列名)`，统计行数；

`count(distinct 列名1, 列名2)`，统计去重之后的行数。


* sum

`sum(列名)`，求和(忽略null值)，要求该列必须是数字类型。


* avg

`avg(列名)`，求平均值(忽略null值)，要求该列必须是数字类型。


* max

`max(列名)`，求该列最大值。

* min

`min(列名)`，求该列最小值。


8. 分组查询（group by ... having ...）

* 语法

`select 列1, 列2, 聚合函数 from 表名 group by 列1, 列2`

* 非分组字段，最好不要出现在`select`后面，因为没有意义(如果非要写在select后面，默认显示该组第一行的值)。

* 如果select后面没有聚合函数，甚至有“非分组字段”，则默认显示该组第一行的记录(一般这样意义也不大)。

* 分组后筛选(having)

having后跟筛选条件，一般用聚合函数作为条件(也可以用“非分组列”作为条件，但同样没有太大意义，因为此时这个条件只作用于“某组首行记录”)

* having和where的筛选时机不同，面向的数据集不同。where筛选的是分组前的记录，having筛选的是分组后，每组的记录。


9. 排序（order by 列1 asc|desc, 列2 asc|desc）

asc是升序，desc是降序。

如果不写asc或desc，则默认是asc升序。

每个asc或desc只对一个列生效，如果要对多个列排序，每个列后面都要跟上asc或desc。


10. 分页（limit start, count）

start是起始位置，count是查询多少个。

start默认从0开始。


11. SQL关键字

* 编写顺序（`select`和`from`必须有，其它关键字在保证顺序的前提下可以任意组合）

select <属性名>
distinct <属性名>
from <表名>
join <表名> on <条件>
where <条件>
group by <属性名> having <条件>
order by <属性名>
limit <起始数，个数>

where后面的条件，和group by的having后面的条件，不同在于前者是筛选满足条件的元组，后者是筛选满足条件的组。

* 执行顺序

from <表名>
join <表名> on <条件>
where <条件>
group by <属性名> having <条件>
select <属性名>
distinct <属性名>
order by <属性名>
limit <起始数，个数>


12. 约束

“外键”和“表之间的关系”本质是两回事。外键是只一种约束，建外键是为了保证“该字段的值一定会在被引用表的字段里找到”。
你完全可以不建立外键，但表之间的关系完全不会收到丝毫影响。


13. 连接查询

![](https://upload-images.jianshu.io/upload_images/1754553-194a3a8ff948836c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

“匹配”的意思是，`on`后面所使用的字段的某个值，在两个表里都存在。如果一个值在左表里存在，而在右表里不存在，即是“不匹配”。

自关联查询：一个表和自己做连接查询，物理上是一张表，逻辑上是多张表。


16. Python操作MySQL

* 概念

编程语言操作数据库，核心其实就几个步骤：

建立连接，执行语句（接收SQL语句和参数），返回结果（将“数据库行”转换为“编程语言中的对象或普通变量”），关闭连接。

这四个步骤其实都是固定的，唯一变动的其实就是上层传过来的“SQL语句”和“参数”。

大多数的ORM框架其实也就是封装了这几个步骤而已，让我们不再一次次写这些重复代码，目的就是减少我们和数据库交互的精力，让我们更关注业务逻辑。

因为我们关心的其实就是两点，`写好SQL给数据库`，`从数据库获取想要的结果`。

至于连接的建立和释放，编程语言的库如何让数据库执行SQL,以及如何将结果映射为对象或普通变量，这些与业务无关的事情，都交给封装好的代码（ORM框架，MySQLdb包）去做了。


* API

核心对象：Connection，Cursor

核心方法：connect，cursor，execute，commit，fetchall，close

















having  和 select distinct 谁先执行？？？

隔离性，两个账户同时向另一个账户转账？？？

锁和事务的关系？？？

编程语言连接数据库时，所用的Connection对象，以及在命令行连接数据库，本质是什么？？？TCP连接？？？













