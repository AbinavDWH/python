# Emily is a librarian who keeps track of books borrowed and returned by her patrons. She maintains four sets of book IDs: the first set represents books borrowed, the second set represents books returned, the third set represents books added to the collection, and the fourth set represents books that are now missing. Emily wants to determine which books are still borrowed but not returned, as well as those that were added but are now missing. Finally, she needs to find all unique book IDs from both results.


# Help Emily by writing a program that performs the following operations on four sets of integers:

#     Compute the difference between the borrowed books (first set) and the returned books (second set).
#     Compute the difference between the added books (third set) and the missing books (fourth set).
#     Find the union of the results from the previous two steps, and sort the final result in descending order.

# Input format :

# The first line of input consists of a list of integers representing borrowed books.

# The second line of input consists of a list of integers representing returned books.

# The third line of input consists of a list of integers representing added books.

# The fourth line of input consists of a list of integers representing missing books.
# Output format :

# The first line of output displays the difference between sets P and Q, sorted in descending order.

# The second line of output displays the difference between sets R and S, sorted in descending order.

# The third line of output displays the union of the differences from the previous two steps, sorted in descending order.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# 1 ≤ set_elements ≤ 50
# Sample test cases :
# Input 1 :

# 1 2 3
# 2 3 4
# 5 6 7
# 6 7 8

# Output 1 :

# [1]
# [5]
# [5, 1]

# Input 2 :

# 5 6 7
# 5 6
# 8 9
# 8 10

# Output 2 :

# [7]
# [9]
# [9, 7]

# You are using Python
p=set(map(int,input().split()))
q=set(map(int,input().split()))
r=set(map(int,input().split()))
s=set(map(int,input().split()))

n_w=p-q
n_d=r-s
print(sorted(list(n_w),reverse=True))
print(sorted(list(n_d),reverse=True))
print(sorted(list(n_w.union(n_d)),reverse=True))
