1、关于模块

* 模块搜索路径

```
>>> import sys
>>> sys.path
['', 'C:\\Windows\\SYSTEM32\\python27.zip', 'C:\\Python\\python\\DLLs', 'C:\\Python\\python\\lib', 'C:\\Python\\python\\lib\\plat-win', 'C:\\Python\\python\\lib\\lib-tk', 'C:\\Python
\\python', 'C:\\Python\\python\\lib\\site-packages', 'C:\\Python\\python\\lib\\site-packages\\tornado-4.3-py2.7-win32.egg', 'C:\\Python\\python\\lib\\site-packages\\backports_abc-0.5
-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\certifi-2017.4.17-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\singledispatch-3.4.0.3-py2.7.egg', 'C:\\Python\\python\\l
ib\\site-packages\\backports.ssl_match_hostname-3.5.0.1-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\six-1.10.0-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\jinja2-2.
8-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\markupsafe-1.0-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\xlwt-1.0.0-py2.7.egg', 'C:\\Python\\python\\lib\\site-packa
ges\\xlrd-0.9.4-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\mysql_connector_python_rf-2.1.3-py2.7-win32.egg', 'C:\\Python\\python\\lib\\site-packages\\peewee-2.8.1-py2.7.egg
', 'C:\\Python\\python\\lib\\site-packages\\requests-2.10.0-py2.7.egg', 'C:\\Python\\python\\lib\\site-packages\\futures-3.0.5-py2.7.egg']
```

* 重新导入模块

当某模块内容被修改时，若要是新代码生效，需要重新导入：
```
import imp
imp.reload(some_module)
```

* 设计模块时要防止出现“循环导入”



2、"=="和"is"

* "=="比较的是"内容"是否相同，"is"比较的是引用(即地址)是否相同。

```
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False
```
```
>>> num = 10000
>>> num == 10000
True
>>> num is 10000
False
```
```
>>> a = "123"
>>> b = "123"
>>> a == b
True
>>> a is b
True
```

* 整数在[x， y]的特殊性

只有在变量赋值给变量时(或某些特殊情况)，才是赋值引用：

```
>>> a = 1000
>>> b = 1000
>>> a == b
True
>>> a is b
False
```
```
>>> a = 300
>>> b = 300
>>> a == b
True
>>> a is b
False
```

3、浅拷贝和深拷贝

* 浅拷贝就是简单的引用赋值

```
>>> a = [1, 2, 3]
>>> b = a
>>> id(a)
46449968
>>> id(b)
46449968
```

* 深拷贝(一直递归)

```
import copy
>>> import copy
>>> a = [1, 2, 3]
>>> b = copy.deepcopy(a)
>>> id(a)
46470248
>>> id(b)
46470488
>>> b
[1, 2, 3]
```

* 单层拷贝

```
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = [a, b]
>>> import copy
>>> d = copy.copy(c)
>>> c
[[1, 2], [3, 4]]
>>> d
[[1, 2], [3, 4]]
>>> a.append(3)
>>> c
[[1, 2, 3], [3, 4]]
>>> d
[[1, 2, 3], [3, 4]]
```
```
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = [a, b]
>>> import copy
>>> d = copy.deepcopy(c)
>>> c
[[1, 2], [3, 4]]
>>> d
[[1, 2], [3, 4]]
>>> a.append(3)
>>> c
[[1, 2, 3], [3, 4]]
>>> d
[[1, 2], [3, 4]]
```

如果是不可变类型，则直接拷贝引用：

```
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = (a, b)
>>> import copy
>>> d = copy.copy(c)
>>> id(c)
44832688
>>> id(d)
44832688
```



4、进程和线程

* 并发和并行

进程数大于CPU核数，就是并发。
进程数小于等于CPU核数，就是并行。


* 父进程和子进程，全局变量不共享，各自有自己的数据，代码相同，但数据不共享。
```
import os
import time

g_num = 100

ret = os.fork()
if ret == 0:
    print("----process-1----")
    g_num += 1
    print("---process-1 g_num=%d---"%g_num)
else:
    time.sleep(3)
    print("----process-2----")
    print("---process-2 g_num=%d---"%g_num)
```


* 进程通信

因为进程间，变量（数据）不共享，所以进程间需要通信。

