
# Rekha is a meteorologist analyzing rainfall data collected over 5 years, with monthly rainfall recorded for each year. She wants to find the total rainfall each year and also identify the month with the maximum rainfall for every year. 


# Help her to implement the task using the numpy package.


# Formula:

# Yearly total rainfall = sum of all 12 months’ rainfall for each year

# Month with max rainfall = index of the maximum rainfall value within the 12 months for each year (0-based index)
# Input format :

# The input consists of 5 lines.

# Each line contains 12 floating-point values separated by spaces, representing the rainfall data (in mm) for each month of that year.
# Output format :

# The first line of output prints: yearly_totals

# The second line of output prints: max_rainfall_months


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:


# Rainfall values are non-negative and can be fractional

# Typical rainfall range per month: 0.0 to 1000.0 mm
# Sample test cases :
# Input 1 :

# 1.0  2.0  3.0  4.0  5.0  6.0  7.0  8.0  9.0  10.0  11.0  12.0
# 2.0  3.0  4.0  5.0  6.0  7.0  8.0  9.0  10.0 11.0  12.0  13.0
# 3.0  4.0  5.0  6.0  7.0  8.0  9.0  10.0 11.0 12.0  13.0  14.0
# 4.0  5.0  6.0  7.0  8.0  9.0  10.0 11.0 12.0 13.0  14.0  15.0
# 5.0  6.0  7.0  8.0  9.0  10.0 11.0 12.0 13.0 14.0  15.0  16.0

# Output 1 :

# [ 78.  90. 102. 114. 126.]
# [11 11 11 11 11]

# Input 2 :

# 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
# 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

# Output 2 :

# [0. 0. 0. 0. 0.]
# [0 0 0 0 0]

# You are using Python
import numpy as np

# Input rainfall data for 5 years
rainfall_data = []
for _ in range(5):
    rainfall_data.append(list(map(float, input().split())))

# Convert the data into a NumPy array
rainfall_array = np.array(rainfall_data)

# Calculate yearly total rainfall
yearly_totals = np.sum(rainfall_array, axis=1)

# Find the month with maximum rainfall for each year (0-based index)
max_rainfall_months = np.argmax(rainfall_array, axis=1)

# Print the results
print(yearly_totals)
print(max_rainfall_months)