# Sita works as a sales analyst and needs to analyze monthly sales data for different cities. She receives lists of cities, months, and corresponding sales values and wants to create a pandas DataFrame using a MultiIndex of cities and months.



# Help her to implement this task and calculate total sales for each city.

# Input format :
# The first line of input consists of an integer value, n, representing the number of records.

# The second line of input consists of n space-separated city names.

# The third line of input consists of n space-separated month names.

# The fourth line of input consists of n space-separated float values representing sales for each city-month combination.

# Output format :
# The first line of output prints: "Monthly Sales Data with MultiIndex:"

# The next lines print the DataFrame with MultiIndex (City, Month) and their corresponding sales values.

# The following line prints: "\nTotal Sales Per City:"

# The final lines print the total sales per city, computed by grouping the sales data on city names.



# Refer to the sample output for the formatting specifications.

# Code constraints :
# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 1000

# Cities and months are provided as strings.

# Sales values are floats or integers.

# Each city-month combination is unique.

# Sample test cases :
# Input 1 :
# 4
# NYC NYC LA LA
# Jan Feb Jan Feb
# 100 200 300 400
# Output 1 :
# Monthly Sales Data with MultiIndex:
#             Sales
# City Month       
# NYC  Jan    100.0
#      Feb    200.0
# LA   Jan    300.0
#      Feb    400.0

# Total Sales Per City:
#       Sales
# City       
# LA    700.0
# NYC   300.0
# Input 2 :
# 6
# Boston Boston Miami Miami Miami Boston
# Mar Apr May May Mar Apr
# 50 60 70 80 90 100
# Output 2 :
# Monthly Sales Data with MultiIndex:
#               Sales
# City   Month       
# Boston Mar     50.0
#        Apr     60.0
# Miami  May     70.0
#        May     80.0
#        Mar     90.0
# Boston Apr    100.0

# Total Sales Per City:
#         Sales
# City         
# Boston  210.0
# Miami   240.0


import pandas as pd

# Read input
n = int(input())
cities = input().split()
months = input().split()
sales = list(map(float, input().split()))

# Create MultiIndex
index = pd.MultiIndex.from_tuples(zip(cities, months), names=["City", "Month"])

# Create DataFrame
df = pd.DataFrame({"Sales": sales}, index=index)

# Display the DataFrame
print("Monthly Sales Data with MultiIndex:")
print(df)

# Calculate total sales per city
total_sales = df.groupby(level="City").sum()

print("\nTotal Sales Per City:")
print(total_sales)
import pandas as pd

# Read input
n = int(input())
cities = input().split()
months = input().split()
sales = list(map(float, input().split()))

# Create MultiIndex
index = pd.MultiIndex.from_tuples(zip(cities, months), names=["City", "Month"])

# Create DataFrame
df = pd.DataFrame({"Sales": sales}, index=index)

# Display the DataFrame
print("Monthly Sales Data with MultiIndex:")
print(df)

# Calculate total sales per city
total_sales = df.groupby(level="City").sum()

print("\nTotal Sales Per City:")
print(total_sales)
