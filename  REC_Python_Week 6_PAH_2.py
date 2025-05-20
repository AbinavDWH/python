# Reeta is playing with numbers. Reeta wants to have a file containing a list of numbers, and she needs to find the average of those numbers. Write a program to read the numbers from the file, calculate the average, and display it.


# File Name: user_input.txt
# Input format :

# The input file will contain a single line of space-separated numbers (as a string).

# These numbers may be integers or decimals.
# Output format :

# If all inputs are valid numbers, the output should print: "Average of the numbers is: X.XX" (where X.XX is the computed average rounded to two decimal places)

# If the input contains invalid data, print: "Invalid data in the input."


# Refer to the sample output for format specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# The file will have between 1 and 100 numbers (1 ≤ n ≤ 100)
# Sample test cases :
# Input 1 :

# 1 2 3 4 5

# Output 1 :

# Average of the numbers is: 3.00

# Input 2 :

# abc 1.1 def 2.2 ghi

# Output 2 :

# Invalid data in the input.

# Input 3 :

# 5 7.9 6.5 9 10

# Output 3 :

# Average of the numbers is: 7.68

# You are using Python
try:
    l=list(map(float,input().split()))
    summ=sum(l)/len(l)
    print(f"Average of the numbers is: {summ:.2f}")
except Exception as e:
    print("Invalid data in the input.")