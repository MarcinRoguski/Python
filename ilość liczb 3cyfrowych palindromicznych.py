def calculate():
    x = 0
    for i in range (100, 1000):
        string = str(i)
        inverse = string[::-1]
        if string == inverse:
           x = x + 1
    return x
print(calculate())
