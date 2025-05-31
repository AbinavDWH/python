
# A company tracks the monthly sales data of various products. You are given a table where each row represents a product and each column represents its monthly sales in sequential months. 


# Your task is to compute the cumulative monthly sales for each product using numpy, where the cumulative sales for a month is the total sales from month 1 up to that month.
# Input format :

# The first line of input consists of two integer values, products and months, separated by a space.

# Each of the next products lines consists of months integer values representing the monthly sales data of a product.
# Output format :

# The first line of output prints: "Cumulative Monthly Sales:"

# The second line of output prints: the 2D numpy array cumulative_array that contains the cumulative sales data for each product.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ products ≤ 1000

# 1 ≤ months ≤ 1000

# Each sales value is a non-negative integer (0 ≤ sales ≤ 10000)
# Sample test cases :
# Input 1 :

# 2 4
# 10 20 30 40
# 5 15 25 35

# Output 1 :

# Cumulative Monthly Sales:
# [[ 10  30  60 100]
#  [  5  20  45  80]]

# Input 2 :

# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# Output 2 :

# Cumulative Monthly Sales:
# [[ 1  3  6]
#  [ 4  9 15]
#  [ 7 15 24]]
# # 

# You are using Python
import numpy as np

n=list(map(int,input().split()))
l=[]
for i in range(n[0]):
    l.append(list(map(int,input().split())))
for i in range(n[0]):
    for j in range(1,n[1]):
        l[i][j]+=l[i][j-1]

cumu=np.array(l)
print("Cumulative Monthly Sales:")
print(cumu)