import time
import functools
def execution_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result=func(*args, **kwargs)
        end_time = time.perf_counter()

        duration=end_time-start_time
        print(f"Duration: {duration:.8f} seconds")
        return result
    return wrapper
@execution_time
def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(5))

