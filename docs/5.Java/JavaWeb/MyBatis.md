### 1. JDBC步骤

* 编写SQL
* 预编译
* 设置参数
* 执行SQL
* 封装结果

Hibernate是框架自动生成SQL，MyBatis可以手动写SQL。

到底是join查询好，还是代码里分步查询好？

### 2. 入门

根据一个配置文件中的信息，创建一个SqlSessionFactory。

调用SqlSessionFactory的openSession()方法，获取一个SqlSession。openSession默认“不自动commit”。

给SqlSession的selectXXX()方法，传入SQL标签的id和参数，可以用于执行SQL。

mapper的XML和接口，是通过<mapper>接口的namespace属性，来进行绑定的。

SqlSession是非线程安全的。

要明白“mybatis-config.xml”这个全局配置文件是做什么用的。其实这些配置都是为了创建SqlSessionFactory而做准备的。

SqlSessionFactory --> SqlSession --> Mapper

mybatis是如何判断resultType是别名还是全类名的？基本类型（int,long等）怎么处理的？

mybatis本身是如何管理事务的？

扫描一个包内的mapper接口，是怎么实现的？

sqlSession的getMapper()方法，是如何根据mapper.xml创建代理对象的？

啥时候用Integer，啥时候用int？

### 3. mapper

useGeneratedKeys和keyProperty的原理：Statement接口有一个getGeneratedKeys()方法。

如果通过@Param传多个参数给mapper接口的insert方法，如何得到自增主键？


### 4. 接口参数处理


单个参数：基本类型及其包装类，String，普通对象；Map；List，Set，数组。

多个参数：@Param注解。

单个参数的时候，#{啥都行？}？

多个参数的时候，可以一个Map，一个对象，一个int吗？


MapperProxy

MapperMethod

ParamNameResolver，用于解析出参数名。

配置useActualParamName


`#`和`$`的区别：`#`是从参数中取值，然后设置给预编译好的SQL。`$`是直接将参数值，拼接在SQL中。
关于SQL注入：
select * from depot_warehouse
where name like '%' or 1 = 1 or '%'


org.apache.ibatis.type.JdbcType

org.apache.ibatis.session.Configuration


### 5. 返回结果处理

### resultType

#### 返回类型

返回单个值：基本类型及其包装类，String，普通对象

返回Map：属性名-->属性值；主键-->对象（@MapKey）

返回数组或List

#### 如何处理映射关系

起别名，配置mapUnderscoreToCamelCase


### resultMap

resultMap可以自定义如何将“数据库的列名”和“Java对象的属性名”对应起来。

association标签中，column属性不能和外层相同吗？

association标签中，通过select属性进行分步查询，有局限性吧？

<association>

<collection>

分步查询

延迟加载


### 6. 动态SQL


<if>, <where>, <trim>, <set>

<choose>, <when>, <otherwise>

<foreach>

<bind>

<sql>, <include>

<cache>

内置对象`_parameter`


一个事务里，批量插入和代码里循环插入，哪个效率高？

JDBC有个allowMultiQueries选项


### 7. 缓存

一个会话中：首次查user1，先看二级缓存，再看一级缓存；之后再查user1，怎么查缓存？？？

mybatis对联表查询的缓存，是怎么做的？


	 * 两级缓存：
	 * 一级缓存：（本地缓存）：sqlSession级别的缓存。一级缓存是一直开启的；SqlSession级别的一个Map
	 * 		与数据库同一次会话期间查询到的数据会放在本地缓存中。
	 * 		以后如果需要获取相同的数据，直接从缓存中拿，没必要再去查询数据库；
	 * 
	 * 		一级缓存失效情况（没有使用到当前一级缓存的情况，效果就是，还需要再向数据库发出查询）：
	 * 		1、sqlSession不同。
	 * 		2、sqlSession相同，查询条件不同.(当前一级缓存中还没有这个数据)
	 * 		3、sqlSession相同，两次查询之间执行了增删改操作(这次增删改可能对当前数据有影响)
	 * 		4、sqlSession相同，手动清除了一级缓存（缓存清空）
	 * 
	 * 二级缓存：（全局缓存）：基于namespace级别的缓存：一个namespace对应一个二级缓存：
	 * 		工作机制：
	 * 		1、一个会话，查询一条数据，这个数据就会被放在当前会话的一级缓存中；
	 * 		2、如果会话关闭；一级缓存中的数据会被保存到二级缓存中；新的会话查询信息，就可以参照二级缓存中的内容；
	 * 		3、sqlSession===EmployeeMapper==>Employee
	 * 						DepartmentMapper===>Department
	 * 			不同namespace查出的数据会放在自己对应的缓存中（map）
	 * 			效果：数据会从二级缓存中获取
	 * 				查出的数据都会被默认先放在一级缓存中。
	 * 				只有会话提交或者关闭以后，一级缓存中的数据才会转移到二级缓存中
	 * 		使用：
	 * 			1）、开启全局二级缓存配置：<setting name="cacheEnabled" value="true"/>
	 * 			2）、去mapper.xml中配置使用二级缓存：
	 * 				<cache></cache>
	 * 			3）、我们的POJO需要实现序列化接口
	 * 	
	 * 和缓存有关的设置/属性：
	 * 			1）、cacheEnabled=true：false：关闭缓存（二级缓存关闭）(一级缓存一直可用的)
	 * 			2）、每个select标签都有useCache="true"：
	 * 					false：不使用缓存（一级缓存依然使用，二级缓存不使用）
	 * 			3）、【每个增删改标签的：flushCache="true"：（一级二级都会清除）】
	 * 					增删改执行完成后就会清楚缓存；
	 * 					测试：flushCache="true"：一级缓存就清空了；二级也会被清除；
	 * 					查询标签：flushCache="false"：
	 * 						如果flushCache=true;每次查询之后都会清空缓存；缓存是没有被使用的；
	 * 			4）、sqlSession.clearCache();只是清楚当前session的一级缓存；
	 * 			5）、localCacheScope：本地缓存作用域：（一级缓存SESSION）；当前会话的所有数据保存在会话缓存中；
	 * 								STATEMENT：可以禁用一级缓存；		
	 * 				
	 *第三方缓存整合：
	 *		1）、导入第三方缓存包即可；
	 *		2）、导入与第三方缓存整合的适配包；官方有；
	 *		3）、mapper.xml中使用自定义缓存
	 *		<cache type="org.mybatis.caches.ehcache.EhcacheCache"></cache>
	 *
	 *
	

