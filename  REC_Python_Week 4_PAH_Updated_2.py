
# Ravi is working on analyzing a set of integers to determine how many of them are divisible by 3 and how many are divisible by 5. He decides to use lambda functions to filter and count the numbers based on their divisibility.


# Write a program that takes a list of integers, calculates how many numbers are divisible by 3, and how many are divisible by 5, and then prints the results.


# Additionally, the program should calculate the total sum of all numbers divisible by 3 and divisible by 5 separately.
# Input format :

# The first line contains an integer n, representing the number of integers in the list.

# The second line contains n space-separated integers.
# Output format :

# The first line should print the count of numbers divisible by 3.

# The second line should print the count of numbers divisible by 5.

# The third line should print the sum of numbers divisible by 3.

# The fourth line should print the sum of numbers divisible by 5.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following specifications:

# 1 ≤ n ≤ 50

# 1 ≤ number ≤ 100
# Sample test cases :
# Input 1 :

# 6
# 3 5 6 10 15 20

# Output 1 :

# 3
# 4
# 24
# 50

# Input 2 :

# 10
# 2 4 7 8 11 13 17 19 23 29

# Output 2 :

# 0
# 0
# 0
# 0

# You are using Python
n=int(input())
l=list(map(int,input().split()))

d_3=[]
d_5=[]
m = lambda s:d_3.append(s) if s%3==0 else None
p = lambda s:d_5.append(s) if s%5==0 else None
for i in range(n):
    m(l[i])
    p(l[i])
print(len(d_3))
print(len(d_5))
print(sum(d_3))
print(sum(d_5))