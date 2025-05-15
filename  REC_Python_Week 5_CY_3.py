# Noah, a global analyst at a demographic research firm, has been tasked with identifying which country experienced the largest population growth over a two-year period. He has a dataset where each entry consists of a country code and its population figures for two consecutive years. Noah needs to determine which country had the highest increase in population and present the result in a specific format. 


# Help Noah by writing a program that outputs the country code with the largest population increase, along with the increase itself.
# Input format :

# The first line of input consists of an integer N, representing the number of countries.

# Each of the following N blocks contains three lines:

#     The first line is a country code.
#     The second line is an integer representing the population of the country in the first year.
#     The third line is an integer representing the population of the country in the second year.

# Output format :

# The output displays the country code and the population increase in the format {code: difference}, where code is the country code and difference is the increase in population.


# Refer to the sample output for formatting specifications.
# Code constraints :

# 1 ≤ N ≤ 15

# 01 ≤ country code ≤ 09

# 1 ≤ population ≤ 10000
# Sample test cases :
# Input 1 :

# 3
# 01
# 1000
# 1500
# 02
# 2000
# 2430
# 03
# 1500
# 3000

# Output 1 :

# {03:1500}

# Input 2 :

# 4
# 01
# 5000
# 5500
# 02
# 6000
# 7200
# 03
# 5500
# 6100
# 04
# 4500
# 5000

# Output 2 :

# {02:1200}

# You are using Python
n=int(input())
d={}

for i in range(n):
    n1=int(input())
    n2=int(input())
    n3=int(input())
    d[n1]=abs(n2-n3)
ke=max(d,key=d.get)
print(f"{{0{ke}:{d[ke]}}}")