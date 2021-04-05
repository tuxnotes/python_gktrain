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

