# Imagine you are tasked with developing a function for calculating the total cost of an item after applying a sales tax. The sales tax rate is equal to 0.08 and it is defined as a global variable.


# The function should accept the cost of the item as a parameter, calculate the tax amount, and return the total cost.


# Additionally, the program should display the item cost, sales tax rate, and total cost to the user.


# Function Signature:  total_cost(item_cost)
# Input format :

# The input consists of a single line containing a positive floating-point number representing the cost of the item.
# Output format :

# The output consists of three lines:

# "Item Cost:" followed by the cost of the item formatted to two decimal places.

# "Sales Tax Rate:" followed by the sales tax rate in percentage.

# "Total Cost:" followed by the calculated total cost after applying the sales tax, formatted to two decimal places.


# Refer to the sample output for formatting specifications.
# Code constraints :

# 0 ≤ item_cost ≤ 105
# Sample test cases :
# Input 1 :

# 50.00

# Output 1 :

# Item Cost: $50.00
# Sales Tax Rate: 8.0%
# Total Cost: $54.00

# Input 2 :

# 100.5

# Output 2 :

# Item Cost: $100.50
# Sales Tax Rate: 8.0%
# Total Cost: $108.54

# You are using Python

def total_cost(x):
    return(x+(x*0.08))
item_cost=float(input())
SALES_TAX_RATE=0.08

total_cost = total_cost(item_cost)
print(f"Item Cost: ${item_cost:.2f}")
print(f"Sales Tax Rate: {SALES_TAX_RATE * 100}%")
print(f"Total Cost: ${total_cost:.2f}")