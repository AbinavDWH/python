import numpy as np
a = np.array([1, 2, 3, 4])
print(a[0] + a[2])

b = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(b)

c = np.array([1, 2, 3, 4, 5])
x = c
c[0]=10
print(x)