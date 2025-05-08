# Hussain wants to create a program to calculate a person's BMI (Body Mass Index) based on their weight in kilograms and height in meters. The BMI is a measure of a person's body fat relative to their height.


# Your program should take user input for weight and height, calculate the BMI, and display the result.


# Function Signature: calculate_bmi(weight, height)


# Formula: BMI = Weight/(Height)2
# Input format :

# The first line of input consists of a positive floating-point number, the person's weight in kilograms.

# The second line of input consists of a positive floating-point number, the person's height in meters.
# Output format :

# The output displays "Your BMI is: [BM] followed by a float value representing the calculated BMI, rounded off two decimal points.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The test cases will fall under the following constraints:

# 1.0 ≤ weight ≤ 100.0

# 0.5 ≤ height ≤ 2.5
# Sample test cases :
# Input 1 :

# 70.0
# 1.75

# Output 1 :

# Your BMI is: 22.86

# Input 2 :

# 50.5
# 1.65

# Output 2 :

# Your BMI is: 18.55

weight = float(input())
height = float(input())

# You are using Python
def calculate_bmi(x,y):
    print(f"Your BMI is : {x/(y*y):.2f}")

calculate_bmi(weight, height)