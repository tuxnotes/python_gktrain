

def decorate(func): # decorate是一个函数，参数为函数对象，返回也是函数对象
    print('running in module')
    def inner():
        return func() # 注意这里的func后是有括号（）的，说明要执行func函数的函数体
    return inner # 返回函数对象


@decorate
def func2():
    pass