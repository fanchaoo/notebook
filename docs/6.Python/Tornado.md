##### Web层框架

* 如何将请求和处理器对应在一起

1. 解释

请求大多可以表现为一个URL，或者一个复杂的请求对象(SpringMVC中的RequestMappingInfo)。

处理器可以是一个类，也可以是一个方法。比如一个Servlet，或者SpringMVC里的一个HandlerMethod等等。

将URL和处理方法对应起来，大致有两种形式。
一种是集中配置，比如在XML文件中配置所有映射。另一种是分散配置，比如SpringMVC中的RequestMapping注解。

2. 对比

SpringMVC：通过```@ReuqestMapping```注解分散配置。

Tornado：通过一个元组列表```handlers```集中配置。

* 如何接收和解析参数

1. 路径中的参数

SpringMVC：通过```@PathVariable```注解。

Tornado：通过正则表达式```(\w+)```接收，并通过注入的方式从形参中获取。

2. queryString中的参数及post表单中的参数

SpringMVC：通过```@RequestParam```注解。

Tornado：通过```self.get_argument```方法获取。

3. multipart/form-data中的参数


* 如何返回响应

1. 返回原始数据

SpringMVC：通过原生Servlet返回字符内容。

Tornado：通过 ```self.write```写入字符内容。

2. 渲染模版后返回

SpringMVC：通过ModelAndView及ViewResolver来渲染模版，通过prefix指定模版文件路径。

Tornado：通过 ```self.render```来渲染模版，通过template_path指定模版文件路径。

3. 返回二进制流


* 如何进行异常处理

SpringMVC：通过ExceptionResolver。

Tornado：在RequestHandler中重写write_error方法。 


* 如何处理静态文件

SpringMVC：通过

Tornado：通过```static_path```指定静态文件路径，通过```static_url```生成完整url。























