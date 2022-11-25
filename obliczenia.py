import figury

#enumeration - spis - wyliczenie

from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', {'Kwadrat':1, 'Prostokąt':2 , 'Koło':3, 'Trójkąt':4, 'Trapez':5})

print(list(Menu_Figury))
wybor = int(input("""Wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez
"""))

if (wybor == Menu_Figury.Kwadrat):
    a = float(input("Podaj bok kwadratu: "))
    print("Pole kwadratu wynosi:", figury.pole_kwadratu(a))
elif (wybor == Menu_Figury.Prostokąt):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    print("Pole prostokąta wynosi:", figury.pole_prostokata(a, b))
elif (wybor == Menu_Figury.Koło):
    r = float(input("Podaj promień koła: "))
    print("Pole koła wynosi:", figury.pole_kola(r))
elif (wybor == Menu_Figury.Trójkąt):
    a = float(input("Podaj bok trójkąta: "))
    h = float(input("Podaj wysokość trójkąta: "))
    print("Pole trójkąta wynosi:", figury.pole_trojkata(a, h))
elif (wybor == Menu_Figury.Trapez):
    a = float(input("Podaj 1-szy bok prostokąta: "))
    b = float(input("Podaj 2-gi bok prostokąta: "))
    h = float(input("Podaj wysokość trapezu: "))    
    print("Pole trapezu wynosi:", figury.pole_trapezu(a, b, h))

