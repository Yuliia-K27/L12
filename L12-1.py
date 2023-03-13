import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
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
    results = []
    for i in range(5):
        start_time = time.time()
        calculate_factorial_threadpool()
        end_time = time.time()
        time_threadpool = end_time - start_time
        print(f'ThreadPoolExecutor time: {time_threadpool}')
        results.append(time_threadpool)

        start_time = time.time()
        calculate_factorial_processpool()
        end_time = time.time()
        time_processpool = end_time - start_time
        print(f'ProcessPoolExecutor time: {time_processpool}')
        results.append(time_threadpool)
        
    avg_time_threadpool = sum(results[::2]) / 5
    avg_time_processpool = sum(results[1::2]) / 5

    if avg_time_threadpool < avg_time_processpool:
        print('ThreadPoolExecutor is faster')
    else:
        print('ProcessPoolExecutor is faster')
