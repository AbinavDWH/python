
# Sita is analyzing her company's daily sales data to find all sales values that are multiples of 5 and exceed 100. She wants to filter these specific sales values from the list. 


# Help her to implement the task using the numpy package.


# Formula:

# To filter sales values:

# Select all values s from sales such that (s % 5 == 0) and (s > 100)
# Input format :

# The first line of input consists of an integer value, n, representing the number of sales entries.

# The second line of input consists of n floating-point values, sales, separated by spaces, representing daily sales figures.
# Output format :

# The output prints: filtered_sales


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 15

# 0 ≤ sales[i] ≤ 1000
# Sample test cases :
# Input 1 :

# 5
# 50.0 100.0 105.0 150.0 99.0

# Output 1 :

# [105. 150.]

# Input 2 :

# 6
# 200.0 205.0 99.0 120.0 125.0 80.0

# Output 2 :

# [200. 205. 120. 125.]
# # 

# You are using Python
import numpy as np
n=int(input())
l=list(map(float,input().split()))

n_l=[]

for i in l:
    if i%5==0 and i>100:
        n_l.append(i)

arr=np.array(n_l)