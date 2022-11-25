def delta(a, b, c):

    x = b ** 2 - (4 * a * c)

    if x < 0:
        print('Delta mniejsza od zera, brak miejsc zerowych')
    else:
        x1 = ((-1 * b) - x ** 0.5)/(2 * a)
        x2 = ((-1 * b) + x ** 0.5)/(2 * a)

        print(f'Delta równa się: {x}')
        print(f'X1 = {round(x1, 2)}')
        print(f'X2 = {round(x2, 2)}')
