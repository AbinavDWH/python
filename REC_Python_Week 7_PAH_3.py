
# You’re analyzing the daily returns of a set of financial assets over a period of time. Each day is represented as a row in a 2D array, where each column represents the return of a specific asset on that day. 



# Your task is to identify which days had all positive returns across every asset using numpy, and output a boolean array indicating these days.

# Input format :
# The first line of input consists of two integer values, rows and cols, separated by a space.

# Each of the next rows lines consists of cols float values representing the returns of the assets for that day.

# Output format :
# The first line of output prints: "Days where all asset returns were positive:"

# The second line of output prints: the boolean array positive_days, indicating True for days where all asset returns were positive and False otherwise.



# Refer to the sample output for the formatting specifications.

# Code constraints :
# The given test cases fall under the following constraints:

# 1 ≤ rows ≤ 1000



# 1 ≤ cols ≤ 1000

# Each asset return is a float number (can be positive, negative, or zero).

# Sample test cases :
# Input 1 :
# 3 4
# 0.01 0.02 0.03 0.04
# 0.05 0.06 0.07 0.08
# -0.01 0.02 0.03 0.04
# Output 1 :
# Days where all asset returns were positive:
# [ True  True False]
# Input 2 :
# 2 3
# 0.1 -0.2 0.3
# 0.0 0.1 -0.2
# Output 2 :
# Days where all asset returns were positive:
# [False False]


