import queue

q = queue.Queue(5)

q.put(111)
q.put(222)
q.put(333)

print(q.get()) # 取队列
print(q.get())
q.task_done() # 每次从q中get一个数据后，当处理好相关问题，最后调用此方法
              # 以提示q.join()是否停止阻塞，让线程向前执行或退出
print(q.qsize()) # 队列元素个数
print(q.empty()) # 队列是否为空
print(q.full())  # 队列是否满了

#################################
import queue
import threading
import random
import time

writelock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self,q, con, name):
        super(Producer,self).__init__()
        self.q = q
        self.con = con
        self.name = name        
        print(f'Producer {self.name} started')

    def run(self):
        while True:
            global writelock
            self.con.aquire() # 获得锁对象

            if self.q.full(): # 队列满
                with writelock:
                    print('Queue is full, produce wait')
                self.con.wait() # 等待资源
            else:
                value = random.randint(0,10)
                with writelock:
                    print(f'{self.name} put value {self.name} {str(value)} in queue')
                self.q.put( (f'{self.name}: {str(self.value)}') ) # 存入队列
                self.con.notify() # 通知消费者
                time.sleep(1)
            self.con.release()

class Consumer(threading.Thread):
    def __init__(self,q, con, name):
        super(Consumer,self).__init__()
        self.q = q
        self.con = con
        self.name = name        
        print(f'Consumer {self.name} started')

    def run(self):
        while True:
            global writelock
            self.con.aquire() # 获得锁对象

            if self.q.empty(): # 队列满
                with writelock:
                    print('Queue is full, produce wait')
                self.con.wait() # 等待资源
            else:
                value = self.q.get()
                with writelock:
                    print(f'{self.name} put value {self.name} {str(value)} in queue')                
                self.con.notify() # 通知消费者
                time.sleep(1)
            self.con.release()            

if __name__ == '__main__':
    q = queue.Queue(10)
    con = threading.Condition() # 条件变量

    p1 = Producer(q, con, 'P1')
    p1.start()
    p2 = Producer(q, con, 'P2')
    p2.start()
    c1 = Consumer(1, con, 'C1')
    c1.start()