整个计算机网络，其实就是无数进程在通信。
比如我的QQ进程和你的QQ进程，
我登百度，其实就是我的浏览器进程，和百度服务器进程在通信。


* 创建进程的方式

fork，Process类，Pool类（进程池）。


* 线程

每个进程都会有一个主线程，线程是CPU的调度单位。

因为多个线程都在同一个进程里，所以线程间共享进程内的全局变量。

多个线程对共享变量进行修改时，可能出现数据被覆盖的情况，所以需要加锁；若每个线程均是仅仅访问变量，则不需要加锁；


同步，就是协同步调，使程序按预定的次序进行执行。

异步，就是当某条件满足时，去执行程序，但不确定何时执行。

同步，异步，指的是执行顺序却不确定；阻塞，非阻塞，指的是等待还是不等待。


* 网络

协议，就是为了相互通信，而建立的一种规则，一种数据格式，根据这个格式，就可以进行有效的通信。

端口，是用来标记一台机器上的进程的，不用pid是因为，pid是一个电脑上比较私有的东西，并且可能会变化，而通信常常需要一个，
（已知&&不会变化）的标识，去标记一个进程，所以就有了端口号。

Socket，是用来在多个计算机的进程之间，进行通信用的。


（IP，端口号，协议），可以确定你要和另一台计算机上的哪个进程进行通信。


广播，只能在UDP协议上使用


* TCP

服务器初始化步骤：bind, listen, accept

TCP套接字的接收和发送用`recv`和`send`，UDP套接字用`recvfrom`和`sendto`。
（因为TCP已经建立了连接，知道目的地址和来源地址，而UDP则是每次接收和发送数据报的时候都要带上地址）


* 路由器

网络号相同的多个计算机可以直接通信（或借助交换机通信）；
网络号不同的两台主机不能直接通信（TCP/IP协议规定的？？？），需要借助路由器。

路由器可以连接不同网段


不同网段的两个终端通信时，在通信过程中，IP协议中的源IP和目的IP始终不变，但MAC地址在途经的每个设备（即路由器）中都会改变。

IP：标记逻辑上的地址；
MAC：标记设备的物理地址（两设备间手拉手传数据用的）；
netmask：用来求网络号的（和IP按位与）；
默认网关：发送数据的IP不在同一个网段内时，回把数据转发给默认网关。


DNS服务器其实就相当于一个电话簿（根据人名找手机号），根据域名找IP地址。


HTTP只是规定了一种数据传输的格式，一次网页的请求，其实是浏览器将请求数据按照HTTP协议要求的格式封装好，
然后通过socket建立TCP连接，在三次握手之后，将数据发送到服务器，最后四次挥手，关闭连接。
在TCP三次握手的过程中，第三步时，会附带上客户端的真正请求数据。
在TCP的四次挥手的过程中，当客户端收到数据时，会在发送给服务器的“确认包”中发送挥手的第一步的数据。




TTL（time to live）：与数据包在网络上经过的路由器的个数有关；
2MSL（Maximum Segment Lifetime）：
TCP最后一次挥手后，为了确保服务器收到了客户端的ACK，所以等待2MSL（在2MSL内没有收到失败反馈，说明ACK成功发送过去了）


TCP半连接攻击（ddos）：
只发送syn，在收到(ack+syn)后，不回复ack，这样会占用服务器的tcp连接队列，
导致服务器大量tcp连接资源被占用，以至于无法正常为普通用户提供服务。



* 服务器

Python多进程的"Copy On Write"：
子进程并不会完全复制父进程的变量，只有当父进程中的变量修改时，操作系统才会复制一份给子进程，
若父进程变量始终没有改变，则子进程会使用同一变量。


为什么要有多进程或多线程服务器？
因为要同时为多个客户端提供服务呀。


用非阻塞的socket，通过`while True`轮训多个套接字，也可以实现单进程内同时对多个请求客户端服务。


select：通过轮训多个文件描述符，实现单进程并发（最多1024个文件描述符）
poll：与select机制相同，但是轮训没有数量限制。
epoll：通过事件通知机制，不用轮训，获得待处理的文件描述符列表。


Python的协程是通过生成器（yield）实现的，通过切换函数实现任务配合，相对于切换线程和切换进程，代价要小很多。
同时，协程的任务切换是由开发者自己控制的，而线程或进程的切换是由操作系统控制的。















