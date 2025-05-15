# Rishi is working on a program to manipulate a set of integers. The program should allow users to perform the following operations:


#     Find the maximum value in the set.
#     Find the minimum value in the set.
#     Remove a specific number from the set.


# The program should handle these operations based on user input. If the user inputs an invalid operation choice, the program should indicate that the choice is invalid.
# Input format :

# The first line contains space-separated integers that will form the initial set. Each integer x is separated by a space.

# The second line contains an integer ch, representing the user's choice:

#     1 to find the maximum value
#     2 to find the minimum value
#     3 to remove a specific number from the set 

# If ch is 3, the third line contains an integer n1, which is the number to be removed from the set.
# Output format :

# The first line of output prints the original set in descending order.

# For choice 1: Print the maximum value from the set.

# For choice 2: Print the minimum value from the set.

# For choice 3: Print the set after removing the specified number, in descending order.

# For invalid choices: Print "Invalid choice".


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ Number of integers in the set ≤ 100

# 1 ≤ Choice (ch) ≤ 3
# Sample test cases :
# Input 1 :

# 1 2 3 4 5
# 1

# Output 1 :

# {5, 4, 3, 2, 1}
# 5

# Input 2 :

# 3 4 5 6 8 9
# 2

# Output 2 :

# {9, 8, 6, 5, 4, 3}
# 3

# Input 3 :

# 5 4 3 2 1
# 3
# 2

# Output 3 :

# {5, 4, 3, 2, 1}
# {5, 4, 3, 1}

# Input 4 :

# 1 5 6 8 2
# 3
# 8

# Output 4 :

# {8, 6, 5, 2, 1}
# {6, 5, 2, 1}

# Input 5 :

# 6 7 5 3 
# 4

# Output 5 :

# {7, 6, 5, 3}
# Invalid choice

# You are using Python
def display(*arr):
    print("{",end="")
    for i in range(len(arr)):
        print(arr[i],end="")
        if(i!=len(arr)-1):
            print(", ",end="")
    print("}")
l=list(map(int,input().split()))
n=int(input())
d=0
if(n==3):
    d=int(input())
l.sort(reverse=True)
display(*l)

if n==1:
    print(max(l))
elif n==2:
    print(min(l))
elif n==3:
    if d in l:
        l.remove(d)
    display(*l)
else:
    print("Invalid choice")
    