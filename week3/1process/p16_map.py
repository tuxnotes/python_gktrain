from multiprocessing import Pool
import time


def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool: # start 4 worker processes
        result = pool.apply_async(f,(10,)) # evaluate "f(10)" asynchromously in a single
        print(result.get(timeout=1)) # prints "100" unless your computer is
        print(pool.map(f, range(10))) # prints "[0,1,4,..,81]"

        it = pool.imap(f, range(10))

        print(next(it))
        print(next(it))
        print(it.next(timeout=1))

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))
