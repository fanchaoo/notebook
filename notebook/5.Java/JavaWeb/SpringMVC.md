

# springmvc请求处理流程？

客户端发起一个请求，请求传到DispacherServlet；
在DispatcherServlet中，通过HandlerMapping找到与请求对象相对应的执行链（HandlerExecutionChain）；
然后执行链获取一个处理器适配器（HandlerAdapter）；
接着执行拦截器pre方法，通过HandlerAdapter执行处理器方法，并返回一个ModelAndView，接着调用拦截器post方法；
最后由ViewResolver将视图返回回去。

# springmvc笔记

不论控制器方法最终返回什么，最终都会转换为ModelAndView。

控制器可以处理转发(forward:)，也可以处理重定向(redirect:)。

通过RESTful实现时，可以通过前台表单的_method参数，和后台配置HiddenHttpMethodFilter过滤器，
实现将POST方法转为PUT或DELETE方法。

当配置DispatcherServlet的映射utl为“/”时，可以配置default-servlet-handler使其不拦截静态资源。

前端传过来的字段都是字符串，springmvc有相应的格式转换器，将字符串转换为对应类型或对象。






