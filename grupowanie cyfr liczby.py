def compress(number):
    numberCompressed = []
    x = 1
    a = tuple()
    strNumber = str(number)
    for i in range(len(strNumber) - 1):
        if strNumber[i] == strNumber[i+1]:
            x = x + 1

        elif strNumber[i] != strNumber[i+1]:
            a = (strNumber[i], x)
            numberCompressed.append(a)
            x = 1


            
    a = (strNumber[i], x)
    numberCompressed.append(a)

            
    return numberCompressed
print(compress(12233344445555555555))

            
        
