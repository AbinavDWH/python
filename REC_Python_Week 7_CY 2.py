
# Rekha works as an e-commerce data analyst. She receives transaction data containing purchase dates and needs to extract the month and day from these dates using the pandas package.


# Help her implement this task by performing the following steps:

# Convert the Purchase Date column to datetime format, treating invalid date entries as NaT (missing).


# Create two new columns:

# Purchase Month, containing the month (as an integer) extracted from the Purchase Date.

# Purchase Day, containing the day (as an integer) extracted from the Purchase Date. Keep the rest of the data as is.
# Input format :

# The first line of input contains an integer n, representing the number of records.

# The second line contains the CSV header — comma-separated column names.

# The next n lines each contain a transaction record in comma-separated format.
# Output format :

# The first line of output is the text:

# Transformed E-commerce Transaction Data:

# The next lines print the pandas DataFrame with:

# The original columns (including Purchase Date, which is now in datetime format or NaT if invalid).

# Two additional columns: Purchase Month and Purchase Day.

# The output uses the default pandas DataFrame string representation as produced by print(transformed_df).


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 1000

# The CSV data includes at least a Purchase Date column (case-sensitive).

# Purchase Date values may include valid and invalid date formats.

# Invalid date entries in the Purchase Date column are set to NaT (missing).

# The CSV data includes additional columns, which should remain unchanged.
# Sample test cases :
# Input 1 :

# 3
# Customer,Purchase Date
# Alice,2023-05-15
# Bob,2023-06-20
# Charlie,2023-07-01

# Output 1 :

# Transformed E-commerce Transaction Data:
#   Customer Purchase Date  Purchase Month  Purchase Day
# 0    Alice    2023-05-15               5            15
# 1      Bob    2023-06-20               6            20
# 2  Charlie    2023-07-01               7             1

# Input 2 :

# 2
# Customer,Purchase Date
# David,2023-01-10
# Emma,2023-12-25

# Output 2 :

# Transformed E-commerce Transaction Data:
#   Customer Purchase Date  Purchase Month  Purchase Day
# 0    David    2023-01-10               1            10
# 1     Emma    2023-12-25              12            25

# You are using Python
import pandas as pd

# Input the number of records
n = int(input())

# Input the CSV header
columns = list(map(str, input().split(',')))

# Input the transaction records
records = []
for _ in range(n):
    records.append(list(map(str, input().split(','))))

# Create a DataFrame
data = pd.DataFrame(records, columns=columns)

# Convert 'Purchase Date' column to datetime format, treating invalid entries as NaT
data['Purchase Date'] = pd.to_datetime(data['Purchase Date'], errors='coerce')

# Extract month and day into new columns
data['Purchase Month'] = data['Purchase Date'].dt.month
data['Purchase Day'] = data['Purchase Date'].dt.day

# Output the transformed DataFrame
print("Transformed E-commerce Transaction Data:")
print(data)