# I have a dream

class MyFirstClass: # Python2中这样的写法为经典类
    pass

a = MyFirstClass()
b = MyFirstClass()
# 不同内存地址，两个不同对象
type(a)
id(a)
a.__class__()
b.__class__()

# 类也是对象
c = MyFirstClass
d = c()
d.__class__()

###########################
# GOD
class Human(object): # python3中带不带object都会认为是新式类，Python2中这里的写法为新式类
    # 静态字段,写在方法外面，也叫类属性
    live = True
    def __init__(self, name): # self不是关键字，是约定俗称的写法，init只有一个功能：接受类传进来的参数
        # 普通字段
        self.name = name

man = Human('Adam')
woman = Human('Eve')

# 有live属性
Human.__dict__
# 有name属性
man.__dict__

# 实例可以使用普通字段也可以使用静态字段
man.name
man.live = False
man.__dict__ # 普通字段有live变量
man.live
woman.live # 其他对象还是从类的静态字段读取
# 类可以使用静态字段
Human.live

# 可以为类添加静态字段
Human.newattr = 1
dir(Human)
Human.__dict__

# 内置类型不能增加属性和方法
setattr(list, 'newattr', 'value')
# TypeError

#######################
class Human2(object):
    # 认为约定，不可修改
    _age = 0
    # 私有属性
    __fly = False

    # 魔术方式，前后两个双下划线不会自动改名
    # __init__

# 自动改名机制做的隐藏
Human2.__dict__
# '_Human2__fly': False
