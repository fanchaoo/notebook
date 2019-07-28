
![image.png](https://upload-images.jianshu.io/upload_images/1754553-c73b32cba0f9ea8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1754553-c3dee1e82799dc7a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


-getmerge，合并顺序？

java客户端连hdfs，不需要密码？

mp的map阶段，以block分隔，把有意义的连续数据断开了咋办？

内存镜像，直接序列化有啥坏处吗？


TextInputFormat，全是空格的行会算吗？

自定义WritableComparable，如果compareTo返回0，会怎么处理？


如果不设置reduce，map会怎么输出？

context.nextKeyValue和nextKeyValue.nextKeyValue

maptask和reducetask，代码层面是怎么调用的？

执行到一半的mr任务，节点坏了咋办？会有类似事务的机制吗？

HDFS的HA，故障之后，zk是如何通知的？


-----------------------------------------------------------------

数据量基数大，数据量增长速度快，数据种类多样化，数据分析与处理困难


Hadoop主要是为了解决海量数据的存储和海量数据的计算的问题。


HDFS是一个分布式文件系统。适用于写入次数少，读出次数多，并且只支持追加写入的场景。一般用于数据分析。


MapReduce步骤：Mapper，Reducer，Driver。

对象序列化：实现Writable接口

InputFormat




















































