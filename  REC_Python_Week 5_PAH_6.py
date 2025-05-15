# Jordan is creating a program to process a list of integers. The program should take a list of integers as input, remove any duplicate integers while preserving their original order, concatenate the remaining unique integers into a single string, and then print the result.


# Help Jordan in implementing the same.
# Input format :

# The input consists of space-separated integers representing the elements of the set.
# Output format :

# The output prints a single integer formed by concatenating the unique integers from the input in the order they appeared.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ the elements of the set ≤ 10000
# Sample test cases :
# Input 1 :

# 11 11 33 50

# Output 1 :

# 113350

# Input 2 :

# 10 10 25 68 74 30 100

# Output 2 :

# 1025687430100

# Input 3 :

# 3 6 9 10 9

# Output 3 :

# 36910

# You are using Python
l=list(map(int,input().split()))
d=[]
for i in l:
    if i not in d:
        d.append(i)
for i in d:
    print(i,end="")