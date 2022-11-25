#mojaLista = [1,2,3,4,5,6,7,1,3,2,3,5,1,3,4,5,1,3,4]

#print(mojaLista.index(1[, 2[, 8]]))


mojaLista = [[] for i in range (3)]
mojaLista[0] = [1,2,3]
mojaLista[1] = [4,5,6]
mojaLista[2] = [7,8,9]

print(mojaLista[1][1]) # zwraca '5'


i = 0
a = 0

mojaLista = [[] for i in range (3)]

for i in range (3):
        mojaLista[i] = [a+1, a+2, a+3] # tworzy listy nr 1,2,3
        a = a + 3
        print(mojaLista[i])

