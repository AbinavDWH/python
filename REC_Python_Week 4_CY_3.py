# Create a program for a mathematics competition where participants need to find the smallest positive divisor of a given integer n. Your program should efficiently determine this divisor using the min() function and display the result.
# Input format :

# The input consists of a single positive integer n, representing the number for which the smallest positive divisor needs to be found.
# Output format :

# The output prints the smallest positive divisor of the input integer in the format: "The smallest positive divisor of [n] is: [smallest divisor]".


# Refer to the sample output for the exact format.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 10000
# Sample test cases :
# Input 1 :

# 24

# Output 1 :

# The smallest positive divisor of 24 is: 2

# Input 2 :

# 9

# Output 2 :

# The smallest positive divisor of 9 is: 3

# You are using Python
n=int(input())
d=[]
for i in range(2,n+1):
    if(n%i==0):
        d.append(i)
if(len(d)!=0):
    
    print("The smallest positive divisor of ",n,"is :",min(d))
else:
    print("The smallest positive divisor of ",n,"is :",1)