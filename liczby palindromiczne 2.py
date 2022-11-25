def calculate():
    for i in range(10, 100):
        for j in range (10, 100):
            liczba = i * j
            string = str(liczba)
            inverse = string[::-1]
            if string == inverse:
                result = liczba

    return result
print(calculate())
