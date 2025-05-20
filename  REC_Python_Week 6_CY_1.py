# Alice is developing a program called "Name Sorter" that helps users organize and sort names alphabetically. 


# The program takes names as input from the user, saves them in a file, and then displays the names in sorted order.


# File Name: sorted_names.txt.
# Input format :

# The input consists of multiple lines, each containing a name represented as a string.

# To end the input and proceed with sorting, the user can enter 'q'.
# Output format :

# The output displays the names in alphabetical order, each name on a new line.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# In this scenario, the given test cases will fall under the following constraints:

# 3 ≤ number of names ≤ 20

# 3 ≤ length of each name ≤ 30

# The name can consist of alphabetic characters and may include spaces.
# Sample test cases :
# Input 1 :

# Alice Smith
# John Doe
# Emma Johnson
# q

# Output 1 :

# Alice Smith
# Emma Johnson
# John Doe

# Input 2 :

# David
# Oliver
# Sophia
# q

# Output 2 :

# David
# Oliver
# Sophia

# You are using Python

l=[]
while True:
    s=input()
    if s=="q":
        break
    l.append(s)
with open('sorted_names.txt','w') as file:
    for i in sorted(l):
        file.write(i+"\n")
with open('sorted_names.txt','r') as file:
    print(file.read())