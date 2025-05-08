# Implement a program that needs to identify Armstrong numbers. Armstrong numbers are special numbers that are equal to the sum of their digits, each raised to the power of the number of digits in the number.


# Write a function is_armstrong_number(number) that checks if a given number is an Armstrong number or not.


# Function Signature: armstrong_number(number)
# Input format :

# The first line of the input consists of a single integer, n, representing the number to be checked.
# Output format :

# The output should consist of a single line that displays a message indicating whether the input number is an Armstrong number or not.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 103.
# Sample test cases :
# Input 1 :

# 153

# Output 1 :

# 153 is an Armstrong number.

# Input 2 :

# 123

# Output 2 :

# 123 is not an Armstrong number.


# You are using Python
n=int(input())
s=str(n)
l=len(s)
su=0
for i in s:
    su+=pow(int(i),l)
if su==n:
    print(n," is an Armstrong number.")
else:
    print(n," is not an Armstrong number.")