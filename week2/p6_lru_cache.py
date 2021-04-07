# functools.lru_cache
# <<fluent python>>的例子
# functools.lru_cache(maxsize=128, typed=False)有两个可选参数
# maxsize代表缓存的内存占用值，超过这个值后，就把结果释放掉
# 若typed为True，则会把不同的参数类型得到的结果分开保存
import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    import timeit
    print('fibonacci(6)', setup='from __main__ import fibonacci')