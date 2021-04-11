# 参数
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})

# - group:分组，实际上很少用
# - target：表示调用对象，可以出入方法的名字
# - name：别名，相当于给这个进程取一个名字
# - args：表示调用对象的位置参数元组，比如target是函数a,它有两个参数m,n那么args就传入(m,n)即可
# - kwargs：表示调用对象的字典

from multiprocessing import Process

def f(name):
    print(f'hello , {name}')

if __name__ == '__main__':
    p = Process(target=f, args=('john',))
    p.start()
    p.join() # 等待子进程结束


# join([timeout])
# 如果可选参数timeout是None(默认值),则方法将阻塞
# 直到调用join()方法的进程终止。如果timeout是一个证数，
# 它最多会阻塞timeout秒
# 请注意，如果进程终止或方法超时，则该方法返回None
# 检查进程的exitcode以确定它是否终止
# 一个进程可以join多次
# 进程无法join自身，因为这回导致死锁
# 尝试在启动进程之前join进程是错误的

