def compress(number):
    from itertools import groupby
    result = []
    for key, group in groupby(str(number)):
        result.append(key + len(list(group)) * ".")
    result2 = ''.join(result)
    return (result2)



print(compress(11225555555555))
