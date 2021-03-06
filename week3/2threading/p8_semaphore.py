import time
import threading

num = 0
semaphore = threading.BoundedSemaphore(5) # 最多允许5个线程同时运行

def run(n):
    semaphore.acquire()
    print('run the thread : %s' % n)
    time.sleep(1)
    semaphore.release()

for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()