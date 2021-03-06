

# RabbitMQ

消息队列和RPC调用最大的区别在于，消息队列提供了一种异步通信的方式，生产者只需要将消息发送给消息队列即可，而无需等待消费者消费完成后再返回结果。而RPC框架则是同步调用，消费者调用生产者的服务，必须等生产者返回结果后再继续执行接下来的程序。

RabbitMQ是由Erlang语言实现的一个基于AMQP协议的消息队列中间件。

![image.png](https://upload-images.jianshu.io/upload_images/1754553-885991486df42158.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


AMQP 说到底还是一个通信协议，通信协议都会涉及报文交互，从 low-level 举例来说， AMQP 本身是应用层的协议，其填充于 TCP 协议 层的数据部分。而从 high-level 来说， AMQP 是通过协议命令进行交互的。 AMQP 协议可以看作一系列结构化命令的集合，这里的命令代表 一种操作，类似于HTTP中的方法 (GET、 POST、 PUT、 DELETE等)。


# 基本概念

通过Connection可以为每个线程创建一个信道Channel；
通过信道Channel，可以创建一个交换机，创建一个队列，然后通过绑定键将交换机和队列绑定起来；
然后生产者可以指定一个交换机和路由键，去生产消息，并发送给Broker服务器；
交换机会通过路由键去匹配绑定键，将消息转发给相应的队列；
最终消费者可以从某个队列中消费消息。

生产者和交换机打交道，消费者和队列打交道。

## 基本概念

连接（Connection），信道（Channel）
交换机（Exchange），路由键（RoutingKey），绑定键（BindingKey），队列（Queue）

在创建好交换机和队列之后，可以为它们之间建立一个或多个绑定关系（可以类比数据库的一个多对多关系的中间表）。

之后在一条消息到达交换机之后，会根据路由键，去和它关联的所有的绑定关系里去匹配，然后找出匹配的队列，将消息转发进去。

一个交换机可以和一个队列建立多个绑定。

topic类型的交换机，在路由时如果通过路由键，找到多个绑定同时指向一个队列，那这个队列也只会收到一条消息。

## 交换机：

类型：direct，fanout，topic

是否持久化：即是否存盘，如果存盘，则服务器重启时数据还在

是否自动删除：当所有其它交换机或队列，都和自己解绑后，删除该交换机

是否内置：生产者不能发送消息给内置交换机，只能通过其它交换机转发到内置交换机


## 队列

是否持久化：即是否存盘，如果存盘，则服务器重启时数据还在

是否自动删除：当所有消费者，都和自己断开连接后，删除该队列

是否排他：排他队列只对声明自己的连接可见，并且连接断开后自动删除；其它连接也不能声明和该队列同名的队列



可以给队列设置过期时间`x-expires`，如果在过期时间内该队列没有被使用过，则过期时间到达时该队列会被删除。在 RabbitMQ 重启后 ， 持久化的队列的过期时间会被重新计算。

也可以给队列中的消息设置TTL过期时间，可以在声明队列时通过参数`x-message-ttl`统一设置，也可以在生产者发布消息时单独设置属性`expiration`，最终的过期时间会去两者中的最小值。

在声明队列时统一设置过期时间的消息，在指定时间之后就会被删除；而单独设置过期时间的消息，只有当有消费者消费该队列中的消息的时候，才会判断消息是否过期，若过期则删除消息。

## DLX（Dead Letter Exchange，死信队列）

DLX其实是一个交换机。

可以在声明队列的时候，通过参数`x-dead-letter-exchange`为该队列设置一个DLX死信队列。

消息变成死信的几种情况：

* 消息被消费者拒绝（reject或nack），并设置requeue为false
* 消息过期(声明队列时统一设置，发布消息时单独设置，过期后都会到DLX中去)
* 队列达到最大长度


## 优先级队列

可以在声明队列时设置一个`x-rnax-priority`参数，使队列成为一个优先级队列。

然后在发布消息的时候，可以为消息设置一个`priority`属性。

这样在队列中有消息堆积的时候，会优先消费优先级高的消息。

## 延迟队列

可以通过DLX和消息的TTL，来模拟出延迟队列的功能。

# 消费者

## 消费模式

在RabbitMQ中，消费者有推和拉两种消费模式。

“推”是指Broker向消费者发送队列中的消息。

“拉”是指消费者主动向Broker获取队列中的消息。

## ACK

当消费者收到消息之后，需要向Broker返回一个ACK，当Broker收到ACK后，会将消息打上删除标记，之后会从队列中删除。

消费者可以选择自动ACK或者手动ACK。

## Reject和Nack

当消费者收到消息之后，也可以告诉Broker拒绝消费某条消息。同时可以通过参数requeue来指示Broker是否要将消息删除。

## QOS（只用于推模式）

channel.basicQos 方法允许限制信道上的消费者所能保持的最大 未确认消息的数量。
举例说明，在订阅消费队列之前，消费端程序调用了 channel.basicQos(5) ，之后订 阅了某个队列进行消费。 RabbitMQ会保存一个消费者的列表，每发送一条消息都会为对应的消 费者计数，如果达到了所设定的上限，那么 RabbitMQ 就不会向这个消费者再发送任何消息。 直到消费者确认了某条消息之后 ，RabbitMQ将相应的计数减1，之后消费者可以继续接收消息， 直到再次到达计数上限。这种机制可以类比于 TCP/IP中的"滑动窗口"。


# 生产者

## mandatory和AltemateExchange

当Broker根据交换机和路由键没有找到相应的队列时：

如果生产者发布消息时设置了mandatory为false，如果在声明交换机的时候设置了备份交换机则消息会进入备份交换机去匹配，否则此时Broker会直接丢弃掉这条消息。

如果生产者发布消息时设置了mandatory为true，则可以通过在生产者端添加一个ReturnListener监听器，这时候Broker会将没有匹配到队列的消息返回给生产者。

## Confirm机制

Confirm机制是为了保证生产者发送的消息已正确的到达Broker。

生产者将信道设置成 confmn C确认)模式，一旦信道进入 confmn 模式，所有在该信道上 面发布的消息都会被指派 一个唯一的 IDC从 l 开始)，一旦消息被投递到所有匹配的队列之后， RabbitMQ 就会发送一个确认 CBasic.Ack) 给生产者(包含消息的唯一 ID)，这就使得生产 者知晓消息已经正确到达了目的地了。


# 可靠投递

持久化：交换机持久化（声明时设置durable），队列持久化（声明时设置durable），消息持久化（发布消息时设置投递模式deliveryMode为2）

生产者方面：备份交换机，mandatory+ReturnListener，生产者异步Confirm，事务

消费者方面：手动ACK

DLX死信队列

镜像队列：master节点挂掉会自动切换到slave节点

# 重复消费和消息顺序

只能通过外部引入 GUID (Globally Unique Identifier)的方式，来解决消息重复消费和消息顺序问题。

********************************************************************

（生产者or消费者）一直没收到ACK，会怎样？

重新推送给消费者，不会引起重复消费吗？

消费端限流，消息堆积在哪里？限流，限制的是哪里？

集群之间，不需要”权限认证“之类的东西吗？

qos?


关于消费者ACK，假如消费者业务处理完了，然后在ACK之前挂掉了，这导致Broker中的消息没有删除，之后会重新消费，咋办？同理生产者Confirm之前，Broker的ACK没发过来咋办？

multiple?


生产者“拉”模式，用ACK吗？



推模式，消费者应该也监听了一个端口吧？


























