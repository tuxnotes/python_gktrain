
import threading
import time

mutex = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1): # 上锁
            print('thread'+self.name+'get mutex')
            time.sleep(1)
            mutex.acquire()
            mutex.release()
        mutex.release() # 解锁

if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()
