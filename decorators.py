import time
def function_performance (func):
    def wrapper(*args, **kwargs):
            start = time.perf_counter()
            func(*args, **kwargs)
            stop = time.perf_counter()
            duration = stop - start
            print('Time = {} sec.'.format(duration))
    return wrapper
