
# A retail store requires a program to calculate the total cost of purchasing a product based on its price and quantity. The program performs validation to ensure valid inputs and handles specific error conditions using exceptions:


#     Price Validation: If the price is zero or less, raise a ValueError with the message: "Invalid Price".
#     Quantity Validation: If the quantity is zero or less, raise a ValueError with the message: "Invalid Quantity".
#     Cost Threshold: If the total cost exceeds 1000, raise RuntimeError with the message: "Excessive Cost".

# Input format :

# The first line of input consists of a double value, representing the price of a product.

# The second line consists of an integer, representing the quantity of the product.
# Output format :

# If the calculation is successful, print the total cost rounded to one decimal place.

# If the price is zero or less prints "Invalid Price".

# If the quantity is zero or less prints "Invalid Quantity".

# If the total cost exceeds 1000, prints "Excessive Cost".


# Refer to the sample output for formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# -10.0 ≤ price ≤ 100.0

# -1 ≤ quantity ≤ 10000
# Sample test cases :
# Input 1 :

# 20.0
# 5

# Output 1 :

# 100.0

# Input 2 :

# -10.0
# 5

# Output 2 :

# Invalid Price

# Input 3 :

# 20.0
# 60

# Output 3 :

# Excessive Cost

# Input 4 :

# 70.0
# 0

# Output 4 :

# Invalid Quantity

# You are using Python
n1=float(input())
n2=int(input())

try:
    if(n1<=0):
        raise ValueError("Invalid Price")
    elif(n2<=0):
        raise ValueError("Invalid Quantity")
    elif(n2*n1>1000):
        raise RuntimeError("Excessive Cost")
    else:
        print(f"{n1*float(n2)}")
except Exception as c:
    print(c)