### 8. 整合Spring


Spring是如何找到SqlSessionFactory，然后拿到mapper去执行的？

SqlSession和Mapper是什么关系？

Spring事务管理，是如何管理SqlSession和Mapper的？

SqlSessionTemplate



### 9. 原理

大脑不要懒，要多思考。所有注解上的信息，和配置文件里的信息，都是需要解析的，最终这些信息都会在代码里起某种作用，或被设置到对象的属性值里。

### 创建SqlSessionFactory

解析总配置文件和所有mapper配置文件，将这些配置信息设置到Configuration对象里。然后根据这个Configuration对象创建一个DefaultSqlSessionFactory。

```
public class DefaultSqlSessionFactory implements SqlSessionFactory {

  private final Configuration configuration;

```

Configuration类的mappedStatements属性，存储了“sqlId --> sql标签对象”的映射关系。

Configuration类的mapperRegistry属性，存储了“mapper的Class --> 代理对象的工厂类”之间的映射关系。

### 创建SqlSession（new）

调用SqlSessionFactory的openSession()方法，然后调用openSessionFromDataSource()方法，最终创建一个经InterceptorChain拦截过的DefaultSqlSession，它里面包含Configuration和Executor。

```
public class DefaultSqlSession implements SqlSession {

  private final Configuration configuration;
  private final Executor executor;

```

### 创建Mapper代理对象（new）

调用SqlSession的getMapper()方法，然后调用Configuration对象中的mapperRegistry的getMapper()方法，这个方法会以Mapper的Class为键值，找到相应的MapperProxyFactory。

然后调用MapperProxyFactory的newInstance()创建一个MapperProxy代理对象（通过JDK的动态代理，MapperProxy实现了InvocationHandler接口）。

这个MapperProxy代理对象里包含DefaultSqlSession（Executor），可以用于执行SQL。


### 执行Mapper方法

首先进入MapperProxy的invoke()方法，在这个方法里创建一个MapperMethod对象。

然后调用MapperMethod的execute()方法，接着调用selectList()方法，在这个方法里，根据Mapper方法的唯一id，从Configuration的mappedStatements属性中，得到对应的MappedStatement对象。

然后根据MappedStatement等信息，执行Executor的query()方法。

接下来会创建一个StatementHandler用于创建PreparedStatement执行SQL语句，同时需要用ParameterHandler处理参数，并通过ResultSetHandler处理执行结果。

参数处理和结果处理，都需要TypeHandler来执行。

四大组件：Executor，StatementHandler，ParameterHandler，ResultSetHandler

![image.png](https://upload-images.jianshu.io/upload_images/1754553-44c72b1458ee570e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/1754553-4641b462cf281a3f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


MyBatis的插件，其实就是Interceptor。

ExecutorType

TypeHandler

SqlSource

MapperBuilderAssistant

MappedStatement


代理对象里的“h”是啥？为啥调select()方法，直接就到invoke()里了？

那种带<foreach>标签的，解析完的sql长啥样？

啥时候用int，啥时候用Integer？


### 10. generator

### 11. 通用Mapper

怎么做连接查询？


MyBatis Generator代码生成的原理是啥？

要从“比较宏观的角度”去想下，某个技术是在解决什么问题？实现的大概思路是怎样的？
比如MyBatis Generator，是为了减少人工去写一些通用的mapper方法。实现的思路大致是“通过配置信息，读取数据库中的某个表的元信息，进行处理后，通过IO流生成相应的文件”。



把PPT和笔记整理下

下个office PPT









