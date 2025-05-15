# Gowshik is working on a task that involves taking two lists of integers as input, finding the element-wise sum of the corresponding elements, and then creating a tuple containing the sum values.


# Write a program to help Gowshik with this task.


# Example:


# Given list:

# [1, 2, 3, 4]

# [3, 5, 2, 1]


# An element-wise sum of the said tuples: (4, 7, 5, 5)
# Input format :

# The first line of input consists of a single integer n, representing the length of the input lists.

# The second line of input consists of n integers separated by commas, representing the elements of the first list.

# The third line of input consists of n integers separated by commas, representing the elements of the second list.
# Output format :

# The output is a single line containing a tuple of integers separated by commas, representing the element-wise sum of the corresponding elements from the two input lists.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# In this scenario, the given test cases will fall under the following constraints:

# 1 ≤ n ≤ 10

# -100 ≤ elements of the list ≤ 100
# Sample test cases :
# Input 1 :

# 4
# 1, 2, 3, 4
# 3, 5, 2, 1

# Output 1 :

# (4, 7, 5, 5)

# Input 2 :

# 3
# 10, -1, 3
# 4, 5, 6

# Output 2 :

# (14, 4, 9)

# You are using Python
n=int(input())
f=list(map(int,input().split(",")))
s=list(map(int,input().split(",")))

l=[]
for i in range(len(f)):
    l.append(f[i]+s[i])
print(tuple(l))