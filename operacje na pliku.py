import pprint

try:
    with open('imionanazwiska.txt', 'a', encoding = "UTF-8",) as file:
        #file.write("Marcin Roguski")
        content = file.read().splitlines()
        pprint.pprint(content)
        
except FileNotFoundError:
    print('Nie znaleziono pliku.')
