python -m IPython

==> python
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

Pip, setuptools, and wheel have been installed. To update them run
  pip3 install --upgrade pip setuptools wheel

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python



1、处理中文

.py文件有中文，需要加注释：

```
#-*- coding: utf-8 -*-
```

help()查看函数文档说明。

2、Python2和Python3的区别

* input()，raw_input()

* 字典的keys()返回值类型不同

* Python2捕获多个异常的时候需要使用元组：(NameError,FileNotFoundError)

* Python3捕获所有异常：```except Exception as ex:```；Python2捕获所有异常：```except:```；

* pip install xxx，pip3 install xxx。

* Python3的range()返回值不是一个简单的列表。

3、标识符和关键字

```
>>> import keyword
>>> keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

4、变量和常量

* 概念

变量相当于一个容器，使用来存数据用的。

变量定义 = 声明 + 初始化，Python变量不须要声明。

* 变量的类型

数字(int,long,float)，布尔，字符串，列表，元组，字典，集合。

type()函数判断变量类型：

```
>>> a = '10'
>>> type(a)
<type 'str'>
```

类型强转：

```
>>> a = '10'
>>> type(a)
<type 'str'>
>>> b = int(a)
>>> type(b)
<type 'int'>
```

input()函数从键盘读取的内容，默认为字符串类型。

羊肉串都吃过吗，一块一块羊肉穿起来就是羊肉串，那一个个字符串起来就是字符串。

* 变量的作用域

局部变量：函数内定义的变量

全局变量：函数外定义的变量

global关键字：将变量声明为全局变量

globals()：返回所有全局变量；

locals()：返回所有局部变量。

LEGB(变量搜索路径)：locals -> enclosing -> globals -> builtins

* 引用

Python中的变量都是引用类型：

```
>>> a = 100
>>> b = a
>>> id(a)
43808412
>>> id(b)
43808412

>>> b = 200
>>> id(b)
43809196
>>> b = 100
>>> id(b)
43808412
```

* 变量的分类：

可变和不可变：

不可变：数字，字符串，元组。

可变：列表，字典。

可迭代：

字符串，列表，元组，字典，集合。

* 常量就是不变的量。

字符串字面量也是一种常量。

5、运算符

* 算数运算符：

```
>>> 1 + 1
2
>>> 1 - 1
0
>>> 3 * 3
9
>>> 10 / 3
3
>>> 10 // 3
3
>>> 10 % 3
1
>>> 2 ** 10
1024
>>> 'ok' * 3
'okokok'
```

* 比较运算符：

```
>，>=，<，<=，==，!=
```

* 逻辑运算符：

```
and，or，not
```

6、模版和数据

模版 + 数据 = 最终输出

```
a = 2
b = 'str'
c = True
print("a:%s, b:%s, c:%s" %(a, b, c))
```

```
a:2, b:str, c:True
```

7、流程控制：if-else

* 语法

Python的if语句，判断表达式没有小括号，而是靠空格分割的；  
语句体没有大括号，是靠冒号和缩进标识语句块的。

```
a = 1
if a == 1:
    print "ok"
    print "ok2"
elif a == 3:
    print "heihei"
else:
    print "no"
    print "no2"
```

* 判断表达式中，```0，""，[]，()，{}，None```均相当于False


8、流程控制：while

```
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

9、流程控制：for-in

in 后面的变量必须是可迭代类型：

```
s = "abc"
for temp in s:
    print temp
```

10、流程控制：break，continue

break：跳过循环体剩余语句，直接结束整个循环

continue：跳过循环体剩余语句，继续下次迭代

11、字符串

将数字转换为字符串：

```
>>> num = 100
>>> num = str(100)
>>> num
'100'
```

计算字符串长度：

```
>>> s = '123'
>>> len(s)
3
```

字符串连接：

```
>>> a = 'a'
>>> b = 'b'
>>> c = a + b
>>> c
'ab'
```

```
>>> a = 'a'
>>> b = '---%s---'%a
>>> b
'---a---'
```

字符串支持负下标：

