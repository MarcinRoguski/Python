import time
def function_performance (func):
    def wrapper(*args, **kwargs):
            start = time.perf_counter()
            func(*args, **kwargs)
            stop = time.perf_counter()
            duration = stop - start
            print('Time = {} sec.'.format(duration))
    return wrapper

my_set = {i for i in range (10000000)}
my_tuple = (i for i in range (10000000))
my_list = [i for i in range (10000000)]

number_to_find = 999999

@function_performance
def find_number (container, number_to_find):
    return number_to_find in container



print(find_number(my_set, number_to_find))
print(find_number(my_tuple, number_to_find))
print(find_number(my_list, number_to_find))
