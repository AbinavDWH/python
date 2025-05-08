# Sara is developing a text-processing tool that checks if a given string starts with a specific character or substring. She needs to implement a function that accepts a string and a character (or substring), and returns True if the string starts with the provided character/substring, or False otherwise. 


# Write a program that uses a lambda function to help Sara perform this check.
# Input format :

# The first line contains a string `str` representing the main string to be checked.

# The second line contains a string `n`, which is the character or substring to check if the main string starts with it.
# Output format :

# The first line of output prints "True" if the string starts with the given character/substring, otherwise prints "False".


# Refer to the sample for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ str ≤ 50
# Sample test cases :
# Input 1 :

# Examly
# e

# Output 1 :

# False

# Input 2 :

# placement season
# p

# Output 2 :

# True

# Input 3 :

# English
# eng

# Output 3 :

# False

# Input 4 :

# BestSchool
# Best

# Output 4 :

# True

# You are using Python

s1=input().strip()
s2=input().strip()

t=lambda s,sub:s.startswith(sub)
print(t(s1,s2))