```
>>> s = 'abc'
>>> s[-1]
'c'
```

切片操作(包前不包后)：

s[ 起始下标 : 终止下标+1 : 步长 ]

步长为正时，默认从第一位开始；步长为负时，默认从倒数第一位开始。

```
>>> s = 'abcdef'
>>> s[2:5]
'cde'
>>> s[2:-2]
'cd'
>>> s[2:]
'cdef'
>>> s[2::2]
'ce'
>>> s[-1::-1]
'fedcba'
>>> s[::]
'abcdef'
>>> s[:]
'abcdef'
>>> s[::-1]
'fedcba'
```

12、字符串常用方法

```
s.capitalize s.endswith   s.isalnum    s.istitle    s.lstrip     s.rjust      s.splitlines s.translate
s.center     s.expandtabs s.isalpha    s.isupper    s.partition  s.rpartition s.startswith s.upper
s.count      s.find       s.isdigit    s.join       s.replace    s.rsplit     s.strip      s.zfill
s.decode     s.format     s.islower    s.ljust      s.rfind      s.rstrip     s.swapcase
s.encode     s.index      s.isspace    s.lower      s.rindex     s.split      s.title
```

split()方法，若不传参数，则默认按空白字符分割(空格，制表，换行)。

13、列表

list中元素可以是不同类型：

```
>>> l = []
>>> l
[]
>>> l = [1,'2']
>>> l
[1, '2']
```

常用方法：

```
In [1]: l = []

In [2]: l.
           l.append  l.index   l.remove
           l.count   l.insert  l.reverse
           l.extend  l.pop     l.sort
```

增：

append()：在末尾追加

insert()：在指定位置添加

extend()：扩展列表，参数必须是可迭代对象，若参数是字典，则添加键值。

删：

pop()：删除末尾元素

remove()：根据内容删除

del list1[2]：根据下标删除(将引用断开)

改：  
list1[2] = "new value"

查：  
查值存不存在：'a' in list1

连接列表：

```
>>> list1 = [1, 2]
>>> list2 = [3]
>>> list3 = list1 + list2
>>> list3
[1, 2, 3]
```

列表也可以使用切片操作，来获取子列表。  
列表可以用for-in来迭代。

列表排序:

```
>>> nums = [3, 3, 2, 1]
>>> nums.sort()
>>> nums
[1, 2, 3, 3]
>>> nums.sort(reverse=True)
>>> nums
[3, 3, 2, 1]
```

删除时的一些坑：

```
# 可以通过倒着循环删除，或通过临时列表。
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i == 2 or i == 3:
        a.remove(i)
print(a)
```
```
[1, 3, 4, 5, 6]
```

```
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i == 2 or i == 3:
        del i
print(a)
```
```
[1, 2, 3, 4, 5, 6]
```

```
>>> a = [1, 2, 3, 2, 3]
>>> a.remove(2)
>>> a
[1, 3, 2, 3]
```
```
>>> a = [1, 2, 3]
>>> b = a[0]
>>> del b
>>> a
[1, 2, 3]
```


* 列表生成式

range()函数(用来生成列表)：

```
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10, 3)
[2, 5, 8]
>>> range(10, 2, -2)
[10, 8, 6, 4]
```

列表生成式：

```
>>> a = [i for i in range(2, 10)]
>>> a
[2, 3, 4, 5, 6, 7, 8, 9]

>>> b = [2 for i in range(2, 10)]
>>> b
[2, 2, 2, 2, 2, 2, 2, 2]

>>> c = [i for i in range(2, 10) if i % 2 == 0]
>>> c
[2, 4, 6, 8]

>>> d = [i for i in range(3) for j in range(2)]
>>> d
[0, 0, 1, 1, 2, 2]

>>> e = [(i, j) for i in range(3) for j in range(2)]
>>> e
[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```


14、字典

* 类似Java中的HashMap，类似JS中的对象，相当于JSON。

* 字典的键必须是“不可变类型”。

* 增删改查：

增：  
dict['name'] = 'fanchao'

删：  
del dict['name']，键值不存在时会报错。

