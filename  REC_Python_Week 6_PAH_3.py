# Peter manages a student database and needs a program to add students. For each student, Alex inputs their ID and name. The program checks for duplicate IDs and ensures the database isn't full.


# If a duplicate or a full database is detected, an appropriate error message is displayed. Otherwise, the student is added, and a confirmation message is shown. The database has a maximum capacity of 30 students, and each student must have a unique ID.
# Input format :

# The first line contains an integer n, representing the number of students to be added to the school database.

# The next n lines each contain two space-separated values, representing the student's ID (integer) and the student's name (string).
# Output format :

# The output will depend on the actions performed in the code.


# If a student is added to the database, the output will display: "Student with ID [ID number] added to the database."

# If there is an exception due to a duplicate student ID, the output will display: "Exception caught. Error: Student ID already exists."

# If there is an exception due to the database being full, the output will display: "Exception caught. Error: Student database is full."


# Refer to the sample outputs for the formatting specifications.
# Code constraints :

# The given test case will fall under the following constraints:

# MAX_CAPACITY = 30.

# 1 ≤ n ≤ MAX_CAPACITY.

# 1 ≤ student ID ≤ 10.

# 1 ≤ length of student’s name ≤ 100

# Each student ID must be a positive integer.
# Sample test cases :
# Input 1 :

# 3
# 16 Sam
# 87 Sabari
# 43 Dani

# Output 1 :

# Student with ID 16 added to the database.
# Student with ID 87 added to the database.
# Student with ID 43 added to the database.

# Input 2 :

# 3
# 44 Udhesh
# 33 Sandy
# 44 Keerthi

# Output 2 :

# Student with ID 44 added to the database.
# Student with ID 33 added to the database.
# Exception caught. Error: Student ID already exists.

# Input 3 :

# 32
# 32 zen
# 23 jazz
# 16 sam
# 87 santhiya
# 43 dominic
# 90 felicia
# 17 tera
# 85 wednesday
# 81 sayari
# 39 danny
# 55 udhesh
# 36 nani
# 21 cheenu
# 12 Sakshi
# 49 madhan
# 33 bons
# 41 Ambika
# 30 Sandy
# 47 Charu
# 59 Theju
# 34 Sabari
# 56 Udhesh
# 40 Babu
# 42 Sandeep
# 102 nancy
# 26 saxy
# 13 doll
# 11 craven
# 211 kanaga
# 94 veronic
# 47 jansi
# 33 yalini

# Output 3 :

# Student with ID 32 added to the database.
# Student with ID 23 added to the database.
# Student with ID 16 added to the database.
# Student with ID 87 added to the database.
# Student with ID 43 added to the database.
# Student with ID 90 added to the database.
# Student with ID 17 added to the database.
# Student with ID 85 added to the database.
# Student with ID 81 added to the database.
# Student with ID 39 added to the database.
# Student with ID 55 added to the database.
# Student with ID 36 added to the database.
# Student with ID 21 added to the database.
# Student with ID 12 added to the database.
# Student with ID 49 added to the database.
# Student with ID 33 added to the database.
# Student with ID 41 added to the database.
# Student with ID 30 added to the database.
# Student with ID 47 added to the database.
# Student with ID 59 added to the database.
# Student with ID 34 added to the database.
# Student with ID 56 added to the database.
# Student with ID 40 added to the database.
# Student with ID 42 added to the database.
# Student with ID 102 added to the database.
# Student with ID 26 added to the database.
# Student with ID 13 added to the database.
# Student with ID 11 added to the database.
# Student with ID 211 added to the database.
# Student with ID 94 added to the database.
# Exception caught. Error: Student database is full.

# You are using Python
n=int(input())
l=[]
for i in range(n):
    n=list(input().split())
    l.append(n)
j=0
with open('summa.txt','a+') as file:
    for i in range(len(l)):
        if j>=30:
            print("Exception caught. Error: Student database is full.")
            break
        file.seek(0)
        content=file.read()
        if l[i][0] in content:
            print("Exception caught. Error: Student ID already exists.")
            break
        file.write("Student with ID "+l[i][0]+" added to the database."+"\n")
        j+=1
        print("Student with ID "+l[i][0]+" added to the database.")