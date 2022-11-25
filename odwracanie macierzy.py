def transpose(array):
#array = [[1, 2, 3], [4, 5, 6]]
    print(len(array))
    w = len(array)  # 2
    h = len(array[0])  # 3
    array2 = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            array2[i][j] = array[j][i]
    return array2
