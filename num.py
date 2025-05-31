import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]])
print(arr)
# s = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e'])
# new_elements = pd.Series([6, 7], index=['f', 'g'])

# # Use pd.concat to append new elements
# s = pd.concat([s, new_elements])
# print(s[:'d'])

# d= {'a': [5,3,6], 'b': [4,5,7], 'c': [8,9,10], 'd': [11,12,13]}

# df=pd.DataFrame(d)
# print(df)