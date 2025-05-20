# In a voting system, a person must be at least 18 years old to be eligible to vote. If a user enters an age below 18, the system should raise a user-defined exception indicating that they are not eligible to vote.
# Input format :

# The input contains a positive integer representing age.
# Output format :

# If the age is less than 18, the output displays "Not eligible to vote".

# Otherwise, the output displays "Eligible to vote".


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ age ≤ 100
# Sample test cases :
# Input 1 :

# 18

# Output 1 :

# Eligible to vote

# Input 2 :

# 12

# Output 2 :

# Not eligible to vote

# You are using Python
n=int(input())
try:
    if n>=18:
        print("Eligible to vote")
    else:
        raise Exception("Not eligible to vote")
except Exception as e:
    print(e)