# GOD

class Human(object):
    # 使用__init__接受参数
    def __init__(self, name):
        # self表示对象本身，约定俗成
        self.name = name

h1 = Human('Adam')
h2 = Human('Eve')

# 对实例属性做修改
h1.name = 'python'
h1.name
h2.name

# 删除实例属性
del h1.name

# AttributeError
# 访问不存在的属性
h1.name

######################
# 对属性进行拦截
# GOD

class Human(object):
    # 使用__init__接受参数
    def __init__(self, name):
        # self表示对象本身，约定俗成
        self.name = name
        self.age = 18

    def __getattr__(self, item):
        """
        拦截不存在的属性
        """
        print('Human2.__getattr__')
        self.item = item
        if self.item == 'fly':
            return 'superman'

    def __getattribute__(self, item):
        """
        拦截已存在的属性
        """
        print('Human2.__getattr__')
        return super().__getattribute__(item) # super代表父类，这里表示调用父类的__getattribute__

    def __getattribute__(self, item):
        """
        将不存在的属性设置为100并返回
        """
        print('Human2.__getattr__')
        try:
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h1 = Human2('Adam')
# __getattr__拦截任意属性
# __getattribute__返回存在的属性，如果不存在则抛出TypeError异常，继续访问__getattr__函数
# 可以根据原理改造__getattribute__实现__getattr__
# 如果同时存在，则执行顺序是__getattribute__ > __getattr__ > __dict__
h1.fly
h1.age
h1.noattr

# __getattribute__底层原理是描述器