改：  
dict['name'] = 'fanchaoo'

查：  
根据键查值：dict['name']  
根据键查值：dict.get('name')

* 常用方法：

```
In [1]: d={}

In [2]: d.
           d.clear      d.get        d.iteritems  d.keys       d.setdefault d.viewitems
           d.copy       d.has_key    d.iterkeys   d.pop        d.update     d.viewkeys
           d.fromkeys   d.items      d.itervalues d.popitem    d.values     d.viewvalues
```

* 字典遍历：

```
dict = {"name":"fanchao", "age": 23}
for key, value in dict.items():
    print("%s %s" %(key, value))
```

15、元组

* 元组定义：

```
In [1]: t = ()

In [2]: t.
           t.count
           t.index
```

* 元组赋值:

```
>>> t = (1, 2, 3)
>>> t1 = t
>>> t1
(1, 2, 3)
>>> t2, t3, t4 = t
>>> t2
1
>>> t3
2
>>> t4
3
```

* 变量交换：

```
a, b = b, a
```

```
a = a + b
b = a - b
a = a - b
```

```
c = a
a = b
b = c
```

单元素元组必须加逗号：`(1,)`

16、函数

* 函数定义和调用：

```
def add(a, b):
    print(a + b)
    return a + b

add(1, 2)
```

* 参数：

形参-parameter，实参-argument。

默认参数(只能放在参数列表末尾)：

```
def add(a, b=2, c=3):
    print(a + b + c)

add(1, 1, 1)
add(1)
add(1, c=2)
```

```
3
6
5
```

变长参数：

```
def test(a, b, c=3, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(1, 2, 3, 4, 5, name="fanchao")
test(1, 2, 3, *(4, 5, 6), **{"name": "fanchao"})
```

```
1
2
3
(4, 5)
{'name': 'fanchao'}
1
2
3
(4, 5, 6)
{'name': 'fanchao'}
```

* 返回值：

参数就是输入，返回值就是输出，函数的作用就是将输入处理后，返回处理后的输出。

多返回值(返回元组)：

```
def test():
    a = 1
    b = 2
    c = 3
    return a, b, c

a, b, c = test()
```

17、匿名函数

排序时使用：

```
peoples = [{"name": "fanchao", "age": 23}, {"name": "zhangsan", "age": 10}, {"name": "list", "age": 30}]
peoples.sort(key=lambda x : x["age"])
print(peoples)
```

```
[{'age': 10, 'name': 'zhangsan'}, {'age': 23, 'name': 'fanchao'}, {'age': 30, 'name': 'list'}]
```

做实参：

```
def test(a, b, func):
    result = func(a, b)
    print(result)

test(1, 2, lambda x, y: x + y)
test(1, 2, eval("lambda x, y: x + y"))
```

```
3
3
```

18、可变参数和不可变参数

```
def test(x):
    x += x
    print(x)

list = [1,2]
test(list)
print(list)

a = 5
test(a)
print(a)
```

```
[1, 2, 1, 2]
[1, 2, 1, 2]
10
5
```

* "num += num"和"num = num + num"不等价：

```
def test(x):
    x = x + x
    print(x)

list = [1,2]
test(list)
print(list)
```

```
[1, 2, 1, 2]
[1, 2]
```

19、文件操作

* 常用方法：

```
f.close      f.errors     f.isatty     f.newlines   f.readinto   f.seek       f.truncate   f.xreadlines
f.closed     f.fileno     f.mode       f.next       f.readline   f.softspace  f.write
f.encoding   f.flush      f.name       f.read       f.readlines  f.tell       f.writelines
```

* 打开 -> 读/写 -> 关闭

* 打开和关闭

```
f = open("test.py", "w")
f.close()
```

r：只读，文件必须存在，否则报错。

w：写，不存在则创建，存在则覆盖。

a：追加，不存在则创建，存在则追加。

可读可写：r+，w+，a+。

针对二进制：rb，wb，ab。

针对二进制可读可写：rb+，wb+，ab+。

* 文件读取

