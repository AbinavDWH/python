# Liam is analyzing a list of product IDs from a recent sales report. He needs to determine how frequently each product ID appears and calculate the following metrics:


#     Frequency of each product ID: A dictionary where the key is the product ID and the value is the number of times it appears.
#     Total number of unique product IDs.
#     Average frequency of product IDs: The average count of all product IDs.


# Write a program to read the product IDs, compute these metrics, and output the results.


# Example


# Input:

# 6       //number of product ID

# 101

# 102

# 101

# 103

# 101

# 102 //product IDs


# Output:

# {101: 3, 102: 2, 103: 1}

# Total Unique IDs: 3

# Average Frequency: 2.00


# Explanation:

# Input 6 indicates that you will enter 6 product IDs.

# A dictionary is created to track the frequency of each product ID.

# Input 101: Added with a frequency of 1.

# Input 102: Added with a frequency of 1.

# Input 101: Frequency of 101 increased to 2.

# Input 103: Added with a frequency of 1.

# Input 101: Frequency of 101 increased to 3.

# Input 102: Frequency of 102 increased to 2.

# The dictionary now contains 3 unique IDs: 101, 102, and 103.

# Total Unique is 3.

# The average frequency is 2.00.
# Input format :

# The first line of input consists of an integer n, representing the number of product IDs.

# The next n lines each contain a single integer, each representing a product ID.
# Output format :

# The first line of output displays the frequency dictionary, which maps each product ID to its count.

# The second line displays the total number of unique product IDs, preceded by "Total Unique IDs: ".

# The third line displays the average frequency of the product IDs. This is calculated by dividing the total number of occurrences of all product IDs by the total number of unique product IDs, rounded to two decimal places. It is preceded by "Average Frequency: ".


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ N ≤ 15

# 101 ≤ productID ≤ 200
# Sample test cases :
# Input 1 :

# 6
# 101
# 102
# 101
# 103
# 101
# 102

# Output 1 :

# {101: 3, 102: 2, 103: 1}
# Total Unique IDs: 3
# Average Frequency: 2.00

# Input 2 :

# 5
# 104
# 105
# 104
# 106
# 105

# Output 2 :

# {104: 2, 105: 2, 106: 1}
# Total Unique IDs: 3
# Average Frequency: 1.67

# You are using Python
l=[]
n=int(input())

for i in range(n):
    l.append(int(input()))
    
n_d=[]
for i in l:
    if i not in n_d:
        n_d.append((i))
d={}
for i in (n_d):
    d[i]=l.count(i)
    
summ=0
for i,j in d.items():
    summ+=j
print(f"{d}\nTotal Unique IDs: {len(n_d)}\nAverage Frequency: {round(summ/len(d),2):.2f}")
