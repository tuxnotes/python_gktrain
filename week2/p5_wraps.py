################
# 内置的装饰方法函数

# functool.wraps
# @wrap接受一个函数来进行装饰
# 并加入了复制函数名称、注释文档、参数列表等功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functool.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=)
# 用于在定义包装饰器函数时发起调用 update_wrapper()作为函数装饰器
# 它等价于partial(update_wrapper, wrapped=wrapped, assigned=assigned)

from time import ctime, sleep
from functools import wraps

def outer_arg(bar):
    def outer(func):
        # 结构不变，增加wraps
        @wraps(func)
        def inner(*args, **kwargs):
            print('%s called at %s'%(func.__name__,ctime()))
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer

@outer_arg('foo_arg')
def foo(a,b,c):
    """ doc """
    return(a+b+c)

print(foo.__name__)

# 如果不使用wraps，则foo的函数名会替换成inner,文档也会替换成inner的注释文档

##################################
# flask 使用@wraps的案例
from functools import wraps
def requires_auth(func):
    @wraps
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)
    return auth_method

@requires_auth
def func_demo():
    pass


######################################
# 日志功能
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        def wrapped_function(*args, **kwargs):
            logs_string = func.__name__ + "was called"
            print(logs_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(logs_string+'\n')
            return func(*args,**kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# output: myfunc1 was called
