
# Alex is working with grayscale pixel intensities from an old photo that has been scanned in a single row. To detect edges in the image, Alex needs to calculate the differences between each pair of consecutive pixel intensities. 


# Your task is to write a program that performs this calculation and returns the result as a tuple of differences.
# Input format :

# The first line of input contains an integer n, representing the number of pixel intensities.

# The second line contains n space-separated integers representing the pixel intensities.
# Output format :

# The output displays a tuple containing the absolute differences between consecutive pixel intensities.


# Refer to the sample output for format specifications.
# Code constraints :

# 5 ≤ n ≤ 20

# 0 ≤ tuple element ≤ 255
# Sample test cases :
# Input 1 :

# 5
# 200 100 20 80 10

# Output 1 :

# (100, 80, 60, 70)

# Input 2 :

# 6
# 171 254 229 150 17 227

# Output 2 :

# (83, 25, 79, 133, 210)

# You are using Pyth
n=int(input())
l=list(map(int,input().split()))

n_l=[]

for i in range(n-1):
    n_l.append(abs(l[i]-l[i+1]))
    
print(tuple(n_l))