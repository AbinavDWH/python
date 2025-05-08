
# Ella is designing a messaging application that needs to handle long text messages efficiently. To optimize storage and transmission, she plans to implement a text compression feature that replaces consecutive repeated characters with the character followed by its count, while leaving non-repeated characters unchanged. 


# Help Ella create a recursive function to achieve this compression without altering the original message's meaning.


# Function Specification: def compress_string(*args)
# Input format :

# The input consists of a single line containing the string to be compressed.
# Output format :

# The output consists of a single line containing the compressed string.


# Refer to the sample output for the formatting specifications.
# Code constraints :

# In this scenario, the given test cases will fall under the following constraints:

# 1 ≤ The length of the input string ≤ 30

# The input string s consists of lowercase and uppercase letters only.
# Sample test cases :
# Input 1 :

# aaaBBBccc

# Output 1 :

# a3B3c3

# Input 2 :

# aabbbccccAAAAABBBBBB

# Output 2 :

# a2b3c4A5B6

# Input 3 :

# efghijk

# Output 3 :

# efghijk

# You are using Python
def com(s):
    def h(index):
        if index>=len(s):
            return ""
        count=1
        while index + count <len(s) and  s[index] ==s[index+count]:
            count+=1
        part=s[index]+(str(count) if count > 1 else"")
        return part+h(index+count)
    return h(0)

s=input()
print(com(s))