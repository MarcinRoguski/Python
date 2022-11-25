import random as rnd
from decorators import function_performance


my_list = [i for i in range(100000000)]
number_to_find = rnd.randint(0, 100000000)


@function_performance
def binary_search(my_list, number_to_find):
    first = 0
    last = len(my_list)-1
    found = False
    while (first <= last and not found):
        mid = (first + last)//2
        if my_list[mid] == number_to_find:
            found = True
        else:
            if number_to_find < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search(my_list, number_to_find))


@function_performance
def linear_search(my_list, number_to_find):
    return number_to_find in my_list


print(linear_search(my_list, number_to_find))
