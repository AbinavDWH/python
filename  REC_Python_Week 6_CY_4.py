# Bob, a data analyst, requires a program to automate the process of analyzing character frequency in a given text. This program should allow the user to input a string, calculate the frequency of each character within the text, save these character frequencies to a file named "char_frequency.txt," and display the results.
# Input format :

# The input consists of the string.
# Output format :

# The first line prints "Character Frequencies:".

# The following lines print the character frequency in the format: "X: Y" where X is the character and Y is the count.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ length of string ≤ 1000

# The input string can contain any printable characters, including:

#     Alphabetic characters (uppercase and lowercase).
#     Digits.
#     Special characters (e.g., punctuation marks, spaces).

# Case sensitivity should be considered when counting frequencies (i.e., 'A' and 'a' are different characters).

# Whitespace characters (spaces, tabs) should be counted as valid characters.
# Sample test cases :
# Input 1 :

# aaabbbccc

# Output 1 :

# Character Frequencies:
# a: 3
# b: 3
# c: 3

# Input 2 :

# Data analyst job is challenging and fun

# Output 2 :

# Character Frequencies:
# D: 1
# a: 6
# t: 2
#  : 6
# n: 5
# l: 3
# y: 1
# s: 2
# j: 1
# o: 1
# b: 1
# i: 2
# c: 1
# h: 1
# e: 1
# g: 2
# d: 1
# f: 1
# u: 1

# Input 3 :

# "~~~~!!!@@@@##$$$$%%%%&&&

# Output 3 :

# Character Frequencies:
# ": 1
# ~: 4
# !: 3
# @: 4
# #: 2
# $: 4
# %: 4
# &: 3

# You are using Python
s=input()
l=[]
for i in s:
    if i not in l:
        l.append(i)
print("Character Frequencies:")
for i in l:
    print(f"{i}: {s.count(i)}")