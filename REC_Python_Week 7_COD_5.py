
# Rekha works in hospital data management and receives patient records with missing or incomplete data. She needs to clean the records by performing the following tasks:


#     Calculate the mean of the available Age values.
#     Replace any missing (NaN) values in the Age column with this mean age.
#     Remove any rows where the Diagnosis value is missing (NaN).
#     Reset the DataFrame index after removing these rows.


# Implement this data cleaning task using the pandas package.
# Input format :

# The first line of input contains an integer n representing the number of patient records.

# The second line contains the CSV header — comma-separated column names (e.g., "Name,Age,Diagnosis,Gender").

# The next n lines each contain one patient record in comma-separated format.
# Output format :

# The first line of output is the text:

# Cleaned Hospital Records:

# The next lines print the cleaned pandas DataFrame (as produced by print(cleaned_df)).

# This will include the updated values of the Age column (with missing ages filled by the mean age), and any rows with missing Diagnosis removed.

# The DataFrame will be displayed using the default pandas print() representation.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# 1 ≤ n ≤ 1000

# The columns include at least Age and Diagnosis among others.

# Age values can be integers or floats, with some missing (NaN).

# Diagnosis values can be strings, some may be missing (NaN).
# Sample test cases :
# Input 1 :

# 5
# PatientID,Name,Age,Diagnosis
# 1,John Doe,45,Flu
# 2,Jane Smith,,Cold
# 3,Bob Lee,50,
# 4,Alice Green,38,Fever
# 5,Tom Brown,,Infection

# Output 1 :

# Cleaned Hospital Records:
#    PatientID         Name        Age  Diagnosis
# 0          1     John Doe  45.000000        Flu
# 1          2   Jane Smith  44.333333       Cold
# 2          4  Alice Green  38.000000      Fever
# 3          5    Tom Brown  44.333333  Infection

# Input 2 :

# 5
# PatientID,Name,Age,Diagnosis
# 101,Mike Ross,29,Asthma
# 102,Rachel Zane,,
# 103,Harvey Specter,47,Cancer
# 104,Donna Paulsen,42,
# 105,Louis Litt,36,Allergy

# Output 2 :

# Cleaned Hospital Records:
#    PatientID            Name   Age Diagnosis
# 0        101       Mike Ross  29.0    Asthma
# 1        103  Harvey Specter  47.0    Cancer
# 2        105      Louis Litt  36.0   Allergy

# You are using Python
import pandas as p
n=int(input())
col=list(map(str,input().split(',')))
l=[]
for i in range(n):
    l.append(list(map(str,input().split(','))))

data = p.DataFrame(l,columns=col)

data['Age']=p.to_numeric(data['Age'],errors='coerce')

mean=data['Age'].mean()

data['Age'].fillna(round(mean,6),inplace=True)

data=data[data['Diagnosis'].notna() &(data['Diagnosis']!='')]

data.reset_index(drop=True,inplace=True)

print("Cleaned Hospital Records:")
print(data)