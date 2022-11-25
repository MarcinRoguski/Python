
suma = x = liczba = 0

while x < 3:
    liczba = int(input("Podaj liczbę: "))
    if (liczba > 0 and liczba % 2 == 0):
        suma += liczba
    else:
        print("Liczba nie jest parzysta lub jest ujemna")
        continue
    x += 1
    
print("Podałeś", x, "liczby o łącznej sumie", suma)
    
    

