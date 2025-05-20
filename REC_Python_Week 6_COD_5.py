
# Sophie enjoys playing with words and wants to count the number of words in a sentence. She inputs a sentence, saves it to a file, and then reads it from the file to count the words.


# Write a program to determine the number of words in the input sentence.


# File Name: sentence_file.txt
# Input format :

# The input consists of a single line of text containing words separated by spaces.
# Output format :

# The output displays the count of words in the sentence.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# The given test cases fall under the following constraints:

# The length of the input string 'S' ≤ 1000
# Sample test cases :
# Input 1 :

# Four Words In This Sentence

# Output 1 :

# 5

# Input 2 :

# Word WordWord WordWordWord WordWordWordWord

# Output 2 :

# 4

# Input 3 :

 

# Output 3 :

# 0

# You are using Python
s=input()
if s==" ":
    print(0)
else:
    with open("sentence_file.txt",'w') as file:
        file.write(s)

    with open("sentence_file.txt",'r') as file:
        print(len(list((file.read().split(" ")))))