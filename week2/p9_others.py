# 官方文档装饰器的其他用途示例
# 向一个函数添加属性

def attrs(**kwds):
    def decorator(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorator

@attrs(versionadded='2.2', author='Guido Van Rossum')
def mymethod(f):
    pass

#######################
# 函数参数观察器
import functools
def trace(f):
    @functools.wraps(f)
    def decorated_func(*args,**kwargs):
        print(f,args, kwargs)
        result = f(*args,**kwargs)
        print(result)
    return decorated_func

@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting,name)

greet('better', 'me')


#################################
# 用单例实例顶一个类
# 类占用内存，每一个对象都会占用内存

def singletone(cls):
    instance ={}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls()
        return instance[cls]
    return singletone

@singletone
class MyClass:
    pass

#################################
# 限定函数参数和返回类型
# assert 2==1,'2不等于1'断言语句为raise-if-not
# 用于比较传入的数据和期望的数据， 断言用于测试，不能
# 替代if-else，因为Python的-O参数会忽略断言
# 用来测试表达式，器返回值为假，就会触发异常


# Python2
def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a,t), \
                    "arg %r does not match %s" % (a,t)
            return f(*args,**kwds)
        new_f.func_name = f.func_name
        return new_f
    return check_accepts

def returns(rtype):
    def check_returns(f):
        def new_f(*args,**kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                'return value %r does not match %s' % (result, rtype)

            return result
        new_f.func_name = f.func_name
        return new_f
    return check_returns
@accepts(int,(int, float))
@returns((int,float))
def func(arg1,arg2):
    return arg1 * arg2

# 如下的类装饰器实现了一个用于类实例属性的Private声明
# 属性存储在一个实例上，或者从一个类继承而来
# 不接受从装饰的类的外部对这样的属性的获取和修改访问
# 但是，仍然允许类自身在其方法中自由访问哪些名称
# 类似于Java中的private属性

traceMe =False
def trace(*args):
    if traceMe:
        print('['+' '.join(map(str, args)) + ']')

def Private(*privates):
    def onDecorator(aClass):
        class onDecorator:
            def __init__(self, *args, **kwargs):
                self.wrapped= aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace('get:',attr)
                if attr in privates:
                    raise TypeError('private attribute ffetch:'+attr)
                else:
                    return getattr(self.wrapped, attr)
                
            def __setattr__(self, attr, value):
                trace('set:',attr, value)
                if attr == 'wrapped': # 这里捕捉对wrapped的赋值
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change:'+attr)
                else: # 这里捕捉对wrapped.attr的赋值
                    setattr(self.wrapped,attr, value)
        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True
    @Private('data','size')
    class Doubler:
        def __init__(self,label,start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s'%(self.label,self.data))
    
    X = Doubler('X is',[1,2,3])
    Y = Doubler('Y is',[-10,-20,-30])
    print(X.label)
    X.display()
    X.double()
    X.display()
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()

    # 这些访问都会引发异常
    print(X.size())
    print(X.data)
    X.data = [1,1,1]
    X.size = lambda S:0
    print(Y.data)
    print(Y.size())

######################################
# python3.7 引入 Data Class PEP557

class MyClass:
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

from dataclasses import dataclass
@dataclass
class MyClass:
    var_a: str
    var_b: str

var_1 = MyClass('x','y')
var_2 = MyClass('x','y')

# 不用在类中重新封装__eq__
var_1 == var_2

# 存在的问题：var_a var_b不能作为类属性访问，数据类型str的声明是无效的

##########################################
# 类装饰器还能支持
# @classmethod
# @staticmethod
# @property
# @*.setter
# @*.deleter


    
