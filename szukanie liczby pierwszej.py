
def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


x = int(input('Podaj zakres: '))
for y in range (2,x):
    if czy_pierwsza(y) == True:
        max = y
print(max)
    



