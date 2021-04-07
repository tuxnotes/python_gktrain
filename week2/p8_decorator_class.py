# 装饰类
# 要对类装饰的话，要实现与类相同的函数的名字
def decorator(aClass):
    class newClass(object):
        def __init__(self, *args):
            self.times = 0
            self.wrapped = aClass(args)

        def runtimes(self):
            # 将runtimes()替换为display()
            self.times += 1
            print('run times', self.times)
            self.wrapped.display()
        
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number

    # 重写display
    def display(self):
        print('number is ', self.number)

six = MyClass(6)
for i in range(5):
    six.runtimes()
