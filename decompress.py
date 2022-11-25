from itertools import groupby

'''
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)
'''
def decompress(number):
    #number = 22_33_44_55
    strNumber = str(number)
    result = []

    for i in range(0, len(strNumber), 2):
        a = int(strNumber[i])
        b = strNumber[i + 1]
        c = (a * b)
        result.append
        result.append(c)
    return int("".join(result))

