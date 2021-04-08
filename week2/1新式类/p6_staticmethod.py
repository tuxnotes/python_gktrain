import datetime

class Story(object):
    snake = 'python'
    def __init__(self, name):
        self.name = name

    # 静态方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2:
            print('God is coming')

Story.god_come_go()

# 静态方法由类直接调用
# 因为不传入self也不传入cls,所以不能直接使用类属性和实例属性