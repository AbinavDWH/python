import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 4,5,6,7,8,9,10 ])
print(a)

mat=np.array([[1, 0, 1], [1, 0, 1], [0, 1,0]])
print(mat)
print(mat.shape)
print(mat.ndim)

a1=a.reshape(5,2)
print(a1)

ran=np.random.randint(1,100)
print(ran)

mat1=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(mat1+mat)

print(mat1*mat)

