# 钻石继承
class BaseClass(object):
    num_base_calls = 0
    def call_me(self):
        print('Calling method on Base Class')
        self.num_base_call += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print('Calling method on Left Subclass')
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        print('Calling method on Right Subclass')
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        print('Calling method on Subclass')
        self.num_sub_calls += 1

a = Subclass()
a.call_me()
print(Subclass.mro())

# 广度优先，Python3中不加object也是新式类，但为了代码不会误运行在Python2中产生意外结果，仍然
# 修改RightSubclass的父类为object,再次执行print(Subclass.mro())观察结果