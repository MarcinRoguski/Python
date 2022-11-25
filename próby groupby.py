def compress(number):
    from itertools import groupby


    result = []
    for key, group in groupby(str(number)):

        result.append(str(key) + str(len(list(group))))
    result2 = '_'.join(result)
    print(result2) 
print(compress(11225555555555))

