def map_longest(arg):
    #lista = arg.split(" ")
    lista = (arg)
    wordLen = 0
    maxWordLen = 0
    for word in lista:
        wordLen = len(word)
        if maxWordLen < wordLen:
            maxWordLen = wordLen

    return maxWordLen
