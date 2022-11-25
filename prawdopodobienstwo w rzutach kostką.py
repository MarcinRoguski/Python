omega = {(x, y, z)
    for x in range(1, 7)
    for y in range(1, 7)
    for z in range(1, 7)
}
result = {(x, y, z) for (x, y, z) in omega if x % 2 == 1 and y % 2 == 1 and z % 2 == 1}
print('P-stwo:', round(len(result) / len(omega), 3))
