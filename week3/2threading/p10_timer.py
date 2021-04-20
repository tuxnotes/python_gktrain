from threading import Timer

def hello():
    print('hello world')

t = Timer(1, hello) # 每1秒后执行hello函数
t.start()