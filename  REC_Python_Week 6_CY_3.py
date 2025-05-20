
# In the enchanted realm of Academia, you, the Academic Alchemist, are bestowed with a magical quill and a parchment to weave the grades of aspiring students into a tapestry of academic brilliance. 


# The mission is to craft a Python program that empowers faculty members to enter student grades for any two subjects, stores these magical grades in a mystical file, and then, with a wave of your virtual wand, calculates the GPA to unveil the true essence of academic achievement.
# Input format :

# The input format is a string representing the student's name, any two subjects, and corresponding grades.

# After entering grades, they can type 'done' when prompted for the student's name.
# Output format :

# The output should display the (average of grades) calculated GPA with a precision of two decimal places.

# The magical grades will be saved in a mystical file named "magical_grades.txt".


# Refer to the sample output for format specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# The grades should be from 0 to 100.
# Sample test cases :
# Input 1 :

# Alice
# Math
# 95
# English
# 88
# done

# Output 1 :

# 91.50

# Input 2 :

# David
# Literature
# 78
# Spanish
# 92
# done

# Output 2 :

# 85.00

# You are using Python
n=input()
s1=input()
n1=int(input())
s2=input()
n2=int(input())
n3=input()

try:
    if n3=="done":
        print(f"{(n1+n2)/2:.2f}")
    else:
        raise Exception()
except Exception() as e:
    print("")
    