读取5个字节，返回读取内容：

```
content = f.read(5)
```

读取整个文件，返回读取内容：

```
content = f.read()
```

读取一行，返回该行内容：

```
content = f.readline()
```

按行读取整个文件，返回一个列表：

```
contents = f.readlines()
```

* 文件写入

写入内容：

```
f.write("abc")
```

* 文件定位

seek()：

```
f.seek(3, 0)
```

第二个参数，0-开头，1-当前位置，2-末尾。

获取当前位置：

```
pos = f.tell()
```

* 重命名和删除

```
import os
os.rename("a.txt", "b.txt")
os.remove("b.txt")
```

* 文件夹操作

```
import os

os.mkdir("test")

os.rmdir("test")

cwd = os.getcwd()

os.chdir("../")

files = os.listdir("./")
```

* 批量重命名文件

```
import os

folder_name = raw_input("please input your folder name...")

file_names = os.listdir(folder_name)

os.chdir(folder_name)

for name in file_names:
    print(name)
    os.rename(name, "[Test]-" + name)
```

20、面向对象

* 类

三要素：类名、属性、方法。

* 类和对象

```
class Dog:

    def __init__(self, name):
        self.name = name
        print("%s has borned..." %self.name)

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name != "dog":
            self.name = name
        else:
            self.name = "error"

    def eat(self):
        print("%s is eating..."%self.name)

dog = Dog("tom")
print(dog)
dog.set_name("dog")
print(dog.get_name())
dog.eat()
```

```
tom has borned...
tom
error
error is eating...
```

* 类内部的各种方法

https://www.cnblogs.com/funfunny/p/5892212.html

* 私有方法

```
def __private():
  pass
```

* "_del_()" 方法

当对象销毁时被调用。

查看对象引用个数：

```
import sys

class T:
    pass

t = T()
t2 = t
print(sys.getrefcount(t))
```

```
3
```

* 继承

```
class A(object):
    def test1(self):
        print("A test1")

    def test2(self):
        print("A test2")

class B(A):
    def test1(self):
        print("B test1")

class C(B):
    def test1(self):
        super(C, self).test1()
        print("C test1")

c = C()
c.test1()
```

私有属性和私有方法不会被继承。

某一个类的公有方法可以访问该类的私有属性和私有方法。

子类构造时，会先调用父类的构造方法。

* 多继承

```
class A(object):
    def test(self):
        print("A")


class B:
    def test(self):
        print("B")


class C(A, B):
    def test(self):
        print("C")

c = C()
c.test()
print(C.__mro__)
```

```
C
(<class '__main__.C'>, <class '__main__.A'>, <type 'object'>, <class __main__.B at 0x02A02A78>)
```

* 多态

```
class A(object):

    def test(self):
        print("A")

class B(A):

    def test(self):
        print("B")

def introduce(item):
    item.test()

a = A()
b = B()
introduce(a)
introduce(b)
```

```
A
B
```

* 类属性，类方法和静态方法

类属性：

```
class A(object):
    num = 0

    def __init__(self):
        A.num += 1

a = A()
a1 = A()
print(a.num)
print(a1.num)
print(A.num)
```

```
2
2
2
```

类方法和静态方法：

```
class A(object):
    num = 0

    @classmethod
    def test1(cls):
        cls.num += 1

    @staticmethod
    def test2():
        print("staticmethod")
```

* __new__()和__init()

__new()__只负责创建对象，__init__()只负责初始化对象。

```
class A(object):
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)

    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__")

a = A()
```
```
__new__
__init__
__del__
```

* 单例模式

因为Java的构造函数不能带返回值，所以若要在对象创建的时候控制对象的唯一，则只能通过方法来返回。
如果用实例方法来返回对象，则需要先用构造器创建对象，才能再调用实例方法，而构造器创建的对象不能保证唯一性。
所以只能用静态方法来返回对象，并且将构造器私有化，在静态方法中返回唯一的对象。

而Python中的__new__()方法可以有返回值，所以不需要用类方法返回唯一对象。

如何保证对象只初始化一次：

