# Sneha is building a more advanced exponential calculator. She wants to implement a program that does the following:


#     Calculates the result of raising a given base to a specific exponent using Python’s built-in pow() function.
#     Displays all intermediate powers from base¹ to base^exponent as a list.
#     Calculates and displays the sum of these intermediate powers.


# Help her build this program to automate her calculations.
# Input format :

# The input consists of line-separated two integer values representing base and exponent.
# Output format :

# The first line of the output prints the calculated result of raising the base to the exponent.

# The second line prints a list of all powers from base^1 to base^exponent.

# The third line prints the sum of all these powers.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ Base ≤ 20

# 0 ≤ Exponent ≤ 10
# Sample test cases :
# Input 1 :

# 2
# 3

# Output 1 :

# 8
# [2, 4, 8]
# 14

# Input 2 :

# 5
# 2

# Output 2 :

# 25
# [5, 25]
# 30


n1=int(input())
n2=int(input())
a1=pow(n1,n2)
l=[]
for i in range(1,n2+1):
    l.append(pow(n1,i))
print(a1)
print(l)
print(sum(l))