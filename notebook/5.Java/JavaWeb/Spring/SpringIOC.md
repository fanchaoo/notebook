Spring的IOC
Spring的IOC，具体做了什么？其实就是读取程序员设定好的“配置信息（XML配置，注解配置）”，然后去统一地“创建对象，并装配类之间的依赖关系”。

IOC的思想最核心的地方在于，资源不由使用资源的双方管理，而由不使用资源的第三方管理，这可以实现“资源集中管理”，实现“资源的可配置和易管理”。




为什么会出现AOP？

如果Java没有多态机制，也就不会有动态代理了





编译期增强，和运行时增强，有区别吗？最终不都是启动完服务器之后，代理对象才可用的吗？



想要“通过反射执行一个方法”，需要的元素：Method对象，方法参数，Method所属类的对象。


FactoryBean和BeanFactory是两个完全不同的东西：
FactoryBean是一个工厂Bean，是专门用来创建别的Bean的；
BeanFactory其实就是Spring的IOC容器，里面存储着所有Bean的定义信息和Bean实例。



org.springframework.aop.framework.ReflectiveMethodInvocation


org.springframework.aop.framework.CglibAopProxy.DynamicAdvisedInterceptor






















http://cdt.zaozuo.com/api/order/orderSync?orderId=94421&isOnline=truess

man hier



sudo lsof -i:8000





xml的bean和component的bean，会重复创建吗？

多种注入方式，会重复注入吗？

为啥要有beanDefinition，直接创建对象不行了吗？后续还会用到beadDefinition吗？

asm操作的是字节码文件吗？还是内存中的Class对象？为啥扫描@Component注解会用ASM而不是Java反射，可能是ASM不会把所有没有@Component的类都加载进虚拟机。

开闭原则，“对扩展开放，对修改关闭”，一直不是很理解这句话。比如Spring配置bean的方式，最初是xml配置，到后来是注解配置。
后来为了支持注解配置会增加很多代码，这时候spring另外搞了一套接口去实现，而不是直接剔除原来的xml配置方式。其实看现在，xml的配置已经很少使用了，那那些为了xml配置写的代码，不是垃圾代码吗？


@Autowired原理是啥？默认是根据名称注入？还是根据类型注入？若是根据类型注入的话，那Spring容器中允许相同类型（但名称不同）的多个实例存在吗？


创建beanDefinition和创建bean，这是两个阶段吧，创建bean的时候，只会创建beanDefinition中有的bean。

给单例类注入非单例类，给非单例类注入单例类，会怎样？

Spring支持循环依赖吗？
@Autowire基础类型，会怎样？

很多注解，value都是默认“属性”，这个怎么做的？

@Configuration被@Component修饰之后，它也是一个组件，原理？

@Controller，默认调用空构造器创建吧？

各种配置，创建bean，最终调用的都是哪个构造器？setter，constructor？

让spring创建bean，有很多种配置方式，这些配置的区别在哪里？应用场景分别是什么？

Spring中非单例bean，有应用场景吗？

为了创建一个bean，制定了多种配置方式，比如注解，xml等，最终是报错还是覆盖？居然会覆盖？好恶心啊。


IoC的核心是“Java反射机制”，AOP的核心是“动态代理”。要好好体会这两句话。
虽然说IoC的核心是“Java反射机制”，但其实真正的反射相关的代码就那么几行，为了实现IoC，Spring做了大量的抽象，有一个相对比较复杂的类体系去实现IoC的功能，并且实现了一个很方便拓展的bean的生命周期。
AOP的核心是“动态代理”，其实就是运行的时候动态生成代理类。


DefaultListableBeanFactory是怎么getBean的？

InitMethod,必须是无参的吗？

bean的生命周期中，那些销毁方法，有应用场景吗？

FactoryBean可以是多实例的吗？好像不可以。

@Autowired，没有set方法也可以注入，原理？

@Import原理？在注解上标注这个@Import，然后就会生效吗？why？


