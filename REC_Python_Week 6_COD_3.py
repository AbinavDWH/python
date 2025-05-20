# Write a program that calculates the average of a list of integers. The program prompts the user to enter the length of the list (n) and each element of the list. It performs error handling to ensure that the length of the list is a non-negative integer and that each input element is a numeric value.
# Input format :

# The first line of the input is an integer n, representing the length of the list as a positive integer.

# The second line of the input consists of an element of the list as an integer, separated by a new line.
# Output format :

# If the length of the list is not a positive integer or zero, the output displays "Error: The length of the list must be a non-negative integer."

# If a non-numeric value is entered for the length of the list, the output displays "Error: You must enter a numeric value."

# If a non-numeric value is entered for a list element, the output displays "Error: You must enter a numeric value."


# If the inputs are valid, the program calculates and prints the average of the provided list of integers with two decimal places: "The average is: [average]".


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 0 < n ≤ 20

# The length of the list and each list element must be integers.
# Sample test cases :
# Input 1 :

# -2
# 1
# 2

# Output 1 :

# Error: The length of the list must be a non-negative integer.

# Input 2 :

# 3
# 1
# 2
# 3

# Output 2 :

# The average is: 2.00

# Input 3 :

# 3
# 1
# 2
# a

# Output 3 :

# Error: You must enter a numeric value.

# Input 4 :

# /
# 1
# 3

# Output 4 :

# Error: You must enter a numeric value.

# Input 5 :

# 0
# 0

# Output 5 :

# Error: The length of the list must be a non-negative integer.

# You are using Python
n=input()

try:
    if n.isdigit():
        if int(n)<=0 or n[0]=="-":
            raise Exception("Error: the length of the list must be a non-negative integer.")
        else:
            l=[]
            for i in range(int(n)):
                nu=input()
                if nu.isdigit():
                    l.append(int(nu))
                else:
                    raise Exception("Error: You must enter a numeric value.")
            su=0
            for i in l:
                su+=i
            print(f"The average is: {float(su/int(n)):.2f}")
    
    elif (n[0]=="-"):
        raise Exception("Error: the length of the list must be a non-negative integer.")
        
    else:
        raise Exception("Error: You must enter a numeric value.")
except Exception as e:
    print(e)
