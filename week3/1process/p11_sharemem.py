# 在进程并发编程时，通常最好尽量避免使用共享状态。使用多个进程时尤其如此
# 如果你真的需要使用一些共享数据，那么multiprocessing提供了两种方法
# 共享内存 shared memory

# 可以使用Value或Array将数据存储在共享内容映射中
# 这里的Array和numpy中的不同，它只能是一维的，不能是多维的
# 童颜和Value一样，需要定义数据形式，否则会报错
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d',0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])