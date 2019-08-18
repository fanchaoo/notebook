


为什么说网络协议很重要？其实协议就是一系列规则，软件和硬件都是依照这些协议规则来运作的，所以说，懂了协议就基本了解了软硬件的运作原理。

网站演变的两个因素：数据量增加，并发量增加。解决方案有：缓存，扩容，消息队列，分布式，分库分表等等。

Servlet是一套规范，它制定了Java中处理Web请求的标准，我们只需要按照标准规定的去实现就可以了。不过还是那句话，规范自己是不能干活的，标准一样也不能自己干活，每种规范都需要有相应的实现。要想使用Servlet，就需要有相应的Servlet容器，比如常见的Tomcat就是一个Servlet容器。

![](https://fanchaoo-notebook.oss-cn-beijing.aliyuncs.com/img/Servlet容器.png)

Servlet容器是用来运行Servlet的，运行Servlet的前提是，要将从客户端接收的HTTP请求报文封装成ServletRequest请求对象，并将ServletResponse对象序列化为HTTP响应报文，并发送至客户端。


Tomcat的两个主要模块：连接器(Connector)和容器(Container)

Socket是操作系统提供给应用程序的一个编程接口，两个不同计算机上的两个应用可以通过Socket接口发送和接受字节流


Tomcat主要的工作，其实是：解析HTTP请求报文和生成HTTP相应报文，负责报文的输入和输出。

如果设置Servlet的load-on-startup属性为一个正数，则在Tomcat启动的时候，会调用该Servlet的init()方法。

在一个Tomcat中，可以部署多个应用，每个应用都会对应着一个ServletContext对象。

每个Servlet都会有一个对应的ServletConfig对象，这个对象保存了该Servlet的一些配置信息，比如初始化参数等等。

Tomcat启动流程：![](https://fanchaoo-notebook.oss-cn-beijing.aliyuncs.com/img/1754553-91145f9a592dcce5.png)

Tomcat由若干个Service组成，每个Service都包括“若干个Connector”和“一个Container”。这个Container有四层，分别是：Engine，Host，Context，Wrapper。


在Tomcat启动过程中，会执行StandardContext的startInternal方法。该方法会先调用Listener的contextInitialized方法，然后创建过滤器Filter，接着会执行配置了load-on-startup的Servlet的init方法。部分代码如下：

```
// Configure and call application event listeners
            if (ok) {
                if (!listenerStart()) {
                    log.error(sm.getString("standardContext.listenerFail"));
                    ok = false;
                }
            }

            // Configure and call application filters
            if (ok) {
                if (!filterStart()) {
                    log.error(sm.getString("standardContext.filterFail"));
                    ok = false;
                }
            }

            // Load and initialize all "load on startup" servlets
            if (ok) {
                if (!loadOnStartup(findChildren())){
                    log.error(sm.getString("standardContext.servletFail"));
                    ok = false;
                }
            }
```































































