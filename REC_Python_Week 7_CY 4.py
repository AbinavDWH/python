# You are working as a data analyst for a small retail store that wants to track the stock levels of its products. Each product has a unique Name (such as "Toothpaste", "Shampoo", "Soap") and an associated Quantity in stock. Management wants to identify which products have zero stock so they can be restocked.


# Write a Python program using the pandas library to help with this task. The program should:


#     Read the number of products, n.
#     Read n lines, each containing the Name of the product and its Quantity, separated by a space.
#     Convert this data into a pandas DataFrame.
#     Identify and display the Name and Quantity of products with zero stock.
#     If no products have zero stock, display: No products with zero stock.

# Input format :

# The first line contains an integer n, the number of products.


# The next n lines each contain:

# <Product_ID> <Quantity>

# where <Product_ID> is a single word (e.g., "Shampoo") and <Quantity> is a non-negative integer (e.g., 5).
# Output format :

# The first line of output prints:

# Products with Zero Stock:


# If there are any products with zero stock, the following lines print the pandas DataFrame showing those products with two columns: Product_ID and Quantity.


# The column headers Product_ID and Quantity are printed in the second line.

# Each subsequent line shows the product's name and quantity, aligned under the respective headers, with no index column.


# The output formatting (spacing and alignment) follows the default pandas to_string(index=False) style.

# If no products have zero stock, print:

# No products with zero stock.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 100

# Product names are single English words, no spaces.

# Quantities are integers from 0 to 10,000.
# Sample test cases :
# Input 1 :

# 3
# P101 10
# P102 0
# P103 5

# Output 1 :

# Products with Zero Stock:
# Product_ID  Quantity
#       P102         0

# Input 2 :

# 4
# M1 7
# M2 8
# M3 9
# M4 1

# Output 2 :

# Products with Zero Stock:
# No products with zero stock.

# You are using Python
import pandas as pd

# Input the number of products
n = int(input())

# Input product data
products = []
for _ in range(n):
    products.append(input().split())

# Create a DataFrame
data = pd.DataFrame(products, columns=['Product_ID', 'Quantity'])

# Convert 'Quantity' column to numeric
data['Quantity'] = pd.to_numeric(data['Quantity'])

# Filter products with zero stock
zero_stock = data[data['Quantity'] == 0]

# Output the result
print("Products with Zero Stock:")
if zero_stock.empty:
    print("No products with zero stock.")
else:
    print(zero_stock.to_string(index=False))