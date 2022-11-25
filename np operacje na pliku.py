import numpy as np

x = np.arange(12).reshape(3, 4)

np.save('array.npy', x)
file = np.load('array.npy')
print(file)

