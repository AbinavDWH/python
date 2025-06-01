# Arjun is monitoring hourly temperature data recorded continuously for multiple days. He needs to calculate the average temperature for each day based on 24 hourly readings. 


# Help him to implement the task using the numpy package.


# Formula:

# Reshape the temperature readings into rows where each row has 24 readings (one day).

# Average temperature per day = mean of 24 hourly readings in each row.
# Input format :

# The first line of input consists of an integer value, n, representing the total number of temperature readings.

# The second line of input consists of n floating-point values separated by spaces, representing hourly temperature readings.
# Output format :

# The output prints: avg_per_day


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# n is a multiple of 24

# 24 ≤ n ≤ 2400
# Sample test cases :
# Input 1 :

# 30
# 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0 30.0

# Output 1 :

# [30.]

# Input 2 :

# 24
# -5.0 -4.0 -3.0 -2.0 -1.0 0.0 1.0 2.0 3.0 4.0 5.0 6.0 -5.0 -4.0 -3.0 -2.0 -1.0 0.0 1.0 2.0 3.0 4.0 5.0 6.0

# Output 2 :

# [0.5]

# Input 3 :

# 72
# 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0 25.0 26.0 27.0 28.0 29.0 30.0 31.0 32.0 33.0 34.0 35.0 36.0 37.0 38.0 39.0 40.0 41.0 42.0 43.0 44.0 45.0 46.0 47.0 48.0 49.0 50.0 51.0 52.0 53.0 54.0 55.0 56.0 57.0 58.0 59.0 60.0 61.0 62.0 63.0 64.0 65.0 66.0 67.0 68.0 69.0 70.0 71.0 72.0

# Output 3 :

# [12.5 36.5 60.5]

import numpy as np

# Input the total number of temperature readings
n = int(input())

# Input the hourly temperature readings
temperature_readings = list(map(float, input().split()))

# Reshape the readings into rows where each row has 24 readings (one day)
temperature_array = np.array(temperature_readings).reshape(-1, 24)

# Calculate the average temperature for each day
avg_per_day = np.mean(temperature_array, axis=1)

# Print the result
print(avg_per_day)