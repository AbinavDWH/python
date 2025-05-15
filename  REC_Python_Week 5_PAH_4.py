
# Sophia is organizing a list of event IDs representing consecutive days of an event. She needs to group these IDs into consecutive sequences. For example, if the IDs 3, 4, and 5 appear consecutively, they should be grouped. 


# Write a program that helps Sophia by reading the total number of event IDs and the IDs themselves, then display each group of consecutive IDs in tuple format.
# Input format :

# The first line of input consists of an integer n, representing the number of event IDs.

# The next n lines contain integers representing the event IDs, where each integer corresponds to an event ID.
# Output format :

# The output should display each group of consecutive event IDs in a tuple format. Each group should be printed on a new line, and single event IDs should be displayed as a single-element tuple.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 20

# 1 ≤ tuple elements ≤ 25
# Sample test cases :
# Input 1 :

# 3
# 1
# 2
# 3

# Output 1 :

# (1, 2, 3)

# Input 2 :

# 5
# 10
# 11
# 12
# 15
# 16

# Output 2 :

# (10, 11, 12)
# (15, 16)

# Input 3 :

# 6
# 1
# 5
# 6
# 7
# 10
# 19

# Output 3 :

# (1)
# (5, 6, 7)
# (10)
# (19)

# You are using Python
n=int(input())
l=[]

for i in range(n):
    l.append(int(input()))

t=[]

for i in range(n):
    t.append(l[i])
    if i+1>=n:
        if len(t)==1:
            print(f"({t[0]})")
        else:
            print(tuple(t))
    elif l[i]+1!=l[i+1]:
        if len(t)==1:
            print(f"({t[0]})")
        else:
            print(tuple(t))
        t.clear()
     