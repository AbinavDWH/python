# Ella is analyzing the sales data for a new online shopping platform. She has a record of customer transactions where each customer’s data includes their ID and a list of amounts spent on different items. Ella needs to determine the total amount spent by each customer and identify the highest single expenditure for each customer. 


# Your task is to write a program that computes these details and displays them in a dictionary.
# Input format :

# The first line of input consists of an integer n, representing the number of customers.

# Each of the next n lines contains a numerical customer ID followed by integers representing the amounts spent on different items.
# Output format :

# The output displays a dictionary where the keys are customer IDs and the values are lists containing two integers: the total expenditure and the maximum single expenditure.


# Refer to the sample output for formatting specifications.
# Code constraints :

# 1 ≤ n ≤ 15

# 101 ≤ customerID ≤ 110

# 100 ≤ amount 1000
# Sample test cases :
# Input 1 :

# 2
# 101 100 150 200
# 102 50 75 100

# Output 1 :

# {101: [450, 200], 102: [225, 100]}

# Input 2 :

# 3
# 101 120 130 140 150
# 102 60 90 120
# 103 30 40 50 60 70

# Output 2 :

# {101: [540, 150], 102: [270, 120], 103: [250, 70]}

# You are using Python
n=int(input())
l=[]

for i in range(n):
    l.append(list(map(int,input().split())))
d={}

for i in range(n):
    ml=[]
    for j in range(1,len(l[i])):
        ml.append(l[i][j])
    nl=[]
    nl.append(sum(ml))
    nl.append(max(ml))
    d[l[i][0]]=nl
    ml.clear
    nl.clear
print(d)
    