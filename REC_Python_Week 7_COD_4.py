
# Alex is a data scientist analyzing the relationship between two financial indicators over time. He has collected two time series datasets representing daily values of these indicators over several months. Alex wants to understand how these two indicators correlate at different time lags to identify possible leading or lagging behaviors.


# Your task is to help Alex compute the cross-correlation of these two time series using numpy, so he can analyze the similarity between the two signals at various time shifts.
# Input format :

# The first line of input consists of space-separated float values representing the first time series, array1.

# The second line of input consists of space-separated float values representing the second time series, array2.
# Output format :

# The first line of output prints: "Cross-correlation of the two time series:"

# The second line of output prints: the 1D numpy array cross_corr representing the cross-correlation of array1 and array2 across different lags.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ len(array1) == len(array2) ≤ 1000

# The input values in the arrays are floating-point numbers (can be positive, negative, or zero).
# Sample test cases :
# Input 1 :

# 1.0 2.0 3.0
# 4.0 5.0 6.0

# Output 1 :

# Cross-correlation of the two time series:
# [ 6. 17. 32. 23. 12.]

# Input 2 :

# -1.0 0.0 1.0
# 1.0  0.0 -1.0

# Output 2 :

# Cross-correlation of the two time series:
# [ 1.  0. -2.  0.  1.]

# You are using Python
import numpy as np

n1=list(map(float,input().split()))
n2=list(map(float,input().split()))


arr=np.correlate(n1,n2,mode="full")
print("Cross-correlation of the two time series:")
print(arr)