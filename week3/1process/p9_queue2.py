from multiprocessing import Process, Queue
import os, time


def write(q):
    print('启动write子进程： %s' % os.getpid())
    for i in ['A','B','C','D']:
        q.put(i) # 写入队列
        time.sleep(1)
    print('结束Write子进程： %s' % os.getpid())


def read(q):
    print('启动Read子进程： %s' % os.getpid())
    while True: # 阻塞，等待获取write的值
        value = q.get(True)
        print(value)
    print('结束Read子进程： %s' % os.getpid()) # 不会执行


if __name__ == '__main__':
    # 父进程穿件队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    # pr进程是一个死循环，无法等待其结束，只能强制结束
    # 写进程结束了，所以读进程也可以结束了
    pr.terminate()
    print('父进程结束')