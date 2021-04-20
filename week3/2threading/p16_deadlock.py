from concurrent.futures import ThreadPoolExecutor
import time

def wait_on_b():
    time.sleep(5)
    print(b.result()) # b will never complet because it wait on a 
    return 5 

def wait_on_a():
    time.sleep(5)
    print(a.result())# a will never complet because it wait on b
    return 6 

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

# 当回调已关联了一个future，然后再等待另一个future的结果时会产生死锁情况

