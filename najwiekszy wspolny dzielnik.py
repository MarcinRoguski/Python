def greatest_common_divisor(a, b):

    wynik = 0
    while b > 0:  
        wynik = a // b
        reszta = a - (b * wynik)
        a = b
        b = reszta
    return a





    
