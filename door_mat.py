# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#     Mat size must be 

# X. ( is an odd natural number, and is times

#     .)
#     The design should have 'WELCOME' written in the center.
#     The design pattern should only use |, . and - characters.

# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------

# Input Format

# A single line containing the space separated values of
# and

# .

# Constraints

# Output Format

# Output the design pattern.

# Sample Input

# 9 27

# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=list(map(int,input().split()))
s="WELCOME"
for i in range(n[0]):
    if i == n[0]//2:
        new_s=s.center(n[1],"-")
        print(new_s)
    else:
        if i<(n[0])//2:
            l=(".|."*(2*i+1))
          
        else:
            l=(".|."*(2*(n[0]-i-1)+1))
        new_l=l.center(n[1],"-")
        print(new_l)
                        
