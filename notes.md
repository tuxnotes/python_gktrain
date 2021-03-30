# Week One
## 1 课程介绍

1. 完整案例：NLP舆情系统。 需求描述-->数据收集-->数据处理-->预料处理-->深度学习-->结果测评-->调参-->展示
2. Python底层功能：作用域，面向对象编程，多线程、协程，框架

两条路线：
- 案例
- 语言层面

难点：
- 算法
- 设计模式

### 高效学习Python的方法

1. 建立高效的学习模型：以任务和目标为导向，遇到不会的功能就去现找，以后再去优化
2. 了解Python的长处：做Python擅长的事情
3. 了解Python的特性：清除的知道Python的特性
4. 官方文档必须玩的溜：官方文档有一些特性的变迁，TensorFlow只能支持到Python3.6，协程功能使用Python3.8，多线程在Linux下进行
5. 深度阅读GitHub
6. 好的问题：Google， Stack Overflow
7. 风格指引：PEP8。代码是给机器执行的，但也是给人看的

### Python开发工具

1. Visual Studio Code：尽量符合团队需求
   - pylint
   - autopep8:有时会自动改代码的顺序，只能先实例化，才能import导入，可能导致运行出错
   - remote-ssh
2. python3.6 or python3.7不同版本差别在哪里
3. jupyter notebook:数据科学家最爱
4. git

## 2 从一个需求开始

获取豆瓣读书Top250的书籍名字和短评，根据短评的舆情判断书的好坏
https://book.douban.com/top250
为什么每次都爬豆瓣？
1. 获取数据不需要登录，其他问题分解到后面
2. 豆瓣网站写的比较工整

### 2.1 实现
步骤：
1. F12调试模式分析网页源代码
2. 用request爬取网页全部内容
3. 用Beautiful Soup解析网页提取关键信息
4. 用csv文件存储书籍名字和评分

HTML标记重复的特性，才使得编写程序变得可能
返回418，需要伪装user-agent
字典需要先声明再使用，否则会报错
Beautiful Soup的安装包的名称为bs4(初学适用),还有一种网页解析库是xpath

翻页：F12，使用选择元素选择下一页，翻页其实是发送了一个GET请求。
### 2.2 pip安装加速

国内常见的镜像站：
- 豆瓣：http://pypi.douban.com/simple
- 清华：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

升级pip:
- 方法一：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
- 方法二：pip config set global.index-url http://pypi.doubanio.com/simple && pip install pip -U

配置文件：
Windows： c:\User\xxx\pip\pip.ini
Linux: ~/.pip/pip.conf

配置文件格式：
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple

### 2.3 格式化字符串
三种常用的格式化字符串方式：
1. %操作符
2. str.format(*args,**kwargs)
3. f-string: Python3.6引入，该方法源于PEP498

% 操作符--printf风格的字符串格式化
```python
import math
print('The value of Pi is approximately %5.3f.' % math.pi)
# 输出： The value of Pi is approximately 3.142.
```
.format--更加灵活
```python
print('{1} and {0}'.format('spam', 'eggs’))
# 输出: eggs and spam
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# 输出:The story of Bill, Manfred, and Georg.
```
参考: https://docs.python.org/zh- cn/3.6/lib rary/string.html#formatstrings

f- string:Python 3.6 引入 ,该方法源于 PEP 498。
https://docs.python.org/zh-cn/3.6/whatsnew/3.6.html#whatsnew36-pep498
f- string 和 %操作符、.format 比较:
1. 性能更好
2. 易读性好
三种写法比较
```python
firstname = 'yin'
lastname = 'wilson'
print('Hello, %s %s.' % (lastname, firstname))
print('Hello, {1} {0}.'.format(firstname, lastname))
print(f'Hello, {lastname} {firstname}.')
```

f- string还可以做其他事情:
```python
class Person:
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
   def __str__(self):
      return f'hello, {self.first_name} {self.last_name}.'
   def __repr__(self):
      return f'hello, {self.first_name} {self.last_name}.'
me = Person('yin', 'wilson')
print(f'{me}')
```
str(),str.format(),print()调用的是__str__方法，__str__返回的结果是给人看的，__repr__是程序对象间使用的
如果定义了repr，没有定义str，则使用取str的方法则使用repr的实现，这是一个坑，类似的还有a += b与a = a + b
# 3 复习配一条红基础知识

赋值使用 “=”符号
Python 3.8会引入海象运算符“:=” (PEP572)
赋值前不需要指定类型(分配内存)
数值、布尔、字符串、序列赋值前不需要指定类型(分配内存)

系统内置sort与列表的魔术方法的sort的区别
系统内置的sort是C++实现的，所以尽量选择内置的排序方法
内置函数和内置类型都可以在官方文档找到

# 3 简单爬虫
丰富我们的爬虫
**pythonic**
packing unpacking
a, b = b, a
推导式
调试
虚拟机环境：pip freeze > requirements.txt
**TCP协议**
爬虫被封，是IP层被封，则更换代理IP
如果是HTTP层被封，则可能需要登录，或更改HTTP层的其他配置
## 3.1 编写爬虫需要掌握HTTP、HTML基础只是

## 3.2 urllib,requests库的深入讲解
如何拿到cookie后继续请求。
两种登录方式
## 3.3 XPath的用法


01:45