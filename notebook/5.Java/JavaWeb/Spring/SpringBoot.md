
1. 自动配置

如果说Spring的核心的IOC和AOP，那么SpringBoot的核心则是Condition + AutoConfiguration（自动化配置）。

SpringApplication.run()中的类，可以和main方法当期类不一样吗？

SpringBootApplication的scanBasePackages不写会怎样？

java -jar 的原理？

约定大于配置：比如配置文件的名字，固定为`application.properties`

自动配置：通过@EnableAutoConfiguration注解会导入一系类自动配置的组件；
每项自动配置都只会在特定条件下才会生效，可以通过配置`debug=true`，来查看生效的自动配置。

@EnableConfigurationProperties会导入组件？

@ConditionalOnMissingClass原理？咋判断的？



​SpringBoot启动时，会通过`EnableAutoConfiguration`注解，然后去所有类路径下搜索`META-INF/spring.factories`文件，加载大量的自动配置类。

​这些自动配置类（一般命名为xxxAutoConfigurartion），会根据某些特定的条件，在容器中装配某些Bean。

这些自动配置类，通常有一个标注了`@ConfigurationProperties`的`xxxProperties`类，这个类封装了一些属性，这些属性就是我们可以在.properties文件中可以配置的内容。




2. 日志适配

SpringBoot的日志统一适配（SLF4J+Logback）：通过排除原来的日志jar包，然后引入新的“-over-”包来实现。

3. 静态资源

有几个默认目录

webjar

4. Theamleaf

语法，th:，${}

5. SpringMVC

WebMvcAutoConfiguration

WebMvcConfigurerAdapter

Formatter和Converter区别？

HiddenHttpMethodFilter，处理put，delete请求

HttpMessageConverter

http request的header里，accept有多个，会怎么处理？RequestMapping的produces？

6. 异常处理

ErrorMvcAutoConfiguration

BasicErrorController

DefaultErrorAttributes

7. 嵌入的Servlet容器

EmbeddedServletContainer

EmbeddedServletContainerAutoConfiguration

EmbeddedServletContainerCustomizer

EmbeddedServletContainerCustomizerBeanPostProcessor

ServerProperties

容器启动过程，容器定制原理



外置Servlet容器配置

注册Servlet三大组件：ServletRegistrationBean

DispatcherServletAutoConfiguration

标有@Configuration的类里，套@Configuration的类，咋解析的？


8. 数据访问

整合Druid，3步：具体原理是？？？
* 在数据源Bean上标注@ConfigurationProperties注解，用于属性解析；
* 创建一个StatViewServlet
* 创建一个WebStatFilter

TODO
整合MyBatis

* 配置数据源DataSource
* @MapperScan指定要扫描的mapper接口所在的包

MybatisAutoConfiguration

可以通过`ConfigurationCustomizer`自定义配置项

可以通过在一个接口上标注`@Mapper`注解，让MyBatis为这个接口创建一个实现类（代理类）

可以通过在一个配置类上标注`MapperScan`注解，让MyBatis为某些包下的接口创建实现类（代理类）

mapperLocation和@MapperScan，有关系吗？


SqlSessionFactory需要数据源，TransactionManager也需要数据源，两者之间有什么联系吗？


9. SpringBoot启动过程

几个拓展点：

ApplicationContextInitializer（须在META-INF/spring.factories中配置）

SpringApplicationRunListener（须在META-INF/spring.factories中配置）

ApplicationRunner（需要配置成Bean）

CommandLineRunner（需要配置成Bean）


10. 自定义starter

@ConfigurationProperties

@EnableConfigurationProperties

@Configuration

@ConditionalOnXXX


11. 关于Docker

在容器中运行的程序，和在普通进程中，性能会有差别吗？

docker kill掉的容器不会删除吗。。默认容器位置在哪里？怎么删？

怎么对容器进行配置？

可不可以配置国内的镜像仓库？

两个重要概念：镜像和容器


12. 缓存

CacheAutoConfiguration

SimpleCacheConfiguration，HashMap线程不安全体现在哪里？和ConcurrentHashMap有啥区别？和Hashtable有啥区别？
为啥在ConcurrentMapCacheManager的getCache方法里还要对cacheMap加锁？

ConcurrentMapCacheManager

ConcurrentMapCache

CacheAspectSupport

@CachePut，更新的同时，有人访问，访问到了旧缓存，咋办？

@Caching，cacheable和put同时作用时，何时会查数据库，何时不会？


@CacheConfig，抽取缓存的公共配置

docker-cn


RedisCacheConfiguration

RedisCacheManager

RedisTemplate序列化机制

RedisAutoConfiguration

如何改变RedisTemplate的序列化规则？


13. 消息队列

消息队列和线程池的应用场景分别是？


像RabbitMQ，Jenkins，它们的后台管理系统，数据持久化在哪里？

@RabbitListener原理是啥？



14. 其它

异步处理，失败了怎么补救？能保证事务吗？

dubbo，调用者必须保存一份被调用者的接口备份吗？这样被调用者的接口变更的时候，岂不是每个调用者都要改？

spring-boot-actuator

