```
class Dog(object):

    __instance = None
    __init_flag = False

    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        if not self.__init_flag:
            self.name = name
            self.__init_flag = True

d1 = Dog("a")
print(id(d1))
print(d1.name)
d2 = Dog("b")
print(id(d2))
print(d2.name)
```
```
46018672
a
46018672
a
```


21、异常

* try-except

```
try:
    print(num)
    print("1")
except NameError:
    print("error happened...")

print("2")
```
```
error happened...
2
```

```
try:
    open("xxx")
    print("1")
except NameError:
    print("error happened...")

print("2")
```
```
Traceback (most recent call last):
  File "H:/Workspace/PyCharm/test/test.py", line 2, in <module>
    open("xxx")
IOError: [Errno 2] No such file or directory: 'xxx'
```

```
# -*- coding: utf-8 -*-
try:
    # open("xxx")
    print("没有异常")
except:
    print(u"发生异常")
else:
    print(u"没有异常时会执行")
finally:
    print(u"有没有异常都会执行")

print("2")
```
```
没有异常
没有异常时会执行
有没有异常都会执行
2
```

* 异常会通过函数调用栈向上传递，直到有try-except或程序崩溃。

* 自定义异常

```
# -*- coding: utf-8 -*-
class ShortInputException(Exception):
    def __init__(self, length, at_least):
        self.length = length
        self.at_least = at_least

try:
    s = raw_input(u"请输入...")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except ShortInputException as ex:
    print("ShortInputException：输入长度为%d，长度至少应为%d" %(ex.length, ex.at_least))
```
```
请输入...aa
ShortInputException：输入长度为2，长度至少应为3
```

22、模块

* 查看模块对应文件的位置(一个模块就对应一个文件)

```
>>> import os
>>> os.__file__
'C:\\Python\\python\\lib\\os.pyc'
```

* import

import xxx
import xxx as x
from xxx import yyy,zzz
from xxx import *

当导入模块时，会将模块中的代码从头到尾执行一遍。

* 模块搜索

先从当前目录搜索模块，再从Python库中搜索模块。

* ```__name__```属性

如果执行的是当前文件，则```__name__```值为```__main__```，
如果当前模块被导入其它程序执行，```__name__```值为当前模块名称。

* ```__all__```属性

选择```from xx import *```时暴露哪些内容：

```
__all__ = ["test1", "Test"]

def test1():
    print("test1")

def test2():
    print("test2")

num = 2

class Test(object):
    pass
```

* 包

一个包含"__init__.py"的文件夹就是包。

"__init__.py"中的"__all__"变量可以控制导出哪些模块。

当导入包的时候，"__init__.py"会被执行。

包中的"__init__.py"：???

```
# 决定from xx import *的时候能不能导入
__all__ = ["fanchao"]

# 决定import xx之后，xx.yy能不能使用
import fanchao
```

* 构建，打包，安装

创建setup.py：

```
from distutils.core import setup
setup(name="hahu", version="1.0", description="hahu module", author="fanchao", py_modules=["pkgname.moduname"])
```
执行命令：
```
python setup.py build
python setup.py sdist
python setup.py install
```

* 给程序传参数

```
import sys
# sys.argv是一个参数的列表
print(sys.argv)
```

23、集合

```
>>> a = [1]
>>> b = (1,)
>>> c = {1}
>>> type(a)
<type 'list'>
>>> type(b)
<type 'tuple'>
>>> type(c)
<type 'set'>
```

```
s.add                         s.difference_update           s.isdisjoint                  s.remove                      s.update                      
s.clear                       s.discard                     s.issubset                    s.symmetric_difference                                      
s.copy                        s.intersection                s.issuperset                  s.symmetric_difference_update                               
s.difference                  s.intersection_update         s.pop                         s.union                              
```



24、list和dict内置函数的时间复杂度

![](http://oy2qbfbi8.bkt.clouddn.com/17-12-28/77863311.jpg)

![](http://oy2qbfbi8.bkt.clouddn.com/17-12-28/7477201.jpg)