org.springframework.beans.factory.config.ConfigurableListableBeanFactory#preInstantiateSingletons

Spring容器启动，是单线程还是多线程？

registerSingleton方法和getBean的关系？

================

@EnableAspectJAutoProxy中的@Import是怎么生效的？

BeanPostProcessor也是bean，为什么没有拦截自己的初始化过程？


AbstractBeanFactory中的doGetBean，”if (sharedInstance != null && args == null) {“，不用加锁吗？只有一个线程在创建是吗？


jdk动态代理，cglib动态代理，生成的对象，名字分别是啥？service类。

异常被”异常advice“拦截后，会怎么处理？抛吗？还是被吞了？


如果commit事务的时候，异常了，咋办？

如果一个类，所有方法，被2个切面作用，怎么创建对象？

InstantiationAwareBeanPostProcessor和@Autowired是怎么相互影响的？


==============


理解Spring，分两步：一是容器启动的时候，做了些什么？（创建对象，注入属性，创建代理对象，执行生命周期相关方法）；二是一个HTTP请求过来的时候，是怎么一步一步执行的？


大多数BeanDefinition的注册，都是在`invokeBeanFactoryPostProcessors`方法中进行的。

如果一个bean1，依赖另一个还未创建的bean2（不管是构造器参数注入也好，属性注入也好），则在bean1被调用构造器之后，会先创建bean2（会将bean2的整个生命周期方法走一遍），然后再去继续创建bean1。


===================

1. 自动配置

SpringApplication.run()中的类，可以和main方法当期类不一样吗？

SpringBootApplication的scanBasePackages不写会怎样？

java -jar 的原理？

约定大于配置：比如配置文件的名字，固定为`application.properties`

自动配置：通过@EnableAutoConfiguration注解会导入一系类自动配置的组件；
每项自动配置都只会在特定条件下才会生效，可以通过配置`debug=true`，来查看生效的自动配置。

@EnableConfigurationProperties会导入组件？

@ConditionalOnMissingClass原理？咋判断的？


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

=========

Servlet3

org.springframework.web.SpringServletContainerInitializer

javax.servlet.annotation.HandlesTypes

org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer

org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter

tomcat 到 servlet 再到springmvc，是怎么连起来的？

异步Servlet管用吗？主线程和异步线程的数量和不是固定的吗，不太懂？

对应异步的请求，SpringMVC的拦截器会调用两次preHandle方法。so what？可以通过AsyncListener或AsyncHandlerInterceptor来解决这个问题。

SpringMVC和Spring整合，非要搞个父子容器，真的有必要吗。。。感觉这样徒增了代码实现的复杂性，也增加了使用者配置的复杂性。。。？



曾经有很长的一段时间，我对Spring那一堆XML的配置感到十分头痛。
除了XML头部那一坨坨命名空间之类的东西，还有着各种不同名称的标签，各种不同的属性，一层嵌套着一层。
为了搭一个项目的架子，去网上到处搜各种配置项怎么配置。
其实这还好，关键是费半天劲配好这些标签之后，心里很慌，因为我根本不明白，我在XML里配置这些标签，究竟是在做什么？为什么搭好这个架子之后，我就可以“安心”地写业务了。
后来才慢慢明白，这些标签最终都是会被Spring去解析的，大多数标签不过是让Spring为我们创建一个Bean，或者是让Spring读到这个标签之后去启用某个功能。

所以说，作为一个Java后端工程师，我觉得很有必要了解一下“从Tomcat，到Servlet，再到SpringMVC，再到MyBatis”，这一层一层是怎么串联起来的。
了解了这些细节之后，可能心里会踏实很多。
如果你看着自己用的技术，还是会感觉很不踏实的话，也可以跳出来用一个旁观者的角度来审视下这些技术，看看它们到底是在做什么，是为了解决什么问题。
毕竟，大多数的技术，都是为了解决某些特定的问题出现的。


“单体”应用的缺点：1.不方便分工合作开发






