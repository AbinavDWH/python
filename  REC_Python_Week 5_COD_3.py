# James is managing a list of inventory items in a warehouse. Each item is recorded as a tuple, where the first element is the item ID and the second element is a list of quantities available for that item. James needs to filter out all quantities that are above a certain threshold to find items that have a stock level above this limit. 


# Help James by writing a program to process these tuples, filter the quantities from all the available items, and display the results.


# Note:

# Use the filter() function to filter out the quantities greater than the specified threshold for each item's stock list.
# Input format :

# The first line of input consists of an integer N, representing the number of tuples.

# The next N lines each contain a tuple in the format (ID, [quantity1, quantity2, ...]), where ID is an integer and the list contains integers.

# The final line consists of an integer threshold, representing the quantity threshold.
# Output format :

# The output should be a single line displaying the filtered quantities, space-separated. Each quantity is strictly greater than the given threshold.


# Refer to the sample output for formatting specifications.
# Code constraints :

# 2 ≤ N,ID ≤ 6

# 1 ≤ tuple elements ≤ 50

# 1 ≤ threshold ≤ 20
# Sample test cases :
# Input 1 :

# 2
# (1, [1, 2])
# (2, [3, 4])
# 2

# Output 1 :

# 3 4

# Input 2 :

# 2
# (1, [6, 7])
# (2, [8])
# 6

# Output 2 :

# 7 8

# You are using Python
import ast

n=int(input())
d={}
for i in range(n):
    k,v=ast.literal_eval(input())
    d[k]=v
#print(d)

l=[]

for i in d.values():
    for k in i:
        l.append(k)
#print(l)

th=int(input())

for i in l:
    if( i>th):
        print(i,end=" ")