# Alice works at a digital marketing company, where she analyzes large datasets. One day, she's tasked with processing customer ID numbers, which are long numeric sequences.


# To simplify her task, Alice needs to calculate the digital root of each ID. The digital root is obtained by repeatedly summing the digits of a number until a single digit remains.


# Help Alice write a program that reads a customer ID number, calculates its digital root, and prints the result using a loop-based approach.


# For example, the sum of the digits of 98675 is 9 + 8 + 6 + 7 + 5 = 35, then 3 + 5 = 8, which is the digital root.


# Function prototype: def digital_root(num)
# Input format :

# The input consists of an integer num.
# Output format :

# The output prints an integer representing the sum of digits for a given number until a single digit is obtained.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ num ≤ 109
# Sample test cases :
# Input 1 :

# 451110

# Output 1 :

# 3

# Input 2 :

# 1234

# Output 2 :

# 1

# Input 3 :

# 98675

# Output 3 :

# 8

num = int(input())

# You are using Python
def digital_root(nu):
    
    while(nu>9):
        s=0
        n=str(nu)
        for i in n:
            s+=int(i)
        nu=s
    return nu
print(digital_root(num))