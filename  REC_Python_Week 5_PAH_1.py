# Maya wants to create a dictionary that maps each integer from 1 to a given number n to its square. She will use this dictionary to quickly reference the square of any number up to n. 


# Help Maya generate this dictionary based on the input she provides.
# Input format :

# The input consists of an integer n, representing the highest number for which Maya wants to calculate the square.
# Output format :

# The output displays the generated dictionary where each key is an integer from 1 to n, and the corresponding value is its square.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 20
# Sample test cases :
# Input 1 :

# 5

# Output 1 :

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Input 2 :

# 7

# Output 2 :

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# You are using Python
n=int(input())

d={}

for i in range(1,n+1):
    d[i]=i*i
print(d)