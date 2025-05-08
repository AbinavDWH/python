# magine you are developing a text analysis tool for a cybersecurity company. Your task is to create a function that analyzes input strings to categorize and count the characters into four categories: uppercase letters, lowercase letters, digits, and special characters. The company needs this tool to process log files and identify potential security threats.


# Function Signature: analyze_string(input_string)
# Input format :

# The input consists of a single string (without space), which may include uppercase letters, lowercase letters, digits, and special characters.
# Output format :

# The first line contains an integer representing the count of uppercase letters in the format "Uppercase letters: [count]".

# The second line contains an integer representing the count of lowercase letters in the format "Lowercase letters: [count]".

# The third line contains an integer representing the count of digits in the format "Digits: [count]".

# The fourth line contains an integer representing the count of special characters in the format "Special characters: [count]".


# Refer to the sample output for the formatting specifications.
# Code constraints :

# In this scenario, the given test cases will fall under the following constraints:

# 1 ≤ Length of the input string ≤ 100
# Sample test cases :
# Input 1 :

# Hello123

# Output 1 :

# Uppercase letters: 1
# Lowercase letters: 4
# Digits: 3
# Special characters: 0

# Input 2 :

# 12345

# Output 2 :

# Uppercase letters: 0
# Lowercase letters: 0
# Digits: 5
# Special characters: 0

def analyze_string(input_string):
    l=list(input_string.strip())
    up,lo,di,sp=0,0,0,0
    for i in l:
        if i.isalpha() and i.isupper():
            up+=1
        elif i.isalpha() and i.islower():
            lo+=1
        elif i.isdigit():
            di+=1
        else:
            sp+=1
    return up,lo,di,sp

input_string = input()
uppercase_count, lowercase_count, digit_count, special_count = analyze_string(input_string)

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Special characters:", special_count)