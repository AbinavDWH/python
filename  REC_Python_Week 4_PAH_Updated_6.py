
# Create a Python program to monitor temperatures in a greenhouse using two sensors. Calculate and display the absolute temperature difference between the two sensor readings to ensure proper temperature control.


# Note: Use the abs() built-in function.
# Input format :

# The first line consists of a floating-point number, representing the temperature reading from Sensor 1.

# The second line consists of a floating-point number, representing the temperature reading from Sensor 2.
# Output format :

# The output displays the absolute temperature difference between Sensor 1 and Sensor 2, rounded to two decimal places.


# Refer to the sample output for the exact format.
# Code constraints :

# The given test cases fall under the following constraints:

# -100.0 ≤ temperature ≤ 100.0
# Sample test cases :
# Input 1 :

# 33.2
# 26.7

# Output 1 :

# Temperature difference: 6.50 °C

# Input 2 :

# -7.8
# 23.6

# Output 2 :

# Temperature difference: 31.40 °C

# You are using Python
n1=float(input())
n2=float(input())

print(f"Temperature difference: {abs(n1-n2):.2f} \u00b0C")