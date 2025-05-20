# John is a data analyst who often works with text files. He needs a program that can analyze the contents of a text file and count the number of times a specific character appears in the file. 


# John wants a simple program that allows him to specify a file and a character to count within that file.
# Input format :

# The first line of input consists of the file's name to be analyzed.

# The second line of the input consists of the string they want to write within the file.

# The third line of the input consists of a character to count within the file.
# Output format :

# If the character is found, the output displays "The character 'X' appears {Y} times in the file." where X is the character and Y i the count,


# If the character does not appear in the file, the output displays "Character not found."


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# The character is to be counted as a single character (alphabetic, numeric, or special character).

# 5 ≤ length of the input string ≤ 500
# Sample test cases :
# Input 1 :

# test.txt
# This is a test file to check the character count.
# e

# Output 1 :

# The character 'e' appears 5 times in the file.

# Input 2 :

# sample.txt
# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# L

# Output 2 :

# The character 'L' appears 3 times in the file.

# Input 3 :

# data.txt
# Some random content with no special character.
# $

# Output 3 :

# Character not found in the file.

# Input 4 :

# document.txt
# This document contains multiple spaces   and a character count.
 

# Output 4 :

# The character ' ' appears 10 times in the file.

# You are using Python
f=input()
s=input()
x=input()

with open(f,'w') as file:
    if x.isalpha():
        file.write(str(s.count(x.upper())+s.count(x.lower())))
    else:
        file.write(str(s.count(x)))
with open(f,'r') as file:
    n=int(file.read())
    if(n<1):
        print("Character not found in the file.")
    else:
        print(f"The character '{x}' appears {n} times in the file.")