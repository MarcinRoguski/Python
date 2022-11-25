y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]
z = 0


def accuracy(x, y):
    if len(x) != len(y):
        print('Listy są nierówne')
    else:
        for i in range(len(y_pred)):
            if x[i] == y[i]:
                z += 1
            else:
                continue


a = round((z/len(y_pred)), 4)
print(a)
