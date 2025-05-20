# Tara is a content manager who needs to perform case conversions for various pieces of text and save the results in a structured manner.


# She requires a program to take a user's input string, save it in a file, and then retrieve and display the string in both upper-case and lower-case versions. Help her achieve this task efficiently.


# File Name: text_file.txt
# Input format :

# The input consists of a single line containing a string provided by the user.
# Output format :

# The first line displays the original string read from the file in the format: "Original String: {original_string}".

# The second line displays the upper-case version of the original string in the format: "Upper-Case String: {upper_case_string}".

# The third line displays the lower-case version of the original string in the format: "Lower-Case String: {lower_case_string}".


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The input string can contain alphanumeric characters, spaces, and special symbols.

# 5 ≤ length of the input string ≤ 500
# Sample test cases :
# Input 1 :

# #SpecialSymBoLs1234

# Output 1 :

# Original String: #SpecialSymBoLs1234
# Upper-Case String: #SPECIALSYMBOLS1234
# Lower-Case String: #specialsymbols1234

# Input 2 :

# LoReM iPsUm D0l0r

# Output 2 :

# Original String: LoReM iPsUm D0l0r
# Upper-Case String: LOREM IPSUM D0L0R
# Lower-Case String: lorem ipsum d0l0r

# Input 3 :

# 1abc!@#AbC!@#123

# Output 3 :

# Original String: 1abc!@#AbC!@#123
# Upper-Case String: 1ABC!@#ABC!@#123
# Lower-Case String: 1abc!@#abc!@#123

# You are using Python
s=input()
l=list(s)

with open("test_file.txt",'w') as file:
    file.write("Original String: ")
    for i in l:
        file.write(i)
    file.write("\n")
    file.write("Upper-Case String: ")
    for i in l:
        if i.isalpha():
            file.write(i.upper())
        else:
            file.write(i)
    file.write("\n")
    file.write("Lower-Case String: ")
    for i in l:
        if i.isalpha():
            file.write(i.lower())
        else:
            file.write(i)


            
    
with open("test_file.txt",'r') as file:
    co=file.read()
    print(co)