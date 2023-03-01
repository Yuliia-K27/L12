import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def factorial(n):
    time.sleep(1)  # імітуємо важку обчислювальну операцію
    return math.factorial(n)

def calculate_factorial_threadpool():
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 11)]
        results = [future.result() for future in futures]
        return results

def calculate_factorial_processpool():
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(factorial, i) for i in range(1, 11)]
        results = [future.result() for future in futures]
        return results

if __name__ == '__main__':
    start_time = time.time()
    calculate_factorial_threadpool()
    end_time = time.time()
    time_threadpool = end_time - start_time
    print(f'ThreadPoolExecutor time: {time_threadpool}')

    start_time = time.time()
    calculate_factorial_processpool()
    end_time = time.time()
    time_processpool = end_time - start_time
    print(f'ProcessPoolExecutor time: {time_processpool}')

    if time_threadpool < time_processpool:
        print('ThreadPoolExecutor is faster')
    else:
        print('ProcessPoolExecutor is faster')
