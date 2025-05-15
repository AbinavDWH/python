
# Mia is organizing a list of integers into a series of pairs for his new project. She wants to create pairs of consecutive integers from the list.  The last integer should be paired with None to complete the series. The pairing happens as follows: ((Element 1, Element 2), (Element 2, Element 3)........(Element n, None)).


# Your task is to help Henry by writing a Python program that reads a list of integers, forms these pairs, and displays the result in tuple format.
# Input format :

# The first line of input consists of an integer n, representing the number of elements in the tuple.

# The second line of input contains n space-separated integers, representing the elements of the tuple.
# Output format :

# The output displays a tuple containing pairs of consecutive integers from the input. The last integer in the tuple is paired with 'None'.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 3 ≤ n ≤ 12

# 1 ≤ tuple elements ≤ 100
# Sample test cases :
# Input 1 :

# 3
# 5 10 15

# Output 1 :

# ((5, 10), (10, 15), (15, None))

# Input 2 :

# 4
# 7 14 21 28

# Output 2 :

# ((7, 14), (14, 21), (21, 28), (28, None))

# You are using Python
n=int(input())
l=list(map(int,input().split()))


o_p=[]
for i in range(len(l)):
    
    
    t=[]
    t.append(l[i])
    if i+1>=len(l):
        t.append(None)
    else:
        t.append(l[i+1])
    o_p.append(tuple(t))
print(tuple(o_p))