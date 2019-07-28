### 1. 问题

向下兼容，到底好不好？

JCP?

JSR？

HTTP接口，返回多于的字段好不好？

对于框架中的数据库操作来说，连接的获取和关闭，Statement的创建，这些都在哪里被做了？

Servlet上下文？到底是啥？

expert one to one j2ee design and development

expert one to one j2ee development without ejb

SpringBoot那一堆starter，是怎么组织的？

Maven的scope为“import”，type为“pom”，啥意思？dependencyManagement标签，啥意思？

看下类加载源码？

JVM 安全管理器？

Spring和SpringMVC的父子容器，是怎么绑定起来的？又是怎么和ServletContext绑定起来的？

ContextLoaderListener是为了创建“WebApplicationContext”还是“ApplicationContext”？

关于bean的id和name是怎么解析和处理的？报错？忽略重复只留一个？

Java反射，拿不到方法的参数名？

@Bean所修饰的方法，参数注入是属于属性注入吧？

@Autowired修饰字段，和修饰方法，反射调用分别是Field合Method吧？

“父bean”是什么鬼？是“继承”吗？

FactoryBean的getObject()，只能对单例bean处理吧？如果是的话，这个方法应该只在容器启动的时候，仅被调用一次吧？

@Autowired，为“List属性”注入所有匹配到的Bean：如果容器里有一个List类型的Bean呢？要怎么注入？

@Configuraion被@Component修饰了，那么@Configuration就拥有@Component的功能了吗？不是吧？应该有地方去解析这些信息吧？

method.invoke()的源码？

Proxy.newProxyInstance的源码？

cglib动态代理，原理？

### 2. 笔记

Tomcat --> Servlet --> SpringMVC --> Spring --> MyBatis --> MySQL

有了Spring，我们可以不必再为编写单例类，属性文件解析等这些底层的需求编写代码，可以更专注于上层的应用。

Spring的好处，好好体会，![](https://upload-images.jianshu.io/upload_images/1754553-473a0d4a6f854685.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Spring框架的五大模块：![](https://upload-images.jianshu.io/upload_images/1754553-e518bb158a6a6011.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Spring的IoC功能，将类与类之间的依赖从代码中脱离出来，用“配置的方式”进行依赖关系描述，由IoC容器负责依赖类之间的创建，获取等工作。

传统的JDBC流程：![](https://upload-images.jianshu.io/upload_images/1754553-4972917a83dc381a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Listener（监听器），顾名思义，就是可以监听某些事件，当这些事件发生的时候，会执行一些提前定义好的操作。
比如实现了`ServletContextListener`的`ContextLoaderListener`，就可以在Servlet上下文初始化的时候，创建Spring容器。































