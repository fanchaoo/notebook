cd /Users/fanchao/software/ZooInspector/build/
java -jar zookeeper-dev-ZooInspector.jar



1、启动Kafka

zkServer.sh start

JMX_PORT=19092 nohup kafka-server-start.sh /usr/local/kafka/config/server.properties &

JMX_PORT=19093 nohup kafka-server-start.sh /usr/local/kafka/config/server.properties1 &

JMX_PORT=19094 nohup kafka-server-start.sh /usr/local/kafka/config/server.properties2 &

2、停止Kafka
kafka-server-stop.sh

3、创建Topic
kafka-topics.sh --zookeeper localhost:2181/kafka --create --topic my-topic --partitions 5 --replication-factor 2

4、 删除Topic

kafka-topics.sh  --delete --zookeeper localhost:2181/kafka  --topic my-topic

5、查看已经创建的Topic信息
kafka-topics.sh --zookeeper localhost:2181/kafka --describe --topic my-topic

6、发送消息
kafka-console-producer.sh --broker-list 172.16.120.151:9092 --topic my-topic

7、接收消息
kafka-console-consumer.sh --bootstrap-server 172.16.120.151:9092 --topic my-topic

8. 查看消费进度
kafka-consumer-groups.sh --bootstrap-server 172.16.120.151:9092 --describe --group my-group


--------------------------

Apache Kafka 是消息引擎系统，也是一个分布式流处理平台（Distributed Streaming Platform）


总之在规划磁盘容量时你需要考虑下面这几个元素：

新增消息数
消息留存时间
平均消息大小
备份数
是否启用压缩

file:///Users/fanchao/Documents/jk-Kafka%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF%E4%B8%8E%E5%AE%9E%E6%88%98%EF%BC%88%E5%AE%8C%E7%BB%93%EF%BC%89/03-Kafka%E7%9A%84%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8%20(3%E8%AE%B2)/06%E4%B8%A8Kafka%E7%BA%BF%E4%B8%8A%E9%9B%86%E7%BE%A4%E9%83%A8%E7%BD%B2%E6%96%B9%E6%A1%88%E6%80%8E%E4%B9%88%E5%81%9A.html

https://www.jianshu.com/p/db9f37bb7f98


Consumer 需要向 Kafka 汇报自己的位移数据，这个汇报过程被称为提交位移（Committing Offsets）。因为 Consumer 能够同时消费多个分区的数据，所以位移的提交实际上是在分区粒度上进行的，即Consumer 需要为分配给它的每个分区提交各自的位移数据。
提交位移主要是为了表征 Consumer 的消费进度，这样当 Consumer 发生故障重启之后，就能够从 Kafka 中读取之前提交的位移值，然后从相应的位移处继续消费，从而避免整个消费过程重来一遍



TCP 连接是在调用 KafkaConsumer.poll 方法时被创建的



Kafka是一个基于“发布和订阅”的消息系统，数据的发送者不会把消息直接发送给接收者，而是将消息进行归类，然后发送到一个broker服务器，然后接收者通过订阅某类消息，以便接收消息

Kafka中的数据单元为消息，可以类比为数据库中的一个“数据行”；消息本身是字节数组格式的，没有特定含义

Kafka中的消息通过“主题”来进行归类，可以类比为数据库中的一张“表”

一个主题可以分为多个分区，每个分区可以位于不同的broker服务器上，主题的分区数只能增加不能减少

Kafka中的消息保存在磁盘上，并且可以通过配置，让消息想保存多久就保存多久





----------------------


---------------------

如何确定一个kafka集群需要多少个broker服务器？
如何确定一个topic需要多少个分区？
如何确定broker服务器的CPU，内存大小，网络带宽，磁盘容量？


isr，怎么理解“保持一定同步”

follower副本什么时候会去从leader副本同步消息，一次通过多少条？

生产者批量发送消息的好处？为什么批量就可以减少网络开销？

生产者异步发送的callback函数，是在哪个线程里执行的？

为什么日志文件要分成多个日志分段文件？方便清理

给定某个topic分区的一个offset，如何找到这一条消息？确定某一个索引文件，通过索引确定消息在分段文件中的位置

为什么要维护一个isr？ack时为了防止永久等待一个“没有同步到消息的follwer副本”

消息可以发送到任意broker吗，还是必须发送到leader所在的broker

消息顺序性和in flight requests

位移提交时，多个消息消费完，只提交最末尾的offset，假如中间有消息失败了怎么办？

消费者处理完逻辑后，但还没有提交offset，此时消费者挂掉了，当消费者重新启动时，怎么避免重复消费之前的消息？

生产者如何保证exactly once？消费者如何保证exactly once？


ZooKeeper 为什么不适用于这种高频的写操作？




