

## 目录结构

```
pom.xml

src
	main
		java
		resource
	test
		java
		resource
```

## 坐标

groupId

artifactId

version

scope

1. 问题

1.1. maven，rpm，yum，npm，这些是一回事吗？
1.2. 手动的，不用maven，在项目里面，通过IDE让一个模块依赖另一个模块，原理是啥？脱离了IDE之后，依赖关系还存在吗？
1.3. maven是如何管理多个模块之间的依赖的？原理是啥？
1.4. maven不会自动去除重复jar包吧？相同依赖的不同版本算相同jar包吗？
1.5. maven管理的jar包，直接可以循环依赖吗？
1.6. 假设A依赖B的1.1版本，那么如果在maven里只提供B的1.2版本，A可以正常工作吗？
1.7. Maven打包之后，有WEB-INF目录吗？
1.8. mvn install，在生命周期中是一个什么样的位置？
1.9. Maven项目和Maven模块有啥区别？父模块是啥？
1.10. <dependencyManagement>的应用场景？

2. 笔记

2.1. Maven是一个服务于Java项目的自动化构建工具。Maven也是Java写的。
2.2. 如何修改Maven项目默认的JDK版本。
2.3. scope为test或provided的依赖，不能被传递到别的项目或模块。但会从父项目继承过来。
2.4. 不同版本的jar包，如何选择的问题。
2.5. Maven项目的“继承”和“聚合”。