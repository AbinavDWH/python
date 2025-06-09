# A software development company wants to classify its employees based on their years of service at the company. They want to categorize employees into three experience levels: Junior (less than 3 years), Mid (3 to 6 years, inclusive), and Senior (more than 6 years).



# Experience Level Classification:

# Junior: Years at Company < 3

# Mid: 3 ≤ Years at Company < 6

# Senior: Years at Company > 5



# You need to create a Python program using the pandas library that reads employee data, processes it into a DataFrame, and adds a new column "Experience Level" to display the appropriate classification for each employee.

# Input format :
# First line: an integer n representing the number of employees.

# Next n lines: each line has a string Name and a floating-point number Years at Company (space-separated).

# Output format :
# First line: "Employee Data with Experience Level:"

# The employee data table printed with no index column, and with columns: Name, Years at Company, Experience Level.



# Refer to the sample output for the formatting specifications.

# Code constraints :
# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 100 – Number of employees will not exceed 100.

# 0 ≤ Years at Company ≤ 50 – Years of service will always be a non-negative number (up to 50).

# Names are single-word strings containing only English alphabets (no spaces).

# Input data is well-formed, so you do not need to handle malformed inputs.

# Sample test cases :
# Input 1 :
# 5
# Alice 2
# Bob 4
# Charlie 7
# Diana 3
# Evan 6
# Output 1 :
# Employee Data with Experience Level:
#    Name  Years at Company Experience Level
#   Alice               2.0           Junior
#     Bob               4.0              Mid
# Charlie               7.0           Senior
#   Diana               3.0              Mid
#    Evan               6.0           Senior
# Input 2 :
# 3
# John 1.5
# Jane 5
# Mark 10
# Output 2 :
# Employee Data with Experience Level:
# Name  Years at Company Experience Level
# John               1.5           Junior
# Jane               5.0              Mid
# Mark              10.0           Senior

import pandas as pd

def classify_experience(years):
    if years < 3:
        return "Junior"
    elif 3 <= years < 6:
        return "Mid"
    else:
        return "Senior"

def main():
    n = int(input())
    data = []

    for _ in range(n):
        line = input().strip()
        name, years = line.split()
        data.append({"Name": name, "Years at Company": float(years)})

    df = pd.DataFrame(data)
    df["Experience Level"] = df["Years at Company"].apply(classify_experience)

    print("Employee Data with Experience Level:")
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()