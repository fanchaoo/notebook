


## 2. Spring的AOP

### 2.1. AOP

AOP全称是Aspect Oriented Programming，翻译过来就是“面向切面编程”。

AOP只不过是种“编程思想”，并不是Spring的专利，意图是“拦截某个方法，在其执行过程中的某些点（执行前，执行后，抛异常后），可以添加一些自定义操作”。只要是有这种“拦截器”思想或意图的，都可以看做是AOP。Servlet的过滤器，SpringMVC的拦截器，MyBatis的Interceptor，Python的装饰器，其实都可以理解为AOP。


在我们的代码里，一般都会有“业务模块”和“非业务模块”。非业务模块可以是事务管理，日志记录，性能统计，权限控制等等。业务模块和非业务模块的关注点完全不同，它们之间应该是正交的关系。我们应该尽量不让那些非业务性代码去破坏业务代码的纯粹性。

Spring的AOP，其实就是通过读取程序员设定好的“配置信息”，“将某些非业务模块，织入到某些业务模块上去”。

### 2.2. 一些概念

join point（连接点），就是一个“方法的执行”

pointcut（切点），就是一系列规则，表示要对哪些方法进行逻辑织入，说白了就是“指定要拦截哪些方法”

advice（通知），表示在方法执行中的某个位置，要执行的操作，其实就是拦截器（interceptor）

aspect（切面），等于“切点（pointcut）+通知（advice）”，其实就是表示“对某些方法的执行过程进行拦截，在这些方法执行过程中的某些位置，织入相应的代码”

![](https://upload-images.jianshu.io/upload_images/1754553-ccda6e7a81b63c7f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/1754553-df32a809c4a978b8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![](https://upload-images.jianshu.io/upload_images/1754553-f1ceeb2bf8d4473d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Advisor：
![](https://upload-images.jianshu.io/upload_images/1754553-f6126156ad594c04.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![](https://upload-images.jianshu.io/upload_images/1754553-d5037f42e898f04e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1754553-1216b8bbe9c8edb2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![](https://upload-images.jianshu.io/upload_images/1754553-99936ac80b7977ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 2.3. 动态代理

Spring的AOP，是通过“动态代理”来实现逻辑织入的。

动态代理，其实就是在程序运行的过程中，为“目标类”生成一个代理类，并创建这个代理类的对象。这个代理类，既可能是“和原类具有相同接口的类”，也可能是“原类的子类”。


### 2.4. AOP的工作时机

容器启动时：
可以通过`@EnableAspectJAutoProxy`注解开启AOP。
这个注解通过`AspectJAutoProxyRegistrar`给容器注入了一个`AbstractAutoProxyCreator`自动代理创建器。
而这个创建器，实现了`SmartInstantiationAwareBeanPostProcessor`这个后置处理器接口。
在`AbstractAutoProxyCreator`的`postProcessAfterInstantiation`方法中，会进行切点匹配等工作，最终织入切面，创建代理对象。

方法调用时：
获取拦截器链


## 3. 声明式事务

通过`@EnableTransactionManagement`注解开启声明式事务管理。
该注解通过`TransactionManagementConfigurationSelector`给容器注入了一个`BeanFactoryTransactionAttributeSourceAdvisor`切面。
这个切面，包含一个`TransactionAttributeSource`事务属性源（它里面会有和事务相关的注解解析器）和`TransactionInterceptor`事务拦截器。

## 4. 关于配置


在使用或者学习Spring的时候，我们会遇到到各种各样的“配置项”。但是我们要注意，不要被这些花里胡哨的配置所迷惑。心里要清楚，“我们配置这些内容，最终都是为了什么？”。

任何所谓的配置，不论是“.propertis文件”也好，“XML配置”也好，或者“注解”也好，都只不过是一些“标记”，一些“记号”而已。这些标记只有“被解析”了之后，才会产生某种特定的效果

不同的配置方式，在“质”上基本是相同的，只是形式不太一样而已。
不管是“<bean>标签”还是“@Bean注解”，它们其实都只不过是表达Bean定义的载体而已，实质都是在"为Spring容器提供Bean定义的信息"，最终让容器实例化这个Bean。

我们要明白一个问题，我们每天在xml里配那些标签，到底是在做什么？是为了什么？答案是：“是为了让Spring去解析这些标签”。

Spring的很大一部分代码，都是在“解析我们的配置”，然后去根据这些配置信息去做某些事情。比如，创建Bean，给Bean注入依赖，创建代理对象等等

每个标签有每个标签的作用，spring在解析完某个标签之后，就会在当前的系统中产生一定的效果。比如说，根据某标签创建了一个类，或者说根据某标签为对象设置属性等等。

xml中的标签也好，Java中的注解也好，其实都是一个“标记”。它们本身是不会产生任何作用的。它们只能被动的被Java中的某些类去解析，然后在那些解析配置的类中进行某些逻辑处理，这时候才会真正地产生某些效果，产生某些作用。所以说，这些配置本身并不会产生效果，是那些“解析配置的类”让系统产生了某种效果。

我们在spring配置文件里配置的那些<bean>标签，其实就是为了让spring帮我们把这个bean对象给创建出来。而在<bean>内部配置的那些<property>标签,其实就是为了让spring去给这个bean对象去设置一些属性。只不过现在不是用代码手动设置了，而是让spring读取这些配置信息，通过类型转换(xml里的一切内容都是字符串，而Java是一个强类型的语言，所以spring需要将<property>标签的值解析成对象，整数，布尔值等等)，反射等一系列步骤为我们把对象的属性设置好。

在往大了想一下，“配置，就是为了被解析”这句话难道仅限于Spring里吗？似乎不是。类似Nginx的配置文件，Tomcat的配置文件，MySQL的配置文件，Maven的POM文件等等，这些配置文件里的所有配置项，也都是为了被解析，然后产生某种效果。

而在Python这种语言中，一个`.py`文件就可以当做一个配置文件。在其它`.py`文件里引入这个`.py`配置文件，然后“直接读取”其中的变量内容，这其实也是种“解析”。

甚至，在Java里，可以把某些配置直接写在一个类里，比如一个常量类，里面全是公有常量。在其它类里读取这个常量类中的内容，然后进行处理，其实也算种“解析”。“直接读取”也是种解析。

总之，配置信息就是为了被解析用的。


