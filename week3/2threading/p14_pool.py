import requests
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'https://www.baidu.com',
    'https://www.qq.com'
]

# 开启线程池
pool = ThreadPool(4)
# urls的结果
results = pool.map(requests.get, urls)

# 关闭线程池等待任务完成退出
pool.close()
pool.join()

for i in results:
    print(i.url)