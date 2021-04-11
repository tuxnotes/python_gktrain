# join dead lock
from multiprocessing import Process, Queue


def f(q):
    q.put('X' * 1000000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join() # this deadlock,join一定要放到最后
    obj = queue.get()

# 交换最后两行可以修复这个问题(或直接删掉p.join())