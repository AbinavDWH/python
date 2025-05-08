# Meena is analyzing a list of integers and needs to count how many numbers in the list are even and how many are odd. She decides to use lambda functions to filter the even and odd numbers from the list. 


# Write a program that takes a list of integers, counts the number of even and odd numbers using lambda functions, and prints the results.
# Input format :

# The first line contains an integer n, representing the number of integers in the list.

# The second line contains n space-separated integers.
# Output format :

# The first line of output prints an integer representing the count of even numbers.

# The second line of output prints an integer representing the count of odd numbers.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ number ≤ 103
# Sample test cases :
# Input 1 :

# 7
# 12 34 56 78 98 65 23

# Output 1 :

# 5
# 2

# Input 2 :

# 10
# 12 34 56 78 98 65 23 46 61 21

# Output 2 :

# 6
# 4

# You are using Python
n=int(input())
l=list(map(int,input().split()))
ev=(lambda lst:[x for x in lst if x%2==0])(l)
o=(lambda lst:[x for x in lst if x%2!=0])(l)
print(len(ev))
print(len(o))
