# You are given a string and width .
# Your task is to wrap the string into a paragraph of width



# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

#     string string: a long string
#     int max_width: the width to wrap to

# Returns

#     string: a single string with newline characters ('\n') where the breaks should be

# Input Format

# The first line contains a string,
# .
# The second line contains the width,

# .

# Constraints

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

# def wrap(string, max_width):
#     if len(string)<max_width:
#         return string
#     s=string[:max_width]
#     new_string=string[max_width:]
    # return (s+"\n"+wrap(new_string,max_width))
# def wrap(string, max_width):
#     # Using textwrap module to wrap the string
#     wrapped_string = textwrap.fill(string, max_width)
#     return wrapped_string
def wrap(string, max_width):
    string= "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])
    return string
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)