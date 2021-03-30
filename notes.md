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
## 3.1 编写爬虫需要掌握HTTP、HTML基础知识
### 3.1.1 HTTP与HTML的关系
- W3C标准
- HTML常用的标签和属性
- 网页的三大组成部分：结构、表现、行为
结构：就是html，xml，爬虫就是爬结构，是我们重点关注的。
表现：CSS样式表，后面将flask会套一个bootstrap的样式表
行为：DOM数，js
浏览器中输入域名，浏览器会将其封装成HTTP协议。

client --> socket(tcp)
server ---> socket--->web server
### 3.1.2 HTML
HTML不是编程语音，是一套标记，使用标记来描述网页的结构。对于数据获取，经常获取下面的标记：
<html>内容</html>
<head>内容</head>
<body>内容</body>，在此标记之间可以包含如<p></p>标记
<img src="路径/文件名．图片格式"width="属性值"height="属性值"border="属性值"alt="属性值">
<a href="链接地址"target="打开方式"name="页面锚点名称">链接文字或者图片</a>
<div>：内容划分元素
<span>：<span> 与 <div> 元素很相似，但 <div> 是一个块元素，而 <span> 则是行内元素 。
HTML内容的匹配，则需要XPath.
BeatifulSoap是一个Python的库，而Xpath是一种匹配的技术。因此beatifulsoap不能直接与xpath对比，但是使用Python实现xpath技术的库(如lxml)可以用来与bs对比,即bs4可以与lxml进行横向对比。
bs4性能较差，主要是因为其底层是基于DOM的，将文档都载入，解析整个的DOM树。因此不管是时间，还是内存，开销都比较大。但其后期也整合了lxml
lxml是基于C和C++写的。
### 3.1.3 CSS
层叠样式表（Cascading Style Sheets）
**用途：解决内容与表现分离的问题**
内联样式表
<body style="background-color:red; "></body>
嵌入式样式表
写在 <style type=“ text/css”></style> 标记之间
外部样式
写为 .css 文件
<link rel="StyleSheet" type="text/css" href="style.css">

### 3.1.4 JavaScript
轻量级的脚本语言，由浏览器进行解释执行。
直接引用
在 <script></script> 标记中编写代码
外部引用
使用单独 .js 文件

### 3.1.5 JSON
JavaScript 对象表示法（JavaScript Object Notation）
• 多用于存储和交换文本信息
• Web 前端中运用非常广泛
• JSON 使用 JavaScript 语法来描述数据对象，但独立于语言和平台
• JSON 解析器和 JSON 库支持许多不同的编程语言

## 3.2 urllib,requests库的深入讲解
如何拿到cookie后继续请求。
两种登录方式
## 3.3 XPath的用法
七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。
xpath搜索的时候，节点之间是有前后的关系的
节点关系：
• 父（Parent）
• 子（Child）
• 同胞（Sibling）
• 先辈（Ancestor）
• 后代（Descendant）

为什么需要节点之间的关系呢，因为在匹配的时候，需要通过网页的一些内容进行匹配。

XPath 是沿着路径来选取节点的

### 3.3.1 XPath 路径表达式：
- nodeName：节点下所有的子节点
- / : 根节点选取
- // : 任意位置选取
- . : 当前节点
- .. : 当前节点的父节点
- @ :选取属性

在F12后，找到关心的内容，鼠标右键---->Copy ---> 
Copy XPath从任意的位置去找
例如： //*[@id="content"]/p[4]
Copy full xpath则显示从根开始的
/html/body/div[2]/div/div[1]/div[3]/p[4]
如果是从任意位置去找，则匹配所有的。例如对于所有的div，css的样式并不是完全一样的，因此可以通过id和type进行区分

### 3.3.2 XPath 谓语（选取位置）
谓语即是[]中的内容

| 选取的为位置   | 写法                                                        |
| -------------- | ----------------------------------------------------------- |
| 第一个元素     | /root/path/to/node[1]                                       |
| 最后一个元素   | node[last()]                                                |
| 倒数第二个元素 | node[ last() - 1 ]                                          |
| 选择属性       | //nodep[@name] ，//nodep[@name='value'] ，//nodep[@name>100 |
| 可以使用通配符 | * 和|                                                        |

XPath基本上能匹配到80%-90%的内容，但还有一部分是匹配不到的，此时就可以使用模拟浏览器的功能，一个webdriver的工具












