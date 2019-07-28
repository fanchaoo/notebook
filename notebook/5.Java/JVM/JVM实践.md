# 1.参数类型

参数类型有**boolean型参数**和**key value型参数**。

-Xss1024K：设置每个线程的栈容量为1024K。等于`-XX:ThreadStackSize`。

-Xms10M：设置堆的初始容量为10M。等于`-XX:InitialHeapSize`。
-Xmx10M：设置堆的最大容量为10M。等于`-XX:MaxHeapSize`。
-Xmn5M：设置新生代的容量为5M

-XX:PretenureSizeThreshhold：设置晋升老年代容量
-XX:NewSize
-XX:MaxNewSize
-XX:NewRitio
-XX:SurvivorRatio：设置Eden区和Survivor区的比例


-XX:MetaspaceSize=10M：设置metaspace的初始容量为10M
-XX:MaxMetaspaceize=10M：设置metaspace的最大容量为10M

-XX:MaxDirectMemorySize=10M：设置直接内存的最大容量为10M



# 2.查看JVM参数

查看当前的JVM参数：`java -XX:+PrintFlagsFinal -version | less`

列出所有JVM进程：`jps -l`

查看进程123的最大堆内存：`jinfo -flag MaxHeapSize 123`

查看进程123的非默认参数：`jinfo -flags 123`

查看垃圾回收器：`jinfo -flag UseConcMarkSweepGC 123`，`jinfo -flag UseParallelGC 123`，`jinfo -flag UseG1GC 123`

查看类加载信息：`jstat -class 123`

每隔1000毫秒输出一次GC信息，共输出5次：`jstat -gc 123 1000 5`。![image.png](https://upload-images.jianshu.io/upload_images/1754553-28cb7706a4112d5a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

堆大小怎么设置：

![](https://www.dutycode.com/content/uploadfile/201711/296d1509689688.png)


# 3.内存

通过jmap导出内存映像，然后用MAT分析内存溢出原因。

`-XX:+HeapDumpOnOutOfMemoryError，-XX:HeapDumpPath=./`：内存溢出时，自动导出内存映像文件

`jmap -dump:format=b,file=filename 123`：导出内存映像文件

`jmap -heap 123`：输出堆内存信息

`jmap -histo:live <pid>`： 打印每个class的实例数目,内存占用,类全名信息.live子参数加上后,只统计活的对象数量. 此时会触发FullGC

用MAT看下，通过Histogram查看些对象数量最多，通过dominator_tree查看哪些对象占用内存最多，查看某个对象的GCRoots。


# 4.线程

通过jstack定位*CPU利用率飙升*和*线程死锁*。

`jstack 123`：输出线程信息

`top -p 123 -H`：显示线程占用CPU，内存等等

`printf "%x" 123`：将10进制转为16进制


# 5.btrace

# 6.psi-probe


# 7.GC 

## 垃圾收集器(3类，7个)

串行收集器：

并行收集器：

并发收集器：

开启CMS：`-XX:+UseConcMarkSweepGC -XX:+UseParNewGC`

开启G1：`-XX:UseG1GC`



## 日志分析

GCeasy

## 性能指标

停顿时间（最小，最大，平均）
吞吐量
GC次数
GC发生的原因


# 8.字节码

查看字节码：`javap -verbose Test1.class`





******************************************

tar -zxvf jdk-8u141-linux-x64.tar.gz -C /usr/local/

nohup

sz 命令

setenforce 0


第一章
无
第二章
jdk8工具集
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/index.html
Troubleshooting
https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/
jps
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jps.html
jinfo
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jinfo.html
jstat
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html
jmap：
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jmap.html
mat:
http://www.eclipse.org/mat/downloads.php
jstack：
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstack.html
java线程的状态
https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/tooldescr034.html
java线程状态转化：
https://mp.weixin.qq.com/s/GsxeFM7QWuR--Kbpb7At2w
死循环导致CPU负载高
https://blog.csdn.net/goldenfish1919/article/details/8755378
正则表达式导致死循环：
https://blog.csdn.net/goldenfish1919/article/details/49123787
第三章
jvisualVM：
https://docs.oracle.com/javase/8/docs/technotes/guides/visualvm/index.html
https://visualvm.github.io/documentation.html
jvisulaVM如何添加插件
https://visualvm.github.io/index.html
第四章
btrace下载
https://github.com/btraceio/btrace
https://github.com/btraceio/btrace/releases/tag/v1.3.11
第五章
jdwp协议：
https://www.ibm.com/developerworks/cn/java/j-lo-jpda3/
tomcat-manager：
{tomcat}/webapps/docs/manager-howto.html
psi-probe:
https://github.com/psi-probe/psi-probe
tomcat优化相关参数：
${tomcat}/webapps/docs/config/http.html
${tomcat}/webapps/docs/config/host.html
${tomcat}/webapps/docs/config/context.html
${tomcat}/webapps/docs/connectors.html
apr连接器：
http://apr.apache.org/
第六章
nginx官网文档
http://nginx.org/en/docs/
nginx安装：
http://nginx.org/en/linux_packages.html
ngx_http_stub_status：
http://nginx.org/en/docs/http/ngx_http_stub_status_module.html
ngxtop：
https://github.com/lebinh/ngxtop
nginx-rdd
http://www.linuxde.net/2012/04/9537.html
第七章
jvm的运行时数据区
https://docs.oracle.com/javase/specs/jvms/se8/html/index.html
Metaspace
http://ifeve.com/jvm-troubleshooting-guide-4/
压缩类空间
https://blog.csdn.net/jijijijwwi111/article/details/51564271
CodeCache
https://blog.csdn.net/yandaonan/article/details/50844806
http://engineering.indeedblog.com/blog/2016/09/job-search-web-app-java-8-migration/
GC调优指南：
https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/toc.html
如何选择垃圾收集器
https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/collectors.html
G1最佳实践
https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/g1_gc_tuning.html#recommendations
G1 GC的一些关键技术
https://zhuanlan.zhihu.com/p/22591838
CMS日志格式
https://blogs.oracle.com/poonam/understanding-cms-gc-logs
G1日志格式
https://blogs.oracle.com/poonam/understanding-g1-gc-logs
GC日志分析工具
http://gceasy.io/   
GCViewer
https://github.com/chewiebug/GCViewer
ZGC：
http://openjdk.java.net/jeps/333
第八章
java虚拟机规范
https://docs.oracle.com/javase/specs/jvms/se8/html/index.html
java语言规范
https://docs.oracle.com/javase/specs/jls/se8/html/index.html
javap：
https://docs.oracle.com/javase/8/docs/technotes/tools/unix/javap.html
字段描述符
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.3.2
方法描述符
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.3.3
字节码指令：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-6.html
常量池：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.4
本地变量表：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html#jvms-2.6.1
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.7.13
操作数栈：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html#jvms-2.6.2
Code属性：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.7.3
LineNumberTable：
https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-4.html#jvms-4.7.12
constant variable：
https://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.12.4
常量表达式
https://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.28
String.intern
https://blog.csdn.net/goldenfish1919/article/details/80410349
String去重
https://blog.csdn.net/goldenfish1919/article/details/20233263
































