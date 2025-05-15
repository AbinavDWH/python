
# Tom wants to create a dictionary that lists the first n prime numbers, where each key represents the position of the prime number, and the value is the prime number itself. 


# Help Tom generate this dictionary based on the input she provides.
# Input format :

# The input consists of an integer n, representing the number of prime numbers Tom wants to generate.
# Output format :

# The output displays the generated dictionary where each key is an integer from 1 to n, and the corresponding value is the prime number.


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 30
# Sample test cases :
# Input 1 :

# 4

# Output 1 :

# {1: 2, 2: 3, 3: 5, 4: 7}

# Input 2 :

# 20

# Output 2 :

# {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13, 7: 17, 8: 19, 9: 23, 10: 29, 11: 31, 12: 37, 13: 41, 14: 43, 15: 47, 16: 53, 17: 59, 18: 61, 19: 67, 20: 71}
# # 

# You are using Python
import math
n=int(input())

def isprime(p):
    for i in range(2,int(math.sqrt(p))+1):
        if p%i==0:
            return False
    return True
            
d={}

i=0
num=2
while True:
    if isprime(num):
        i+=1
        d[i]=num
    num+=1
    if(i==n):
        break

print(d)