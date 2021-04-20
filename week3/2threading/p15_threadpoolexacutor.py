from concurrent.futures import ThreadPoolExecutor
import time

def func(args):
    print(f'call func {args}')

if __name__ == "__main__":
    seed = ['a', 'b', 'c', 'd']

    with ThreadPoolExecutor(3) as executor:
        executor.submit(func, seed)

    with ThreadPoolExecutor(3) as executor2:
        executor.map(func, seed)

    time.sleep(1)

    with ThreadPoolExecutor(max_workers=1) as executor:
        fucture = executor.submit(pow,2,3)
        print(fucture.result())


    
