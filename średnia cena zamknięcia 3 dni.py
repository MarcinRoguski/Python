"""

playway = []

with open ('playway.txt', 'r', encoding = 'UTF-8') as file:
           for line in file:
               playway.append(list((line.split(',')))[4])

x = ((int(playway[1]) + int(playway[2]) + int(playway[3])))
print('3-dniowa średnia cena zamknięcia:', round(x/3,2))
"""

""" WERSJA UDEMY
with open('playway.txt', 'r') as file:
     lines = file.read().splitlines()
 
close = []
for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))
 
close_avg = sum(close) / len(close)
print(f'3-dniowa średnia cena zamknięcia: {close_avg:.2f}')

"""

with open('playway.txt', 'r') as file:
     lines = file.read().splitlines() #podzielone na linie

close = []
for idx, line in enumerate(lines): # wrzucamy index linii, numerujemy linie
    if idx > 0: # odrzucamy pierwszą linie z tytułem
        close.append(int(line.split(',')[-2]))#rodzielamy elementy przecinkiem i dodajemy tylko [-2]
close_avg = sum(close) / len(close)
print(f'3-dniowa średnia cena zamknięcia: {close_avg:.2f}')
