# Sophia is developing a feature for her online banking application that calculates the total sum of digits in customers' account numbers. This sum is used to generate unique verification codes for secure transactions. She needs a program that takes an account number as input and outputs the sum of its digits.


# Help Sophia to complete her task.


# Function Specification: def sum_digits(num)
# Input format :

# The input consists of an integer, representing the customer's account number.
# Output format :

# The output prints an integer representing the sum of the digits of the account number.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 0 ≤ num ≤ 1016
# Sample test cases :
# Input 1 :

# 123245

# Output 1 :

# 17

# Input 2 :

# 0

# Output 2 :

# 0


num = int(input())

# You are using Python
def sum_digits(num):
    n=0
    for i in str(num):
        n+=int(i)
    num=n
    return num

sum = sum_digits(num)
print(sum)