# 父类
class People(object):
    def __init__(self):
        self.gene = 'XY'
        # 假设人人都有名字
        self.name = name
    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self, name):
        # 找到Man的父类People，把类People的对象转换为类Man的对象
        # super(Man, self).__init__(name)
        super().__init__(name) # 随着Python版本的演进，进化成这种写法了
        # self.name = name

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        super().__init__(name) # super表示父类，其会按括号内写的父类进行查找

    def shopping(self):
        print('buy buy buy')

p1 = Man('Adam')
p2 = Woman('Eve')

# 问题1： gene有没有被继承
# 没有被继承，子类的__init__覆盖了父类的__init__，所以需要使用super(Man, self).__init__()
p1.gene

# 问题2： People的父类是谁
# type与object
print('object',object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type元类由type自身创建，object类由元类type创建(创建关系)
# type继承了object类
# type people list dict 都是object的子类， object没有父类(继承关系)
# Python中一切皆对象，object也是个对象，由type创建，object是type的实例，type是它自己的实例
# People也是type的实例

# 问题3： 能否实现多重层级继承


# 问题4： 能否实现多个父类同时继承
class Son(Man, Woman):
    pass

# 新的问题：继承顺序
# 钻石继承：C3算法
# 方法解析顺序MRO
# 图论：有向无环图
