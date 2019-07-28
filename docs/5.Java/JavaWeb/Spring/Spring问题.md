org.springframework.web.context.WebApplicationContext.ROOT
org.springframework.web.servlet.FrameworkServlet.CONTEXT.spring


服务器生成sessionid的算法是什么？？？同一个浏览器窗口，登录—>注销->再登录，sessionid一样吗？？？


为什么springmvc返回纯文本或者说json，会这么复杂？要配置那么多东西？它和普通视图到底是怎么个关系？为什么python返回纯文本或json这么简单？？？

spring aop织入的时期是什么时候？？？

给bean织入多个切面的时候，有顺序吗？

jdk动态代理，生成的代理对象，和原对象toString相同，hashCode相同，equals不同，"=="也不同，为什么？？？



容器初始化时，
initPropertySources是干嘛用的？？？
XmlWebApplicationContext的Evironment属性是啥时候实例化的？？？
ApplicationContextInitializer是干嘛用的？？？



JVM --> 服务器 --> Spring容器，各种变量是怎么连起来的，哪个“容器”里？？？
“单例对象”在哪个容器里唯一？？？被Spring管理的单例对象和普通的单例对象，存储的地方一样吗？？？
单例对象与类加载器的关系？？？


在web.xml里可以传一个“配置类”吗？如何不默认用xmlWebApplicationContext？？？

想要使用@Autowired，前提必须打开<context:component-scan>吗？内部细节是怎样的？？

为什么要把很多单例对象，例如service,mapper等，用spring容器管理起来？？？直接所有方法和属性都用静态的，不能达到同样效果吗？？？

在项目里，有哪些类的对象是spring容器管理的？？？有哪些不是？？？为什么那些类的对象不需要容器管理？？？

为什么属性一定要用“Autowired”注入？？？不写这个注解，直接使用不行吗？？？“注入”的过程到底做了什么？？？

一个HTTP请求，到达dispatcherServlet之后，是如何一步一步找到各个controller，service,mapper，并执行它们的方法的？？？

setter注入的过程是怎样的？？？

构造器注入，发生循环依赖（死锁）时，细节是怎样的？？？

<import>，导入配置文件的原理，重复导入会怎样？？？

@Service和@Autowired不同时使用，会报错吗？？？

springmvc容器是如何把spring容器当作父容器的？？？

“请求转发”的过程，具体做了什么？？？

springmvc参数绑定，可以绑定int之类的原生类型吗？？？都可以绑定哪些类型的参数（对象，基本类型包装类，String）？？？

视图渲染的过程？？？Model里的东西是怎么绑到request域里的？？？


ServletContext servletContext = request.getServletContext();
		XmlWebApplicationContext spring = (XmlWebApplicationContext) servletContext.getAttribute("org.springframework.web.context.WebApplicationContext.ROOT");
		XmlWebApplicationContext springmvc = (XmlWebApplicationContext) servletContext.getAttribute("org.springframework.web.servlet.FrameworkServlet.CONTEXT.spring");
		DefaultListableBeanFactory beanFactory = (DefaultListableBeanFactory) springmvc.getBeanFactory();
		
		ApplicationContext parent1 = spring.getParent();
		ApplicationContext parent2 = springmvc.getParent();
		String[] names = beanFactory.getSingletonNames();
		for(String name : names){
			System.out.println(name);
			System.out.println(beanFactory.getSingleton(name));
			System.out.println();
		}


通过Spring提供的IOC容器，我们可以将对象之间的依赖关系交由Spring进行控制，避免硬编码所造成的过度耦合。有了Spring，用户不必再为单实例模式类、属性文件解析等这些很底层的需求编写代码，可以更专注于上层的应用。

“注入”，其实就是将某个对象的引用“赋值”给某变量而已。注入的过程就是一个简单的变量赋值的过程。

IOC容器，其实只做了一件事，就是“管理bean的生命周期”。其中包括“bean的实例化”和“bean之间的依赖关系的绑定”。
所有各种复杂的配置，本质其实都是为了“给容器提供bean定义信息”，好让容器去“实例化bean”和“注入bean”。

AOP：大量重复性的,通用的，模板代码，非核心的业务代码


所有的Web层的框架，不论是什么语言，核心问题就是：“将一个请求，与一个处理方法对应起来。当这个请求到来时，便执行这个处理方法最后返回响应”。

Servlet只是一套标准，一套接口，真正很多的细节都是有服务器（Tomcat等）做的，比如将请求报文解析，并封装为一个请求对象，将一个响应对象，序列化为响应报文等等。


当服务器在响应报文中，加入“Set-Cookie”之后，浏览器会将这个Cookie存在本地。之后的每次请求，浏览器会“自动”在请求报文头部，带上这个Cookie。Cookie是基于域名相互隔离的，不同的域名之间不能相互访问Cookie。










ThreadLocal类型的属性，其引用在堆内存，是怎么做到其内的值和线程绑定的？？？

```
	static ThreadLocal<Integer> t = new ThreadLocal<Integer>();

	public static void main(String[] args) {
		new Thread(new Runnable() {

			public void run() {
				t.set(1);
				System.out.println(t);
				System.out.println(t.get());
			}
		}).start();
		new Thread(new Runnable() {

			public void run() {
				System.out.println(t);
				System.out.println(t.get());
			}
		}).start();

	}
```
```
java.lang.ThreadLocal@194e1cdc
java.lang.ThreadLocal@194e1cdc
1
null
```





























